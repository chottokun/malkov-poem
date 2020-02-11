# これは？
マルコフ連鎖でポエムを生成して遊ぶもの

#必要なもの
mecab

    sudo apt-get install mecab libmecab-dev mecab-ipadic-utf8 python-mecab
    sudo apt-get install aptitude swig

#インストール

    pipenv install

ただし、python 3.7なので、3.6で動かしたい場合はPipFileの記述を変更

# 使い方

poem.txt に適当な文章を入れておく
python learn_poems.py
で、分かち書きと言葉の学習を行う。

python make_poems.py
で、新しい文章の生成

# まだまだ、未完成です

生成する文章の長さ
生成する文書の数
は決め打ち。

# メモ
分かち書きの精度を上げたい場合は、辞書をipadic-NEologdにしましょう。
