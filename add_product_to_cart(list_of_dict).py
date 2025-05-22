cart=[{"id":1,"name":"shirt","qty":1},]
cart1={}
product_id=int(input("enter product id:"))
product_name=input("enter product name:")
cart1[product_id]=product_name
if product_id is 1:
    print("id is already exist")
else:
    users={**cart[0],**cart1}
    print(users)  