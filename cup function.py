print('Muhammad Hamza Hnif')
print('18B-041-CS')
print('Sec: A')
print('Lab Quiz')

# Function for cup.
def cup():
    x = int(input('How many cup of tea you want? '))
    cost = 25 *x
    print("Your total amount is Rs.",cost)
    note = int(input("Enter note of Pakistani rupees: "))
    
    
    if note == cost:
        print("Reminder is " ,0)
        print("Thanks forr purchasing ",x, " cups of tea(s) form our shop and paid ",cost, "Rupees.")
        
    if note > cost:
            print("You have entered Rs.",note)
            cal = int(note-cost)
            print("\nHere your change: \n","Rs.",cal)
            result = []
            pennies = int(cal * 100)
            for name, value in (('RS.100', 100),('RS.50',50),('R.20', 20),('RS.5', 5)):
                    count = int(pennies / value) 
                    pennies -= count * value
                    result.append(name)
                    result.append(count)
    
    print("Recieve before leave:\n")
    print(result)
    print("Thanks forr purchasing ",x, " cups of tea(s) form our shop and paid ",cost, "Rupees")
            
    if note < cost:
            print("Sorry! You have to pay more.")

cup()        


