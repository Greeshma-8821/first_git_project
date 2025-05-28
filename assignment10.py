person={
    "name":"joy",
    "age":45,
    "hobbies":["dancing","swimming","reading"]
}
for key in person:
    if key=='hobbies':
        myhobbies=person["hobbies"]
        for j in myhobbies:
            print(j)