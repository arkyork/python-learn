# 型に関するメタデータ
# (int, int)ではなくtupleという書き方がある
def swap(a: int,b: int) -> tuple[int,int]:
    return b,a

print(swap(1,2))
