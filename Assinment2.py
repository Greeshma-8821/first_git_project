

menu={
    "idly":40,
    "dosa":45,
    "vada":50,
    "milk":15,
    "water":10
}
ask=input("Enter what you want:")
if ask.lower()=="idly":
    print("Do you want any other dish to eat:")
elif ask.lower()=="dosa":
    print("Do you want any other dish to eat:")
elif ask.lower()=="vada":
    print("Do you want any other dish to eat:")
elif ask.lower()=="milk":
    print("Do you want any other dish to eat:")
elif ask.lower()=="water":
    print("Do you want any other dish to eat:")
else:
    ask=menu.keys()
    count=ask.get("ask")
    ask2=input("what you want else:")
    count2=ask2.get("ask2")
    a=menu.values()
    print(f"your total bill is:{a}")



