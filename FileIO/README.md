# データファイルの読み込み・書き出し
データファイルの読み込みと書き出しに関するコード。
## MHDファイル
```
python mhd_io.py
```
- 参考文献
    - [itk::simple::ImageFileReader Class Reference](https://simpleitk.org/doxygen/latest/html/classitk_1_1simple_1_1ImageFileReader.html#ab8d91d4ca4ee13f704d72205d344837e)
    - [scikit-image](https://scikit-image.org/docs/stable/api/skimage.io.html)

- 操作内容
    - mhdファイルからraw imageを取得して保存(simpleITK/skimage.io)
    - simpleITKを用いた方法には、その保存方法も。
    - 解像度を求める方法(simpleITK)

- 実行時注意点
    - 各関数の引数には、読み込みたいMHDファイル名を入力する

## csvファイル
```
python csv_io.py
```
- 参考文献
    - [csv : CSV ファイルの読み書き](https://docs.python.org/ja/3/library/csv.html)
    - [pathlib : オブジェクト指向のファイルシステムパス](https://docs.python.org/ja/3/library/pathlib.html)
- 操作内容
    - ディレクトリ内のファイルと子ディレクトリの一覧を取得する
    - ディレクトリ内のファイルと子ディレクトリの一覧を再帰的に取得する
    - ファイルの情報を確認
    - フォルダのパス操作色々

- 実行時注意点
    - ディレクトリ内の一覧を取得する際はそのディレクトリ名もしくはパスを引数として与える