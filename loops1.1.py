numbers=[]
for x in range(5):
    number=int(input(f"Enter number {x+1}:"))
    numbers.append(number)
search_num=int(input("Enter the number to the search:"))
for num in numbers:
    if num==search_num:
        print("found")
        break
    else:
        print("not found")
        break