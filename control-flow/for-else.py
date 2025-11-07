for i in range(3):
    print(i)
else:
    print("not break")
    print("="*50)



# breakされると elseが実行されない
for i in range(3):
    print(i)
    break
else:
    print("not break")