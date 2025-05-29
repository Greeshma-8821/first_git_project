user_input=int(input("Enter number:"))
def divisibleby3(num): 
  for i in range(1,num+1):
        if i%3==0:
            print(i)
  else:
    print("you entered number is:",user_input)
divisibleby3(user_input)