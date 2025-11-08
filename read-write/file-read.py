# f.read(size: int) -> binary objectまたは stringを返す
# size が 0以下なら全体を返す

with open("./read-write/file","r+") as f:
    # data = f.read()
    data_size = f.read(3)

# print(data)
# 3文字だけ
print(data_size)

# f.readlineは1行だけ取り出す
print("="*45)

with open("./read-write/file","r") as f:
    print(f.readline(),end="")

# forで取り出す場合

print("="*45)

with open("./read-write/file","r") as f:
    for line in f:
        # lineのままだと\nが含まれているので end = ""を指定する必要がある
        print(line,end="")
    print()

# list(f)やf.readlines
print("="*45)


with open("./read-write/file","r") as f:
    for line in f.readlines():
        
        # lineのままだと\nが含まれているので end = ""を指定する必要がある
        print(line,end="")
    print()

# f.tell() 現在の場所
print("="*45)

with open("./read-write/file","r+") as f:
    # data = f.read()
    print(f.tell())
    data_size = f.read(3)
    print(f.tell())

# f.seek(offset,whence) 基準値に対して offsetを足すことで位置を変える
# whence 0:先頭 1:ファイル位置 2：末尾

print("="*45)
with open("./read-write/file","r+") as f:
    # data = f.read()
    f.seek(2)
    print(f.tell())
    data_size = f.readline()
    print(data_size,end="")
    # 次の行に移動

    data_size = f.readline()
    print(data_size,end="")
    # 先頭に移動
    f.seek(0,0)
    data_size = f.readline()
    print(data_size,end="")

    print(f.tell())