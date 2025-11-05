import argparse

parser = argparse.ArgumentParser(
    prog='grep', # コマンドの見え方が変わる
    description='コマンドの説明です。' # コマンドの説明
    )

# add_argumentで引数の設定を追加

# 引数filenamesは一つ以上を受け取る
parser.add_argument('filenames', nargs='+')

# -abcオプションは整数値を受け取る
# 引数の型はstr型で defaultはabc
parser.add_argument("-abc","--abcdefg",type=str,default="abc")

args = parser.parse_args()
print(args)