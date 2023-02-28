from pathlib import Path
import csv
import json
import pickle
import os


def get_dir_size(path='.') -> int:
    result = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                result += entry.stat().st_size
            elif entry.is_dir():
                result += get_dir_size(entry.path)
    return result


def get_size(path='.') -> int:
    if os.path.isfile(path):
        return os.path.getsize(path)
    elif os.path.isdir(path):
        return get_dir_size(path)


def direct_info(direct: Path):
    json_data = {}
    fieldnames = ['name', 'path', 'size', 'file_or_dir']
    rows = []
    with open('direct_info.json', 'w') as f_json, open('direct_info.csv', 'w', newline='', encoding='utf-8') as f_csv,\
            open('direct_info.pickle', 'wb') as f_pickle:
        for dir_path, dir_name, file_name in os.walk(direct):
            json_data.setdefault(dir_path, {})
            for dir in dir_name:
                size = get_size(dir_path + '/' + dir)
                json_data[dir_path].update({dir: {'size': size, 'file_or_dir': 'directory'}})
                rows.append({'name': dir, 'path': dir_path, 'size': size, 'file_or_dir': 'directory'})
            for fi in file_name:
                size = get_size(dir_path + '/' + fi)
                json_data[dir_path].update({fi: {'size': size, 'file_or_dir': 'file'}})
                rows.append({'name': fi, 'path': dir_path, 'size': size, 'file_or_dir': 'file'})
            print(f'{dir_path = }\n{dir_name = }\n{file_name = }\n')
        json.dump(json_data, f_json, indent=2)
        writer = csv.DictWriter(f_csv, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        pickle.dump(f'{pickle.dumps(json_data)}', f_pickle)


if __name__ == '__main__':
    direct_info(Path('/Users/mac/Desktop/GeekBrain/second_python/all_tasks'))
