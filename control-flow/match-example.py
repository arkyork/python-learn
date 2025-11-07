class Ramen:
    # match caseでキーワードを指定する必要がない
    __match_args__  = ('name',)
    def __init__(self,name):
        self.name = name


# matchでラーメンを判断
def ramen_judge(ramen):
    match ramen:
        case Ramen("shouyu"):
            print("醤油ラーメン")
        case Ramen("sio"):
            print("塩ラーメン")
        case _:
            # _は該当なし
            print("不明")


ramen_judge(Ramen("shouyu"))
ramen_judge(Ramen("sio"))
ramen_judge(Ramen("nasi"))