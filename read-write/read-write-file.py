# openはファイルオブジェクトを返す

f = open("./read-write/file","r",encoding="UTF-8")

# file名,mode,
# mode = "a"はappending
# r+はread and write
# bはbinary mode

# f.closedはファイルが閉じているかどうか

print(f.closed)

f.close()

print(f.closed)