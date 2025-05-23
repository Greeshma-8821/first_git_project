users={("john","1234"):"admin",("alice","abcd"):"editor"}
username=input("enter username:")
username1=input("enter username")
password=input("enter password:")
user={(username,username1),password}
print(user)
if user==users.items():
    print(f"Welcome {username}")
else:
    print("invalid login")