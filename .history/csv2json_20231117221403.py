import csv
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(base_dir, 'static', 'assets', 'datapribadi.csv')


def csv_ke_json(path_file):
    with open(path_file, 'r') as file_csv:
        pembaca_csv = csv.reader(file_csv)
        data = [baris for baris in pembaca_csv]

    data_json = json.dumps(data)
    return data_json


def tampil_data():
    if os.path.exists(csv_file_path):
        data_json = csv_ke_json(csv_file_path)
        return data_json
    else:
        return 'File CSV tidak ditemukan.'
