a = input("")
for i in 0,1,2,3,4,5,6,7,8,9:
    if str(i) in a or a!=a.title():
        print("Ошибка")
        break
    else:
        print("Нет ошибки")
        break
