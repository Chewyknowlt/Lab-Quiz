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

    # If inserted notes greater than total cost.
    if notes >  cost:
        change     = int(notes - cost)
        change_int = int(change)
        change_str = str(change)
        change_lst = list(change_str)
        digits     = []

        for digit in range(len(change_lst)):
            cath = int(change_int % 10)   # '% 10' it will cath last unit reminder, i.e. 1234 % 10 = 4. If we use 1234 % 100 = 34 as reminder.
            change_int //= 10  # By int div. to evalute simpler i.e. 1234 // 10 = 123, 123 // 10 = 12, etc, we are using 10 as to approach above.
            digits.append(cath)
        digits.reverse()       # It will braek int into integer list.

    # Working on notes.
    _1000 = 0
    _500  = 0
    _100  = 0
    _50   = 0
    _20   = 0
    _10   = 0
    _5    = 0
    _1    = 0


    if len(digits)==4:
        _1000 += digits[0]
        if digits[1]>=5:
            _500 += 1
            c = digits[1]-5
            _100 += c
        else:
            _100 += digits[1]
        if digits[2]>=5:
            _50 += 1
            d = digits[2]-5
            if d>=2 and d<4:
                _20 += 1
                e = d-2
                _10 += e
            elif d>=4:
                _20 +=2
                f = d-4
                _10 +=f
            else:
                _10 += d
        else:
            if digits[2]>=2 and digits[2]<4:
                _20+=1
                h=digits[2]-2
                _10+=h
            elif digits[2]>=4:
                _20+=2
                i=digits[2]-4
                _10+=i
            else:
                _10+=digits[2]
        if digits[3]>=5:
            _5 +=1
            g=digits[3]-5
            _1 += g
        else:
            _1 +=digits[3]
        
    elif len(digits)==3:
        if digits[0]>=5:
            _500 += 1
            c = digits[0]-5
            _100 += c
        else:
            _100 += digits[0]
        if digits[1]>=5:
            _50 += 1
            d = digits[1]-5
            if d>=2 and d<4:
                _20 += 1
                e = d-2
                _10 += e
            elif d>=4:
                _20 +=2
                f = d-4
                _10 +=f
            else:
                _10 += d
        else:
            if digits[1]>=2 and digits[1]<4:
                _20+=1
                h=digits[1]-2
                _10+=h
            elif digits[1]>=4:
                _20+=2
                i=digits[1]-4
                _10+=i
            else:
                _10+=digits[1]
        if digits[2]>=5:
            _5 +=1
            g=digits[2]-5
            _1 += g
        else:
            _1 +=digits[2]

    if len(digits)==2:
        if digits[0]>=5:
            _50 += 1
            d = digits[0]-5
            if d>=2 and d<4:
                _20 += 1
                e = d-2
                _10 += e
            elif d>=4:
                _20 +=2
                f = d-4
                _10 +=f
            else:
                _10 += d
        else:
            if digits[0]>=2 and digits[0]<4:
                _20+=1
                h=digits[0]-2
                _10+=h
            elif digits[0]>=4:
                _20+=2
                i=digits[0]-4
                _10+=i
            else:
                _10+=digits[0]
        if digits[1]>=5:
            _5 +=1
            g=digits[1]-5
            _1 += g
        else:
            _1 +=digits[1]

    print('The notes are as: ')        
    print("Rs.1000 = ",_1000)
    print("Rs.500  = ",_500)
    print("Rs.100  = ",_100)
    print("Rs.50   = ",_50)
    print("Rs.20   = ",_20)
    print("Rs.10   = ",_10)
    print("Rs.5    = ",_5)
    print("Rs.1    = ",_1)
    print("Thanks for purchasing ",coffee, " cups of tea(s) form our shop and paid Rs.",cost,".")
f()
