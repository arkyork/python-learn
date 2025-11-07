# リストの基本的な操作

# カレーの種類
curry = [
    "jawa",
    "hotel",
    "ki-ma",
    "chiken",
    "spice"
]

print("元のリスト：",curry)

# curry.append("spice")と同じ
#　末尾に追加
curry[len(curry):] = ["spice"]
print("追加後：",curry)

# spiceの個数をcount

print(curry.count("spice"))

# pop => 要素の削除+取り出し

print(curry.pop())

print("削除後：",curry)
# del popとは違い 返り値がない

del curry[0]

print("削除後：",curry)
