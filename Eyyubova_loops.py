# part A
question 1
for i in range(10,0,-1):
    print(i)
print("Liftoff!")

# question 2
childticket=0
adultticket=0
for i in range(1,6):
    age=int(input())
    if age<18:
        childticket+=1
    else:
        adultticket+=1
    print("Age of visitor",i,":",age)
print("Child tickets :",childticket)
print("Adult tickets :",adultticket)

# question 3
# cavab:1 3 5 7 9

# question 4
total=0
for i in range(1,6):
    price=float(input())
    print("Price of item",i,":",price)
    total+=price
average=total/5
print("Total :",total)
print("Average :",average)

# question 5
l=0
while l!=1:
    npassword=input()
    if len(npassword)<8:
        print("Too short,try again")

    else:
        l=1
print("Password accepted")

# question 6
# cavab: balance
# balance
# balance
# balance
# Done

# question 7
steps=1200
for i in range(1,8):
    print("Day",i,":",steps)
    steps+=1200

# question 8
l=0
for i in range(1,4):
    username = input()
    password = input()
    if username!="admin" or password!="1234":
        print("wrong username or password")
    else:
        print("Welcome!")
        l=1
        break
if l==0:
    print("Account locked")

#Part B-medium
# question 9
balance=500
while balance>=0:
    wa=int(input("withdrawal amount:"))
    if wa>balance:
        print("Insufficient funds")
    elif wa==0:
        print("Goodbye")
        break
    elif wa<0:
        print("Invalid amount")
    else:
        balance-=wa
        print("Balance:",balance)

# question 10
# cavab:Wrong pin,2 attempts left
# wrong pin,1 attempt left
# access granted
# attempts used:3

# question 11
l=0
c=0
d=0
sum=0
highest=0
while l==0:
    grade=int(input("Grade :"))
    print("Grade:",grade)
    if grade>highest:
        highest=grade
    if grade>=51:
        c=c+1
    elif grade==-1:
        break
    else:
        d=d+1
    sum=sum+grade
print("Passed :",c)
print("Failed :",d)
print("Highest :",highest)
print("Average :",sum/(c+d))

# question 12
pspace=0
while True:
    command = input("command:")
    if command=="in":
        print("Command: in")
        if pspace==20:
            print("Garage full")
        else:
            pspace+=1
            print("Free spaces:",20-pspace)
    elif command=="out":
        print("Command: out")
        if pspace==0:
            print("Garage is empty")
        else:
            pspace-=1
            print("Free spaces:",20-pspace)
    elif command=="stop":
        break
    else:
        print("Unknown command")

# question 13
hot=0
hottest=0
c=0
for i in range(1,8):
    degree=int(input())
    print("Day",i,":",degree)
    if degree>30:
        hot+=1
    if degree>hottest:
        hottest=degree
        c=i
print("Hot days:",hot)
print("Hottest day:",c)
    
# question 14
password = "secret"
attempts = 0
while True:
 entered = input("Password: ")
 if entered == password:
 print("Welcome")
 break
 attempts += 1
 if attempts == 3:
 print("Account locked")
 break
# cavab:attempts=0 while den evvel olmalidir,yoxsa her dovr basladigca attempts=0 olacaq ve dovr sonsuz davam edecek

# question 15
password=input()
digits=0
ucase=0
lcase=0
for character in password:
    if character.isdigit():
        digits+=1
    elif character.isupper():
        ucase+=1
    elif character.islower():
        lcase+=1
if len(password)<8:
    print("Weak password:not enough characters")
elif digits==0:
    print("Weak password:no digits")
elif ucase==0:
    print("Weak password:no upper case letters")
elif lcase==0:
    print("Weak password:no lowercase letters")
else:
    print("Strong password")

# question 16
saved=0
more=50
month=1
while saved<1000:
    saved+=more
    more+=10
    print("Month",month,":",saved)
    month+=1
print("Goal reached in month",month-1)

# question 17
# 100den boyuk 7ye bolunen ilk tek ededi cap eden proqramdir,bize ondan sonraki ededler lazim olmadigi ucun break dovru dayandirir

# Part C- Hard :o
# question 18
attempt=0
balance=1000
while attempt<3:
    pin=input()
    if pin=="2580":
        print("Successsful login")
        break
    else:
        attempt+=1
        if attempt==3:
            print("Card blocked")
if attempt<3:
    while True:
        print("1 - Check balance")
        print("2 - Deposit")
        print("3 - Withdraw")
        print("4 - Exit") 
        choice=input("Choose an option:")
        if choice=="1":
            print("Balance",balance)
        elif choice=="2":
            amount=float(input("Deposit amount:"))
            if amount<=0:
                print("Invalid amount")
            else:
                balance+=amount
                print("Balance:",balance)
        elif choice=="3":
            wamount=float(input("Withdraw amount:"))       
            if wamount<=0 or wamount>balance:
                print("Invalid amount")
        elif choice=="4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

# question 19
total=0
a=[0.05,0.10,0.20,0.50,1]
while total<1.50:
    insert=float(input())
    if insert not in a:
        print("Coin not accepted")
    else:
        total+=insert
        print("Total :",total)
print("Here is your water")
if total>1.50:
    print("change :",total-1.50)

# question 20
total=0
for i in range(2,100):
    c=0

    for j in range(2,i//2+1):
        if i%j==0:
            c=c+1
            break
    if c==0:
        print(i,end=" ")
        total+=1
print("Total codes:",total)

#question 21
101 102 104 
201 202 204
301 302 304

#question 22
for floor in range(1,6):
    print("Floor ",floor,end=" ")
    for room in range(1,5):
        if room==4:
            break
        else:
            print(floor*100+room,end=" ")
    print()

#question 23
mins=480
customer=0
while True:
    time=int(input())
    if time<mins:
        customer+=1
        print("Customer",customer,"needs (min):",time)
    else:
        print("Sorry,come back tomorrow")
    mins-=time
    if mins==0:
        break
print("Customer served:",customer)
print("Minutes left :",mins)

#question 24
spoiled=0
a=0
b=0
c=0
while True:
    vote=input("Vote:")
    if vote=="A":
        a+=1
    elif vote=="B":
        b+=1
    elif vote=="C":
        c+=1
    elif vote=="end":
        break
    else:
        spoiled+=1
print("A:",a,"B:",b,"C:",c)
print("Spoiled:",spoiled)
if a>b and a>c:
    print("Winner: A")
elif b>c and b>a:
    print("Winner: B")
elif c>a and c>b:
    print("Winner: C")
else:
    print("Tie")

#question 25
while True:
    number=input()
    if len(number)!=16 or number.isdigit()==False:
        print("Invalid card number")
        continue
    sum=0
    for i in range(15,-1,-1):
        if (15-i)%2!=0:
            num=int(number[i])*2
            if num>9:
                num=num-9
        else:
            num=int(number[i])
        sum=sum+num
    if sum%10==0:
        print("valid")
    else:
        print("invalid")



