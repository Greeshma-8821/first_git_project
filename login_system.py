users={
    "username":"Mythri",
    "password":"my3"
}
username=input("Enter your username:")
password=input("Enter your password:")
correct_username=users.get("username")
correct_password=users.get("password")
if(username==correct_username)and(password==correct_password):
    print("login sucessful")
else:
    print("invalid information")

