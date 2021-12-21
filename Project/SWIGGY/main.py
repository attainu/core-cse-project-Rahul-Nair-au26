"""
"""
from random import randint


"""
Welcome all this is a python based industrial project on a food delivery application.
The following is the process to create this application.

Initail process: Term 1

In the intial process I've created a class a class SWIGGY, wherein there are 3 different 
fast food corners and resturant, which each contain a total of 5 different food items, respectively.
"""

class swiggy():

    def __init__(self):
        print()
        print("-"*40 ,"SWIGGY ", "-"*40)
        
        global res, Mcdonalds, Subway, Origami, dic, history 
        
        Mcdonalds = {  
            "Mc chicken burger" : 200, 
            "Mc grill       ": 250, 
            "Mc Chicken wrap" : 240, 
            "Mc coffee/Mc latte" : 150, 
            "coke & fries" : 110
            }

        Subway = {       
            "Sub chicken kofta" : 200, 
            "Sub paneer tikka" : 180, 
            "Sub fresh tuna" : 169, 
            "coke & wedges" : 110, 
            "cookies      " : 50
            }

        Origami = {      
            "chicken tteokbokki" : 400, 
            "kimchi jjigae" : 500, 
            "korean ramyun" : 450, 
            "japchae      " : 450, 
            "soju         " : 800
            }


        res = {
            "Mcdonalds": Mcdonalds, 
            "Subway": Subway, 
            "Origami": Origami
            }

        dic = {}        # To store any item ordered by the user
        history = {}    # To see the history of any item ordered by the user at any takeaway.

        self.main_menu()
    





    """
    Term 2:

    In Second phase, I've created a function wherein the user has an access to the main page of the application
    for example user can check the resturants and fast food joints avaliable to the user at that particular time
    and area, order any food avaliable in the menu and also the user can the check the previously ordered food 
    through the RECENT ORDERs fucntion. 
    """

    def main_menu(self):
        print("")
        print("*"*25 ,"Welcome To SWIGGY Homepage", "*"*25)
        print()
        print("Please select the desired option")
        print()
        print("(O) ORDER FOOD \n"
        "(H) RECENT ORDER \n"
        "(R) RESTURANT'S & FOOD JOINT'S \n"
        "(E) EXIT" )
        
        print()
        print("="*90)
        while True:
            inp1 = input("PLEASE ENTER YOUR DESIRED OPTION HERE: ").upper()
            if inp1 == 'O':
                self.restaurants()
                break
            elif inp1 == 'R':
                self.res_corner()
            elif inp1 == 'E':
                print("="*90)
                print("THANKYOU FOR USING OUR SERVICES, HOPE TO SEE YOU AGAIN")
                print("="*90)
                exit()
            elif inp1 == 'H':
                self.History(history)
                break
            else:
                print("INVALID INPUT PLEASE TRY AGAIN")





    """
    Term 3:
    In this phase, I've created the function Resturants wherein the user has the accessibility to check all the resturants
    present on the application at that moment.
    """

    def restaurants(self):

        print("="*90)
        print()
        print(">"*19,"Avaliable Resutrant's in your Area:","<"*19)
        print()
        count = 1
        for i in res:
            print(str(count)+")", i)
            count += 1
        print()
        print("\n                           (M) MAIN MENU    (E) EXIT")
        print("="*90)
        while True:
            inp = str(input().upper())
            print("="*90)
            if inp == 'M':
                self.main_menu()
                break
            if inp == "E":
                print("="*90)
                print("THANKYOU FOR USING OUR SERVICES, HOPE TO SEE YOU AGAIN")
                print("="*90)
                exit()
            try:
                if int(inp) == 1:
                    count = 1
                    for i in Mcdonalds:
                        j = Mcdonalds[i]
                        print("("+str(count)+")",i.upper(),"\t"*6,"price","\t","Rs","{:.2f}".format(float(j)))
                        count += 1
                    self.Mcdonalds()
                    break   


                if int(inp) == 2:
                    count = 1
                    for i in Subway:
                        j = Subway[i]
                        print("("+str(count)+")",i.upper(),"\t"*5,"price","\t","Rs","{:.2f}".format(float(j)))
                        count += 1
                    self.Subway()
                    break    

                if int(inp) == 3:
                    count = 1
                    for i in Origami:
                        j = Origami[i]
                        print("("+str(count)+")",i.upper(),"\t"*5,"price","\t","Rs","{:.2f}".format(float(j)))
                        count += 1
                    self.Origami()
                    break              
            except:
                print("INVALID INPUT PLEASE TRY AGAIN")





    """
    Term 4:
    In this phase, I've created a function in which the user has the access to visit any of the avaliable resturants and
    food joint's, where the user will be having the access to see thourgh the food menu and will have various call functions
    provided therein, such as main  "menu" "exit" "cart", which allows the user to surf though the swiggy application.
    This fucntion also has an limitation on the food quantity ordered by the user.
    This fucntion will be done for all the 3 resturants mentioned above respectivey. 
    """

    def Mcdonalds(self):
        print()
        print("\n                     (M) MAIN MENU    (E) EXIT    (C)CART")
        print("="*90)
        dic = {}
        counter = 0
        qu = 0
        while True:
            inp = input("SELECT YOUR DESIRED CHOICE: ").upper()
            if inp == 'M':
                self.main_menu()

            if inp == 'E':
                print("="*90)
                print("THANKYOU FOR USING OUR SERVICES, HOPE TO SEE YOU AGAIN")
                print("="*90)
                exit()

            if inp == "C":
                if counter < 4:
                    self.cart(dic,Mcdonalds)
                    break
                else:
                    print("="*90)
                    print("RESTAURANT CANNOT PROCESS MORE THAN 3 ITEMS FOR ONE ORDER")
                    print("PLEASE TRY AGAIN")
                    self.main_menu()
                    break
            try:
                if qu <= 3:
                    if int(inp) == 1:
                        inp1 = int(input("DESIRED QUANTITY: "))
                        if "Mc chicken burger" not in dic:
                            dic["Mc chicken burger"] = inp1
                        else:
                            dic["Mc chicken burger"] += inp1
                        counter += inp1
                    if int(inp) == 2:
                        inp1 = int(input("DESIRED QUANTITY: "))
                        if "Mc grill" not in dic:
                            dic["Mc grill"] = inp1
                        else:
                            dic["Mc grill"] += inp1
                        counter += inp1
                    if int(inp) == 3:
                        inp1 = int(input("DESIRED QUANTITY: "))
                        if "Mc Chicken wrap      " not in dic:
                            dic["Mc Chicken wrap      "] = inp1
                        else:
                            dic["Mc Chicken wrap      "] += inp1
                        counter += inp1
                    if int(inp) == 4:
                        inp1 = int(input("DESIRED QUANTITY: "))
                        if "Mc coffee/ Mc latte" not in dic:
                            dic["Mc coffee/ Mc latte"] = inp1
                        else:
                            dic["Mc coffee/ Mc latte"] += inp1
                        counter += inp1
                    if int(inp) == 5:
                        inp1 = int(input("DESIRED QUANTITY: ")) 
                        if "coke & fries" not in dic:
                            dic["coke & fries"] = inp1
                        else:
                            dic["coke & fries"] += inp1
                        counter += inp1
                else:
                    print("RESTURANT CANNOT PROCESS MORE THAN THREE ITEMS A TIME")   

            except:
                print("INVALID INPUT PLEASE TRY AGAIN--")




    
    def Subway(self):
            print()
            print("\n                     (M) MAIN MENU    (E) EXIT    (C)CART")
            print("="*90)
            dic = {}
            counter = 0
            while True:
                inp = input("SELECT YOUR DESIRED CHOICE: ").upper()
                if inp == 'M':
                    self.main_menu()

                if inp == 'E':
                    print("="*90)
                    print("THANKYOU FOR USING OUR SERVICES, HOPE TO SEE YOU AGAIN")
                    print("="*90)
                    exit()
                if inp == "C":
                    if counter < 4:
                        self.cart(dic,Subway)
                        break
                    else: 
                        print("="*90)
                        print("RESTAURANT CANNOT PROCESS MORE THAN 3 ITEMS FOR ONE ORDER")
                        print("PLEASE TRY AGAIN")
                        self.main_menu()
                        break
                try:
                    if int(inp) == 1:
                        inp1 = int(input("DESIRED QUANTITY: "))
                        if "Sub chicken kofta" not in dic:
                            dic["Sub chicken kofta"] = inp1
                        else:
                            dic["Sub chicken kofta"] += inp1
                        counter += inp1
                    if int(inp) == 2:
                        inp1 = int(input("DESIRED QUANTITY: "))
                        if "Sub paneer tikka" not in dic:
                            dic["Sub paneer tikka"] = inp1
                        else:
                            dic["Sub paneer tikka"] += inp1
                        counter += inp1
                    if int(inp) == 3:
                        inp1 = int(input("DESIRED QUANTITY: "))
                        if "Sub fresh tuna" not in dic:
                            dic["Sub fresh tuna"] = inp1
                        else:
                            dic["Sub fresh tuna"] += inp1
                        counter += inp1
                    if int(inp) == 4:
                        inp1 = int(input("DESIRED QUANTITY: "))
                        if "coke & wedges" not in dic:
                            dic["coke & wedges"] = inp1
                        else:
                            dic["coke & wedges"] += inp1
                        counter += inp1
                    if int(inp) == 5:
                        inp1 = int(input("DESIRED QUANTITY: ")) 
                        if "cookies     " not in dic:
                            dic["cookies     "] = inp1
                        else:
                            dic["cookies     "] += inp1
                        counter += inp1
                    

                except:
                    print("INVALID INPUT PLEASE TRY AGAIN")




    
    def Origami(self):
            print()
            print("\n                     (M) MAIN MENU    (E) EXIT    (C)CART")
            print("="*90)
            dic = {}
            counter = 0
            while True:
                inp = input("SELECT YOUR DESIRED CHOICE: ").upper()
                if inp == 'M':
                    self.main_menu()

                if inp == 'E':
                    print("="*90)
                    print("THANKYOU FOR USING OUR SERVICES, HOPE TO SEE YOU AGAIN")
                    print("="*90)
                    exit()
                if inp == "C":
                    if counter < 4:
                        self.cart(dic, Origami)
                        break
                    else:
                        print("="*90)
                        print("RESTAURANT CANNOT PROCESS MORE THAN 3 ITEMS FOR ONE ORDER")
                        print("PLEASE TRY AGAIN")
                        self.main_menu()
                        break
                    
                try:
                    if int(inp) == 1:
                        inp1 = int(input("DESIRED QUANTITY: "))
                        if "chicken tteokbokki" not in dic:
                            dic["chicken tteokbokki"] = inp1
                        else:
                            dic["chicken tteokbokki"] += inp1
                        counter += inp1
                    if int(inp) == 2:
                        inp1 = int(input("DESIRED QUANTITY: "))
                        if "kimchi jjigae    " not in dic:
                            dic["kimchi jjigae    "] = inp1
                        else:
                            dic["kimchi jjigae    "] += inp1
                        counter += inp1
                    if int(inp) == 3:
                        inp1 = int(input("DESIRED QUANTITY: "))
                        if "korean ramyun" not in dic:
                            dic["korean ramyun"] = inp1
                        else:
                            dic["korean ramyun"] += inp1
                        counter += inp1
                    if int(inp) == 4:
                        inp1 = int(input("DESIRED QUANTITY: "))
                        if "japchae" not in dic:
                            dic["japchae"] = inp1
                        else:
                            dic["japchae"] += inp1
                        counter += inp1
                    if int(inp) == 5:
                        inp1 = int(input("DESIRED QUANTITY: ")) 
                        if "soju" not in dic:
                            dic["soju"] = inp1
                        else:
                            dic["soju"] += inp1
                        counter += inp1

                except:
                    print("INVALID INPUT PLEASE TRY AGAIN")
            




    """
    Term 5:
    In this phase, I've created a function in which the user get a happy hour discount, the fucntion "cart" is where all the 
    food selected by the user is stored, if the user's order is above 500 the user will get a whooping discount of 15% on the 
    over all menu and if the order value is less than 500 but more than 300 the user will get a discount of lovely 10% on his/her
    overall order.
    """

    def cart(self,dic,name):

        print(">"*40, "CART", "<"*40)
        print()
        print('\t'+"-"*68)
        print('\t'*2, "   ITEM","                            ", "QUANTITY")
        print('\t'+"-"*68)
        s = 0
        order_no = randint(0,10000)
        if name == Mcdonalds:
            d = "Mcdonalds"
        elif name == Subway:
            d = "Subway"
        elif name == Origami:
            d = "Origami"
        for i in dic:
            s += name[i]*dic[i]
            if name == Subway:
                print('\t'*2, i.upper(),'\t'*4, dic[i])
            else:
                print('\t'*2, i.upper(),'\t'*3, dic[i])
        print('\t'+"-"*68)
        print('\t'*2,"  ","TOTAL", "\t"*4,s)
        if s > 500:
            s -= s * 0.15
            print('\t'*2,"  ","DISCOUNT", "\t"*4,"15%")
            print('\t'+"-"*68)
            print('\t'*2,"  ","TO PAY", "\t"*4,s)
            
        elif s > 300:
            s -= s * 0.10
            print('\t'*2,"  ","DISCOUNT", "\t"*4,"10%")
            print('\t'+"-"*68)
            print('\t'*2,"  ","TO PAY", "\t"*4,s)
        print("\n                      P(PAY)    (M) MAIN MENU    (E) EXIT")
        print("="*90)
        while True:
            inp = input("SELECT YOUR OPERATION: ").upper()
            if inp == 'M':
                self.main_menu()
                break
            elif inp == 'P':
                history[order_no] = [d , s]
                self.payment(s)
                break
            elif inp == 'E':
                exit()
            else:
                print("INVALID INPUT PLEASE TRY AGAIN")

    """
    Term 6:
    In this phase, I've created the function for payment in which the user has various modes of payment, such as credit card,
    net banking, cash od delivery, etc. Some restritions for the user on the mode of payments are also added in this step.
    """ 




    def payment(self, s):
        print()
        print(">"* 40, "PAYMENT", "<"*40)
        print()
        print("AMOUNT TO BE PAID FOR YOUR SWIGGY ORDER IS ₹", s, "/-")
        print()
        print("AVAILABLE PAYMENT OPTIONS \n"
        "(CC) CREDIT CARD \n"
        "(DC) DEBIT CARD \n"
        "(NB) NET BANKING \n"
        "(U) UPI \n"
        "(W) WALLETS \n"
        "(COD) CASH ON DELIVERY")

        print("="*90)
        while True:
            inp = input().upper()
            if inp == "CC" or inp == "DC" or inp == "NB" or inp == "U" or inp == "W":
                print("="*90)
                print()
                print("PAYMENT SUCCESSFULL")
                print("HURRAY, ORDER CONFIRMED")
                print()
                print("\n                 (H) RECENT ORDER    (M) MAIN MENU    (E) EXIT")
                print("="*90)
                while True:
                    inp1 = input("SELECT YOUR OPERATION: ").upper()
                    if inp1 == "M":
                        self.main_menu()
                        break
                    elif inp1 == 'E':
                        exit()
                    elif inp1 == 'H':
                        self.History(history)
                        break
                    else:
                        print("INVALID INPUT PLEASE TRY AGAIN")
                print("="*90)
                self.main_menu()
            elif inp == 'COD':
                if s > 499:
                    print("CASH ON DELIVERY IS NOT AVAILABLE FOR ORDERS ABOVE 499")
                    print("TRY AGAIN WITH DIFFERENT OPTIONS")
                else:
                    print("="*90)
                    print()
                    print("PLEASE PAY THE AMOUNT TO THE DELIVERY PARTNER")
                    print("CONGRATS!!, ORDER CONFIRMED")
                    print()
                    print("\n                 (H) RECENT ORDER    (M) MAIN MENU    (E) EXIT")
                    print("="*90)
                    while True:
                        inp1 = input("SELECT YOUR OPERATION").upper()
                        if inp1 == "M":
                            self.main_menu()
                            break
                        elif inp1 == 'E':
                            exit()
                        elif inp1 == 'H':
                            self.History(history)
                        else:
                            print("INVALID INPUT PLEASE TRY AGAIN")
            else:
                print("INVALID INPUT PLEASE TRY AGAIN")
        





    def History(self,history):
        print()
        print(">"*33, " RECENT ORDER","<"*33)
        if len(history) == 0:
            print("NO ORDERS YET")
            print()
            print("(M) MAIN MENU \n"
            "(E) EXIT")
            print("="*90)
        else:
            for i in history:
                print("ORDER NUMBER = ", i)
                print("RESTURANT -",history[i][0])
                print("ORDER TOTAL =",history[i][1])
                print("-"*30)
                print("(M) MAIN MENU \n"
                "(E) EXIT")
                print("="*90)
        while True:
            r = input("SELECT A OPERATION: ").upper()
            if r == 'M':
                self.main_menu()
                break
            elif r == 'E':
                exit()
            else:
                print("INVALID INPUT TRY AGAIN")




###Term 8:
###In this phase, I've called the function res_corner, wherein the resturant's & food joint's can change the food price on 
###the menu, as per our needs. 
###The followig codes are for each of the resturants respectively.





    def res_corner(self):
        print()
        print(">"*25,"WELCOME TO SWIGGY PARTNER  PROGRAM","<"*25)
        print()
        count = 1
        for i in res:
            print(str(count)+")", i)
            count += 1
        print()
        print("="*90)
        while True:
            inp = input("SELECT YOUR RESTURANT: ")
            if int(inp) == 1:
                print("="*90)
                print()
                print("LOGIN SUCCESSFULL")
                print("WELCOME Mcdonalds")
                print()
                print("(1) UPDATE YOUR PRICES \n"
                "(2) MAIN MENU \n"
                "(3) EXIT")
                print("="*90)
                while True:
                    inp1 = input("SELECT A OPERATION: ")
                    if int(inp1) == 1:
                        print("="*90)
                        print()
                        count = 1
                        for i in Mcdonalds:
                            j = Mcdonalds[i]
                            print("("+str(count)+")",i.upper(),"\t"*5,"price","\t","Rs","{:.2f}".format(float(j)))
                            count += 1
                        print()
                        print()
                        print("(M) MAIN MENU \n"
                        "(E) EXIT")
                        print("="*90)
                        while True:
                            w = input().upper()
                            if w == 'M':
                                "hello"
                                self.main_menu()
                            elif w == 'E':
                                exit()
                            try:
                                if int(w) == 1:
                                    print("="*90)
                                    print("ITEM -","Mc chicken burger")
                                    print("OLD PRICE -", Mcdonalds["Mc chicken burger"])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Mcdonalds["Mc chicken burger"] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 2:
                                    print("="*90)
                                    print("ITEM -","Mc grill")
                                    print("OLD PRICE -", Mcdonalds["Mc grill"])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Mcdonalds["Mc grill"] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 3:
                                    print("="*90)
                                    print("ITEM -","Mc Chicken wrap      ")
                                    print("OLD PRICE -", Mcdonalds["Mc Chicken wrap      "])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Mcdonalds["Mc Chicken wrap      "] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 4:
                                    print("="*90)
                                    print("ITEM -","Mc coffee/ Mc latte")
                                    print("OLD PRICE -", Mcdonalds["Mc coffee/ Mc latte"])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Mcdonalds["Mc coffee/ Mc latte"] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")
                                
                                if int(w) == 5:
                                    print("="*90)
                                    print("ITEM -","coke & fries")
                                    print("OLD PRICE -", Mcdonalds["coke & fries"])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Mcdonalds["coke & fries"] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")
                                    
                            except:
                                print("INVALID INPUT PLAESE TRY AGAIN")
                    elif int(inp1) == 2:
                        self.main_menu()
                        break
                    elif int(inp1) == 3:
                        exit()
                    else:
                        print("INVALID INPUT PLEASE TRY AGAIN")

            elif int(inp) == 2:
                print("="*90)
                print()
                print("LOGIN SUCCESSFULL")
                print("WELCOME Subway")
                print()
                print("(1) UPDATE YOUR PRICES \n"
                "(2) MAIN MENU \n"
                "(3) EXIT")
                print("="*90)
                while True:
                    inp1 = input("SELECT A OPERATION: ")
                    print()
                    if int(inp1) == 1:
                        print("="*90)
                        print()
                        count = 1
                        for i in Subway:
                            j = Subway[i]
                            print("("+str(count)+")",i.upper(),"\t"*5,"price","\t","Rs","{:.2f}".format(float(j)))
                            count += 1
                        print()
                        print()
                        print("(M) MAIN MENU \n"
                        "(E) EXIT")
                        print("="*90)
                        while True:
                            w = input().upper()
                            if w == 'M':
                                "hello"
                                self.main_menu()
                            elif w == 'E':
                                exit()
                            try:
                                if int(w) == 1:
                                    print("="*90)
                                    print("ITEM -","Sub chicken kofta")
                                    print("OLD PRICE -", Subway["Sub chicken kofta"])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Subway["Sub chicken kofta"] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 2:
                                    print("="*90)
                                    print("ITEM -","Sub paneer tikka")
                                    print("OLD PRICE -", Subway["Sub paneer tikka"])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Subway["Sub paneer tikka"] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 3:
                                    print("="*90)
                                    print("ITEM -","Sub fresh tuna")
                                    print("OLD PRICE -", Subway["Sub fresh tuna"])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Subway["Sub fresh tuna"] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 4:
                                    print("="*90)
                                    print("ITEM -","coke & wedges")
                                    print("OLD PRICE -", Subway["coke & wedges"])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Subway["coke & wedges"] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")
                                
                                if int(w) == 5:
                                    print("="*90)
                                    print("ITEM -","cookies     ")
                                    print("OLD PRICE -", Subway["cookies     "])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Subway["cookies     "] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")
                                    
                            except:
                                print("INVALID INPUT PLAESE TRY AGAIN")
                    elif int(inp1) == 2:
                        self.main_menu()
                        break
                    elif int(inp1) == 3:
                        exit()
                    else:
                        print("INVALID INPUT PLEASE TRY AGAIN")

            elif int(inp) == 3:
                print("="*90)
                print()
                print("LOGIN SUCCESSFULL")
                print("WELCOME Origami")
                print()
                print("(1) UPDATE YOUR PRICES \n"
                "(2) MAIN MENU \n"
                "(3) EXIT")
                print("="*90)
                while True:
                    inp1 = input("SELECT A OPERATION: ")
                    if int(inp1) == 1:
                        count = 1
                        print("="*90)
                        print()
                        for i in Origami:
                            j = Origami[i]
                            print("("+str(count)+")",i.upper(),"\t"*5,"price","\t","Rs","{:.2f}".format(float(j)))
                            count += 1
                        print()
                        print("(M) MAIN MENU \n"
                        "(E) EXIT")
                        print("="*90)
                        while True:
                            w = input().upper()
                            if w == 'M':
                                "hello"
                                self.main_menu()
                            elif w == 'E':
                                exit()
                            try:
                                if int(w) == 1:
                                    print("="*90)
                                    print("ITEM -","chicken tteokbokki")
                                    print("OLD PRICE -", Origami["chicken tteokbokki"])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Origami["chicken tteokbokki"] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")


                                if int(w) == 2:
                                    print("="*90)
                                    print("ITEM -","kimchi jjigae    ")
                                    print("OLD PRICE -", Origami["kimchi jjigae    "])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Origami["kimchi jjigae    "] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 3:
                                    print("="*90)
                                    print("ITEM -","korean ramyun")
                                    print("OLD PRICE -", Origami["korean ramyun"])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Origami["korean ramyun"] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")

                                if int(w) == 4:
                                    print("="*90)
                                    print("ITEM -","japchae")
                                    print("OLD PRICE -", Origami["japchae"])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Origami["japchae"] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")
                                
                                if int(w) == 5:
                                    print("="*90)
                                    print("ITEM -","soju")
                                    print("OLD PRICE -", Origami["soju"])
                                    e = input("NEW PRICE - ").upper()
                                    print("PRICE UPDATED")
                                    Origami["soju"] = e
                                    print("="*90)
                                    print("(M)MAIN MENU    E(EXIT)")
                                    while True:
                                        A = input().lower()
                                        if A == 'm':
                                            self.main_menu()
                                        elif A == 'e':
                                            exit()
                                        else:
                                            print("INVALID INPUT PLEASE TRY AGAIN")
                                    
                            except:
                                print("INVALID INPUT PLAESE TRY AGAIN")
                    elif int(inp1) == 2:
                        self.main_menu()
                        break
                    elif int(inp1) == 3:
                        exit()
                    else:
                        print("INVALID INPUT PLEASE TRY AGAIN")

            else:
                print("INVALID INPUT PLEASE TRY AGAIN")

         


if __name__ == "__main__":
    swiggy()