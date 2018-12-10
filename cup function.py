print('Muhammad Hamza Hanif')
print('18B-041-CS')
print('Sec: A')
print('Lab Quiz')

def f():
    # Asking no. of coffee & giving its cost.
    coffee = int(input('How many cup of tea you want? '))
    cost = 25 * coffee
    print("Your total amount is Rs.",cost)

    # Inserting rupees.
    notes = int(input("Enter note of Pakistani rupees: "))
    print('Ypu have inserted', notes)

    # If cost is equals to inserted money. 
    if notes == cost:
        print("Reminder is " ,0)
        print("Thanks for purchasing ",coffee, " cups of tea(s) form our shop and paid Rs.",cost,".")

    # If inserted notes less than total cost.    
    if notes < cost:
        print("Sorry! You have to pay more.")
    
    if notes > cost:
        change = notes-cost
        change_int = int(change)
        change_str = str(change)
        change_lst = list(change_str)
        digits     = []

        for digit in range(len(change_lst)):
            cath = int(change_int % 10)   # '% 10' it will cath last unit reminder, i.e. 1234 % 10 = 4. If we use 1234 % 100 = 34 as reminder.
            change_int //= 10  # By int div. to evalute simpler i.e. 1234 // 10 = 123, 123 // 10 = 12, 123 // 10 = 1, we are using 10 as to approach above.
            digits.append(cath)
        digits.reverse()     # if we dont use reverse(), we get ['4','3','2','1']. Therefore; by using reverse() we get list as in order ['1','2','3','4'].


        # Working on notes.
        _1000 = 0
        _500  = 0
        _100  = 0
        _50   = 0
        _20   = 0
        _10   = 0
        _5    = 0
        _1    = 0


        if len(digits) == 1:        # [1] >>> [0,1]
                digits.reverse()
                digits.append(0)
                digits.reverse()
        if len(digits) == 2:        # [0,1] >>> [0,0,1]
                digits.reverse()
                digits.append(0)
                digits.reverse()
        if len(digits) == 3:        # [0,0,1] >>> [0,0,0,1]
                digits.reverse()
                digits.append(0)
                digits.reverse()
                
        # It works only if notes is greater than & equals to thousand.
        if len(digits)==4:  
            _1000 += digits[0]  # At 0 iteration of list, any digit is added to varuiable _1000.

            if digits[1] >= 5: # At 1 iteration of list, which for hundered >= 5. 
                _500 += 1       # At 1 iteration of list, simply add 1 to vsriable _500.
                a = digits[1]-5 # Suppose wwe have 9, it minus from 5 to give reminder. 
                _100 += a       # i.e. We have Rs.900 then we get Rs.500 note & left for Rs.100 note(s).
            else:
                _100 += digits[1] # At 1 iteration of list, > 4 we Rs.100 note(s).

            if digits[2] >= 5:  # At 2 iteration of list, which is for ten >= 5 more than& equals to Rs.50.
                _50 += 1        # We have Rs.80, it adds Rs.50 note. 
                b = digits[2]-5 # We have left Rs. 30, if we have Rs,90.
                if b >= 2 and b < 4:      # For Rs.20.
                    _20 += 1    # We add Rs.20 & left Rs.10.
                    c = b - 2   # We have (Rs.80 - Rs.50) - Rs.20 = Rs.10.
                    _10 += c    # It simply adds note(s) of Rs.10 in variable _10.
                else:
                    _10 += b    # We add Rs.10 to it if we have Rs.15 left.

            if digits[2] < 5:  # At 2 iteration of list, which is for ten < 5 means Rs.40.
                if digits[2] >= 2 and digits[2] < 4:      # For Rs.20.
                    _20 += 1    # We add Rs.20 & left Rs.10.
                    x = digits[2]-2
                    _10 += x
                else:
                    _10 += digits[2]    # We add Rs.10 to it if we have Rs.15 left.
                    
            if digits[3] >= 5:  # At iteration 3, which is for unit, for Rs.5.
                _5 += 1         # If we have Rs.9, it will give Rs.5 note.
                d = digits[3] - 5       # Left are Rs.1 and add it.
                _1 += d
            else:
                _1 += digits[3]  # If we have Rs.4 it will give 4 notes of Rs.1. 
        print("Thanks for purchasing ",coffee, " cups of tea(s) form our shop and paid Rs.",cost,".")
        print('The notes are: ')
        print('Rs.1000: ',_1000)
        print('Rs.500: ',_500)
        print('Rs.100: ',_100)
        print('Rs.50: ',_50)
        print('Rs.20: ',_20)
        print('Rs.10: ',_10)
        print('Rs.5: ',_5)
        print('Rs.1: ',_1)
f()
