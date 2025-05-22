bill=0
menu={
    "idly":10,
    "dosa":40,
    "poori":25,
    "bonda":10
}
item1=input("Enter item:")
item1_count=int(input("enter count:"))
item2=input("Enter item:")
item2_count=int(input("enter count:"))
item3=input("Enter item:")
item3_count=int(input("enter count:"))
bill=menu[item1]*item1_count+menu[item2]*item2_count+menu[item3]*item3_count
print(f""" ------------------villa hotel---------------------------------------
      {item1}X{item1_count}+{item2}X{item2_count}+{item3}X{item3_count}={bill}
---------------------------------------------------------------------------------
""")