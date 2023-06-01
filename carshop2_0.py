#Car shopping program with various makes and models as well as a financing calculator

makes = ["Toyota", "Ford", "Mazda"]# makes
models = ["4runner", "rav4", "tacoma"]# toyota models
modelsf = ["f150", "escape", "focus"]# ford models
modelsm = ["cx5", "miata", "mazda3"]# mazda models

import random
import time

def Financing(): # finance function
    financing = input("Would like to see our financing options for this vehicle?")
    if financing == "Yes":
        score = random.randint(0,3)
        print("Financing for our " + modelchosen + " is in 36 monthly payments with options for 10 20 or 30 percent down")
        fnumber = input("10, 20, or 30 down?")
        if fnumber == "10" or "20" or "30":
            print("Down payment recorded.")
            time.sleep(1)
            Creditcheck()
            if score == 1:
                apr = 14
                print("You have a credit score of 650. Your apr will be at 14%")
            elif score == 2:
                apr = 7
                print("You have a credit score of 700. Your apr will be at 7%")
            elif score == 3:
                apr = 4
                print("You have a credit score of 750. Your apr will be at 4%")
            fdown = (int(fnumber)/100)*price
            amtfin = (price - int(fdown))*(apr/100)
            ffinal = (price - int(fdown)+amtfin)/36
            print("All done! That is $" + str(fdown) + " down and monthly payments of $" + str(ffinal))

def Creditcheck(): # creditcheck function
    creditcheck = input("Can we run a credit check to see what your percentage rate will be?")
    if creditcheck == "Yes":
        print("Running credit report")
        time.sleep(1)
        print("---10%")
        time.sleep(2)
        print("---34%")
        time.sleep(1)
        print("---85%")
        time.sleep(1)
        print("---100%")
        time.sleep(2)

print("Welcome to my car shop")
enter = input("Would you like to see our options?\n")
if enter == "Yes":
    makechoice = input("Here are our options today\n" + str(makes) + "\n" + "Which would you like to look at?\n") 
    if makechoice == makes[0]: # toyota option
        print("Excellent! You have chosen Toyota. Here are our models\n" + models[0] + " " + models[1] + " " + models[2])
        modelchosen = input("Choose a model\n")
        if modelchosen == models[0]:
            print("You have chosen a 4Runner!")
            options = { # options for 4runner
                "color" : ["red", "yellow", "grey"],
                "year" : ["2005","2009","2014"],
                "mileage" : ["230,000","180,000","140,000"],
                "price" : ["5999","11999","15999"]
            }
        if modelchosen == models[1]:
            print("You have chosen a Rav4!")
            options = { # options for rav4
                "color" : ["white","red","black"],
                "year" : ["2018", "2022", "2023"],
                "mileage" : ["95,000", "11,000", "4,000"],
                "price" : ["18000","26000","34000"]
            }
        if modelchosen == models[2]:
            print("You have chosen a Tacoma!")
            options = { # options for tacoma
                "color" : ["tan","graphite","black"],
                "year" : ["2021","2022","2022"],
                "mileage" : ["22,000","12,000","8,000"],
                "price" : ["36000","45000","53000"]
            }
    if makechoice == makes[1]: # ford option
        print("You have chosen Ford. Here are our models\n" + modelsf[0] + " " + modelsf[1] + " " + modelsf[2])
        modelchosen = input("Choose a model\n")
        if modelchosen == modelsf[0]:
            print("You have chosen a F150!")
            options = { # options for f150
                "color" : ["white","red","grey"],
                "year" : ["2021","2022","2023"],
                "mileage" : ["23,000","18,000","5,000"],
                "price" : ["43000","53000","60000"]
            }
        if modelchosen == modelsf[1]:
            print("You have chosen a Escape!")
            options = { # options for escape
                "color" : ["orange","red","black"],
                "year" : ["2012","2014","2015"],
                "mileage" : ["130,000","123,000","97,000"],
                "price" : ["8000","12000","15000"]
            }
        if modelchosen == modelsf[2]:
            print("You have chosen a Focus!")
            options = { # options for focus
                "color" : ["white","black","blue"],
                "year" : ["2014","2017","2019"],
                "mileage" : ["145,000","110,000","68,000"],
                "price" : ["8000","12000","18000"]
            }
    if makechoice == makes[2]: # mazda option
        print("You have chosen Mazda. Here are our models\n" + modelsm[0] + " " + modelsm[1] + " " + modelsm[2])
        modelchosen = input("Choose a model\n")
        if modelchosen == modelsm[0]:
            print("You have chosen a CRX!")
            options = { # options for crx
                "color" : ["grey","blue","red"],
                "year" : ["2014","2015","2020"],
                "mileage" : ["68000","52000","28000"],
                "price" : ["22000","25000","32000"]
            }    
        if modelchosen == modelsm[1]:
            print("You have chosen a Miata!")
            options = { # options for miata
                "color" : ["white","red","black"],
                "year" : ["2016","2017","2019"],
                "mileage" : ["85,000","79,000","52,000"],
                "price" : ["18000","20000","28000"]
            }
        if modelchosen == modelsm[2]:
            print("You have chosen a Mazda3!")
            options = { # options for mazda3
                "color" : ["black","white","red"],
                "year" : ["2020","2021","2023"],
                "mileage" : ["20,000","16,000","7,000"],
                "price" : ["43000","47000","52000"],
            }
    #Option 1
    colorget0 = options.get("color")[0]
    yearget0 = options.get("year")[0]
    mileget0 = options.get("mileage")[0]
    priceget0 = options.get("price")[0]
    #Option 2
    colorget1 = options.get("color")[1]
    yearget1 = options.get("year")[1]
    mileget1 = options.get("mileage")[1]
    priceget1 = options.get("price")[1]
    #Option 3
    colorget2 = options.get("color")[2]
    yearget2 = options.get("year")[2]
    mileget2 = options.get("mileage")[2]
    priceget2 = options.get("price")[2]
    #Dictionary options as vars converted into sentences
    options0 = colorget0 + " " + yearget0 + " " + mileget0
    options1 = colorget1 + " " + yearget1 + " " + mileget1
    options2 = colorget2 + " " + yearget2 + " " + mileget2
    optionsfull = "1. " + options0 + "\n2. " + options1 + "\n3. " + options2
    print("Heres the color, year, and mileage options we have for " + modelchosen + "s")
    print(optionsfull)
    #Stringname is a printed representation of dictionaries options of the car + prices
    stringname0 = ("This is a " + yearget0 + " " + modelchosen + " with a " + colorget0 + " clearcoat. It has " + mileget0 + " miles. It starts at $" + priceget0)
    stringname1 = ("This is a " + yearget1 + " " + modelchosen + " with a " + colorget1 + " clearcoat. It has " + mileget1 + " miles. It starts at $" + priceget1)
    stringname2 = ("This is a " + yearget2 + " " + modelchosen + " with a " + colorget2 + " clearcoat. It has " + mileget2 + " miles. It starts at $" + priceget2) 
    optionschoice = input("Number?...")
    if optionschoice == "1" :
        price = int(priceget0)
        stringname = stringname0
        print(stringname)
        Financing()
    if optionschoice == "2" :
        price = int(priceget1)
        stringname = stringname1
        print(stringname)
        Financing()
    if optionschoice == "3" :
        price = int(priceget2)
        stringname = stringname2
        print(stringname)
        Financing()
#Exceptions      
else:
    print("Okay have a nice day!")