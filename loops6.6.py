fruits={
    "grapes":30,
    "pineapple":50,
    "pear":40
}
a=fruits["strawberry"]=60
b=fruits.update({"pear":20})
del fruits["grapes"]
for item in fruits.items():
    print(item)