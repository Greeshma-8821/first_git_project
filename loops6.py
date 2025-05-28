fruits={"apple":2,"banana":3,"apricot":4,"berry":5}
count=1
for keys,items in fruits.items():
    if keys.startswith("a"):
        count*=items
print(f"product of values:{count}")