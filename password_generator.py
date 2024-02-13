import random
print("\t\t\t\t\t\t\t\tPASSWORD GENERATOR\t\t\t")
def fun():
    j=int(input("Enter the desired length to generate password :"))
    b= [str(i) for i in range(10)]
    a= [chr(i) for i in range(65, 91)]
    f= [chr(i) for i in range (97,123)]
    g=['#','&','@','*','(',')','!','$','%']
    c=a+b+f+g
    d=""
    d=d+random.choice(a)
    for i in range(j-1):
        k=random.choice(c)
        d=d+k
    print(f"The generated password of length {j} is : {d}")
 
 
 
fun()
while(1):
    l=input("\nAre you satisfied with the password (Y/N) :")
    print()
    if(l=='Y' or l=='y'):
        print("Thank You !! have a nice day :)")
        break
    elif(l=='N' or l=='n'):
        fun()
    else:
        print("Enter valid option !!!")
