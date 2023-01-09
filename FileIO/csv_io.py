import csv
import pathlib
import pprint


# csvファイルの読み込み(open())
def input_csv_1(csv_file):
    with open(csv_file) as f:
        pprint.pprint(f.read())
        

# csvファイルの読み込み(コンストラクタ使用)
def input_csv_2(csv_file):
    with open(csv_file) as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)