"""
Created on Fri Jan 6 2023
@author: ShogoHayashi
"""

import pathlib
import pprint


# ディレクトリ内のファイルと子ディレクトリの一覧を取得する関数
def file_acquisition(folder_path):
    p_folder = pathlib.Path(folder_path)
    # 一覧を出力する
    pprint.pprint(list(p_folder.iterdir()))
    # 以下のようにPathオブジェクトを引数にするとエラーが起きる
    # pprint.pprint(list(pathlib.Path(folder_path)))
    
    ディレクトリのみ一覧を出力する
    [x for x in p.iterdir() if x.is_dir()]
    

# ディレクトリ内のファイルと子ディレクトリの一覧を再帰的に取得する関数
def file_acquisition_glob(folder_path, extension = ""):
    p_folder = pathlib.Path(folder_path)
    # 一覧を出力する
    pprint.pprint(list(p_folder.glob(extension)))
    
    # extensionには求めたいファイルの拡張子
    # 例えば.txtが欲しい時は"**/*.txt"とする。
    # *には任意の何かが入るということ
    

# ファイルの情報を確認
def file_information(file_path):
    p_file = pathlib.Path(file_path)
    print(f"File Name = {p_file.name}")
    print(f"File Path = {str(p_file)}")
    print(f"File Extension = {p_file.suffix}")
    print(f"File Name Excpt Extension = {p_file.stem}")
    print(f"Folder Name = {p_file.parent.name}")
    print(f"File Size = {p_file.star().st_size} byte")
    print(f"Last Access Time in second = {p_file.star().st_atime} second")
    print(f"Last Update Time in second = {p_file.star().st_mtime} second")
    print(f"Creation Time in second = {p_file.star().st_ctime} second")
    print(f"Creator is  = {p_file.star().st_creator}")
        
    
    
# フォルダのパス操作色々    
def file_check():
    # カレントディレクトリのパスを返す
    p_cd = pathlib.Path.cwd()
    print(p_cd)
    
    # homeディレクトリのパスを返す
    p_home = pathlib.Path.home()
    print(p_home)
    
