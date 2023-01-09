# ファイル・ディレクトリ操作
ファイルやディレクトリの操作に関するコード。
## ディレクトリ操作
```
python dir_operation.py
```
### 参考文献
- [pathlib : オブジェクト指向のファイルシステムパス](https://docs.python.org/ja/3/library/pathlib.html)
- [shutil : 高水準のファイル操作](https://docs.python.org/ja/3/library/shutil.html)

主にpathlibを使用している。操作内容は以下の通り。
- カレントディレクトリ上に任意のディレクトリを作成
- 中間ディレクトリを含めてディレクトリを作成
- 中身が空のディレクトリを削除
- 中身が空でないディレクトリの削除

実行時注意点として、
- 各関数の引数には、作成したいディレクトリ名もしくはパスを与える

## ファイル操作
```
python file_operation.py
```
### 参考文献
- [pathlib : オブジェクト指向のファイルシステムパス](https://docs.python.org/ja/3/library/pathlib.html)
- [pprint : データ出力の整然化](https://docs.python.org/ja/3/library/pprint.html)

主にpathlibを使用している。操作内容は以下の通り。
- ディレクトリ内のファイルと子ディレクトリの一覧を取得する
- ディレクトリ内のファイルと子ディレクトリの一覧を再帰的に取得する
- ファイルの情報を確認
- フォルダのパス操作色々

実行時注意点として
- ディレクトリ内の一覧を取得する際はそのディレクトリ名もしくはパスを引数として与える