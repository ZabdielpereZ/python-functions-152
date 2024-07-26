def div():
    print('='*50)

# Different types of parameters 

# Basic parameters : assume their value from arguments passed into the defined function when it's called

def name_printer(first, middle, last):
    print(f"hello, {first}{middle}{last}!")

#-- positional arguments : the position of the argument determines which parameter it becomes the value of in our function
name_printer("Travis", "Cline", "Peck")
name_printer("Peck", "Travis", "Cline")

#-- keyword arguments : we can explicitly store which parameter takes which value 
name_printer(last ="Peck", first="Travis", middle="Cline")

div()

#-- Default Parameters : Give a perameter a default value if nothing is passed into the function 

def greeting(name= "World!"):
    print(f"Hello, {name}!")

greeting()
greeting("Travis")

div()

#--- *args : unknown number of arguments, brought into the function as a tuple 

def vet_hands(staff, *vols):
    print(f"on satff today we have {staff[0]} and {staff[1]}!")
    if vols:
        print("They will be assited by the following volunteers:")
        for vol in vols:
            print(vol)
        
vet_hands(["Dr. Adam", "Dr. Jones",], "Dylan", "Travis", "Grace", "Josh", "Walter", "Phillip")

div()

#-- **kwargs : unknown amount  of keyword arguments, brough into the function as a dictionary

def routine(**daily_events):
    print(daily_events)

routine(morning ="I wakee up, brush my teeth, and have breakfast", mid_morning= "Walk my dog", afternoon="Grading and preppering for class", evening= "In class", dinner_time="time to eat something", night= "Go to sleep")