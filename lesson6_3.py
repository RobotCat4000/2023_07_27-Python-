import random
min = 1
max = 100
target = random.randint(1,10)
count = 0

print("========猜數字遊戲========\n\n")
while True:
    keyin = int(input(f"猜數字的範圍{min}~{max}:"))
    count += 1
    if keyin >= min and keyin <= max:
        if(keyin == target):
            print(f"Da way,答案是:{keyin}")
            print(f"一共猜了{count}次")
            break
        elif(keyin > target):
            print("小一點")
            max = keyin-1
        elif(keyin < target):
            print("大一點")
            min = keyin +1
        
        print(f"已經猜了{count}次")
    else:
        print("超出範圍")
print("Da way! Da way! Da way!")