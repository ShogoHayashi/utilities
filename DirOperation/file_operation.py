"""
Created on Fri Jan 6 2023
@author: ShogoHayashi
"""

import pathlib


# ディレクトリ内のファイルと子ディレクトリの一覧を取得する関数
def file_acquisition(folder_path):
    p_folder = pathlib.Path(folder_path)
    