def  main():
    firstname=input ("Enter Firstname:")
    lastname=input("Enter Lastname:")
    age=int(input("Enter the age:"))
    if age <0:
        print(f"your full name is{firstname} {lastname} and please enter valid age")

    elif age <18:
        print(f"your full name is {firstname} {lastname} and you are a miner")
    elif age>18 and age<=67:
        print(f"your full name is {firstname} {lastname} and you are a adlt")  
    else:
        print(f"your full name is{firstname} {lastname} and you are a seinor cition ") 
        print("hi") 
    
if __name__=="__main__":
    main()