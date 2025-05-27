tags={"python","fastapi","backend"}
tag=input("enter your new tag:")
if tag in tags:
    print("Tag is already exist")
else:
    print(tags.add(tag))
print(tags)