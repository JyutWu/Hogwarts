import random

computer_num=random.randint(1,100)
# print(computer_num)

while True:
    person_num = int(input("请输入一个数字:"))
    if  person_num == computer_num:
        print ("猜对了")
        break
    elif person_num < computer_num:
        print ("大一点")
    else :
        print  ("小一点")



