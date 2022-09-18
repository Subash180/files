print("\n********************WELCOME TO BOOKMYSHOW **********************")

acc = input("DO YOU HAVE BOOKMYSHOW ACCOUNT:")
em=["suba@gmail.com"]
if acc=='yes':
    email = input("\nENTER YOUR EMAIL ID:-")
    em.append(email)
    ph= input("\nENTER YOUR PHONE NO:")
    name=input("\nenter your name:")
    pas = input("\nENTER YOUR PASSWORD:-")
    otp = int(input("\nENTER A OTP CODE ON YOUR EMAIL AND PHONE NO:-"))
   
    print("\n-------LOGIN SUCCESSFUL-------")

elif acc=="no":
    print("SIGNUP THE DETAILS")
    name = input("\nENTER YOUR FULL NAME:-")
    ph = int(input("\nENTER YOUR PHONE NO:-"))
    city = input("\nENTER YOUR CITY NAME:-")
    state = input("\nENTER YOUR STATE:-")
    email = input("\nENTER YOUR EMAIL ID:-")
    em.append(email)
    passw = input("\nENTER YOUR PASSWORD:-")
    print(f"\nOTP SEND TO {ph} AND {em}")
    ot = int(input("\nENTER THE OTP NO:-"))
    
    print("\n-------YOUR ACCOUNT IS CREATED SUCCESSFULLY-------")  


print("\n********* SHOWING LATEST MOVIES*********----")

print("which movie do you want to watch ?:")
print(" vikram")
print(" sitaramam")
print(" sinam")

movies=["vikram", "sitaramam", "sinam"]

vikram_amount=120
sitaramam_amount=150
sinam_amount=100

click_movie=input("enter your movie name:")
if click_movie in movies:
    print(f"the {click_movie} movie showtime is available")

    print("*******select the theater **********")

    print("inox maal")
    print("mayajal")
    print("marina maal")


theater=["inox maal","marina maal","mayajal"]  

click_theater=input("enter the theater name:")  

print("************seats select***********") 

seats=int(input("enter how many seats you want:"))

if click_movie=="vikram":
    total=vikram_amount*seats
    print(f"your payment is {total}")

elif click_movie=="sitaramam":    
    total=sitaramam_amount*seats
    print(f"your payment is {total}")

elif click_movie=="sinam":
    total=sinam_amount*seats
    print(f"your payment is {total}")

else:
    print("enter valid details")

print("**********if you want snacks in showtimes********")  



snacks=["cooldrinks","samosa","chicken puffs","popcorn"]
cooldrinks=100
samosa=20
chicken=40
popcorn=60
if snacks:
    print("\n the snacks menus are:")
    print("1. cooldrinks -------->rs.100")
    print("2. samosa ---------->rs.20")
    print("3. chicken puffs ------->rs.40")
    print("4. popcorn -------->rs.60")

    x=int(input("you have choose option:"))
    n=int(input("how many you want:"))
    snacks_amount=snacks*n
   
    if (x==1):
        print("you have chosen cooldrinks")
        snacks_amount=cooldrinks*n
        print(f"you have to pay {snacks_amount}")
    elif (x==3):
        print("you have chosen samosa")
        snacks_amount=samosa*n
        print(f"you have to pay {snacks_amount}")    
    elif (x==3):
        print("you have chosen chicken puffs")
        snacks_amount=chicken*n
        print(f"you have to pay {snacks_amount}")  
    elif (x==4):
        print("you have chosen popcorn")
        snacks_amount=popcorn*n
        print(f"you have to pay {snacks_amount}")  
    else:
        print("you have choose right option")    
    total_payment=total+snacks_amount


print("<----___**************you ticket is here********************___---->")


print(f"your name is <---{name}  ----- and ------your phone number-<----{ph}--->")

print(f"your email id is {email}")

print(F"your movie name is<--- {click_movie} --->")

print(f"your theater is <---{click_theater}--->")

print(f"your ticket payment is <---{total}--->")

print(f"your snacks amount <---{snacks_amount}--->")

print(f"your total payment is <---{total_payment}--->")


print("************------enjoy your movies--------***********")

print("*********************thank you*******************")














   
  
