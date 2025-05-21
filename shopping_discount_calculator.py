amount=int(input("Enter you total purchase amount:"))
if amount>100:
    print("you have 10% discount")
    amount1=10
elif amount>50:
    print("you have 5% discount")
    amount1=5
else:
    print("No discount")
    amount1=0
final_amount=amount-amount1
print(final_amount)
    
