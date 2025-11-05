## argparseのデモ

--helpオプションでメッセージを確認できる
```bash
python .\argparse-demo.py --help
```

出力は次のようになる。

```text
usage: grep [-h] [-abc ABCDEFG] filenames [filenames ...]

コマンドの説明です。

positional arguments:
  filenames

options:
  -h, --help            show this help message and exit
  -abc ABCDEFG, --abcdefg ABCDEFG
```

