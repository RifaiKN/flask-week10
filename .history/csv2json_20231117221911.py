import csv
import json
import os

base_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(base_dir, 'static', 'datapribadi.csv')


def csv2json(path_file):
    with open(path_file, 'r') as file_csv:
        csv_reader = csv.reader(file_csv)
        data = [baris for baris in csv_reader]

    data_json = json.dumps(data)
    return data_json


def tampilkan_data():
    if os.path.exists(csv_file_path):
        data_json = csv2json(csv_file_path)
        return data_json
    else:
        return 'File CSV tidak ditemukan.'
