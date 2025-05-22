locations=[(12.9716,77.5946)]
location=[]
latitude=float(input("Enter latitude:"))
longitude=float(input("Enter longitude:"))
location=[(latitude,longitude)]
if location==locations:
    print("location already exist")
else:
    print(location)