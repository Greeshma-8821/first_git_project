categories={
    "clothes":["shirt","jeans"],
    "electronics":["phone","charger"]
}
user=input("enter category:")
if user=="clothes":
    clothe=categories["clothes"]
    print(clothe)
elif user=="electronics":
    electronic=categories["electronics"]
    print(electronic)
else:
    print("invalid category")