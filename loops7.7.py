names=[]
count=0
for x in range(5):
    name=input(f"Enter name {x+1}:")
    names.append(name)
search_name=input("Enter the name to the search:")
for n in names:
    if search_name in names:
        print("found")
        break
    else:
        print("not found")
        break