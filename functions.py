data=[{
    "name":"prashanth",
    "age":45
},
{
    "name":"Kareem",
    "age":55
}]
def extract_ages(data):
    age_1=data[0]["age"]
    age_2=data[1]["age"]
    return [age_1,age_2]
ages=extract_ages(data)
print(ages)
def extract_names(data):
    name_1=data[0]["name"]
    name_2=data[1]["name"]
    return [name_1,name_2]
names=extract_names(data)
print(names)