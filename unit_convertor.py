#user enters a action based on that action we choose what should we do.
#actions = ["meter" , "kilometer" ," centimeter" ," milimeter"]
def action_pro(action):
    if (action == "meter" or action == "m"):
        print(f"Its gonna be {user} meter ")  
    elif (action == "kilometer") or action == "km" :
        print(f"Its gonna be {float(user/1000)} kilometer") 
    elif (action == "centimeter" or action == "cm"):
        print(f"Its gonna be {float(user * 100)} centimeter")
    elif (action == "milimeter" or action == "mm"):
        print(f"Its gonna be {float(user * 1000)} milimeter") 
    elif last in ['yes' , 'Yes']:
        pass    
    else:
        print("Check your spelling plz!")
    return
user = int(input("Enter the value in meter: "))
action = input("What is the convertion is gonna be, plz choose from these [meter(m) , kilometer(km) , centimeter(cm) , milimeter(mm)] ")

while True:    
    action_pro(action) 

    last = input("Would u like to continew [ yes or no ]:  ")
    if last == 'yes':
        action_pro(action)
    elif last == 'no':
        break       
    user = int(input("Enter the value in meter: "))
    action = input("What is the convertion is gonna be, plz choose from these [meter(m) , kilometer(km) , centimeter(cm) , milimeter(mm)] ")
   