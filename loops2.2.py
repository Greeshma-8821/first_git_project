total=0
count=0
while total<100:
    num=int(input("enter a number:"))
    total+=num
    count+=1
else:
    print("please enter a valid number")
print("total reached or exceeded 100")
print(f"numbers entered {count}")
    