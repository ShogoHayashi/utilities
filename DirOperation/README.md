# ファイル・ディレクトリ操作
ファイルやディレクトリの操作に関するコード。
## ディレクトリ操作
```
python dir_operation.py
```
以下が参考文献
- [pathlib : オブジェクト指向のファイルシステムパス](https://docs.python.org/ja/3/library/pathlib.html)
- [shutil : 高水準のファイル操作](https://docs.python.org/ja/3/library/shutil.html)

主にpathlibを使用している。操作内容は以下の通り。
- カレントディレクトリ上に任意のディレクトリを作成
- 中間ディレクトリを含めてディレクトリを作成
- 中身が空のディレクトリを削除
- 中身が空でないディレクトリの削除
