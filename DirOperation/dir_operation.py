"""
Created on Thu Jan 5 2023
@author: ShogoHayashi
"""


import pathlib
import shutil



# カレントディレクトリ上にディレクトリを作成
def make_directory_in_current(folder_path):
    # Pathオブジェクトを作成
    p_folder = pathlib.Path(folder_path)
    
    # 既に存在している名前かどうかを確認
    if p_folder.exists():
        print(f"{folder_path} is already exists.")
        # If exists, return to main function
        return
    else:
        print(f"{folder_path} is not exists.")
        
    # ディレクトリを作成
    p_folder.mkdir()
    
    # ディレクトリの作成に成功したかどうか
    if p_folder.exists():
        print(f"Successfully created {folder_path}.")
    else:
        print(f"Failed to create {folder_path}.")


# 中間ディレクトリを含めてディレクトリを作成
def intermediate_directory(folder_path):
    # Pathオブジェクトを作成
    p_folder = pathlib.Path(folder_path)
    
    # 既に存在している名前かどうかを確認
    if p_folder.exists():
        print(f"{folder_path} is already exists.")
        # If exists, return to main function
        return
    else:
        print(f"{folder_path} is not exists.")
        
    # 中間ディレクトリを含めてディレクトリを作成
    # parents = Trueとすると中間ディレクトリを含めて作作成できる
    p_folder.mkdir(parents=True)
    
    # ディレクトリの作成に成功したかどうか
    if p_folder.exists():
        print(f"Successfully created {folder_path}.")
    else:
        print(f"Failed to create {folder_path}.")

    
# 空のディレクトリを削除するための関数
def delete_empty_directory(folder_path):
    # Pathオブジェクトを作成
    p_folder = pathlib.Path(folder_path)
    
    # ディレクトリが存在するものであるかを確認
    if not p_folder.exists():
        print(f"{folder_path} is not exists.")
        # If exists, return to main function
        return
    else:
        print(f"{folder_path} is exists.")
        
    # 空のディレクトリを削除
    # pathlibのrmdir()はその中身が空の時だけ使用できる
    p_folder.rmdir()
    
    # 空のディレクトリの削除が成功したかどうか
    if not p_folder.exists():
        print(f"Successfully deleted {folder_path}.")
    else:
        print(f"Failed to delete {folder_path}.")
        
        
# 中身からではないディレクトリの削除
def delete_not_empty_directory(folder_path):
    # Pathオブジェクトを作成
    p_folder = pathlib.Path(folder_path)
    
    # ディレクトリが存在するものである確認
    if not p_folder.exists():
        print(f"{folder_path} is not exists.")
        # If exists, return to main function
        return
    else:
        print(f"{folder_path} is exists.")
    
    # 中身が空でないディレクトリの削除
    # shutilモジュールのretree関数を使用
    # 引数にはディレクトリのパスもしくはPathオブジェクト
    shutil.rmtree(p_folder)
    
    # ディレクトリの削除が成功したかどうか
    if not p_folder.exists():
        print(f"Successfully deleted {folder_path}.")
    else:
        print(f"Failed to delete {folder_path}.")

folder_path = "new_folder"

delete_not_empty_directory(folder_path)