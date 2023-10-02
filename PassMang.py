2import random
import string
import tkinter

menu = ' '  #creates menu to choose option of creating or viewing passwords

while menu != '1' or menu != '2':               #if menu is not equal to 1 or 2 display menu
    menu = input('Save new password or view old? '
                 '\n1. Input new password: '
                 '\n2. View passwords: '
                 '\n3. Exit: ' )

    if menu == '1':
        sw = input ('Software/Website? : ')
        
        user = input('Username? : ')
        
        length = int(input('How long would you like the password to be? : '))
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        numbers = string.digits             #creates password 
        symbols = string.punctuation


        pw = lower + upper + numbers + symbols  #combines parts of password

        temp = random.sample(pw, length) #stores them in a temporary variable to randomize charcters

        password = ''.join(temp) #add to final variable

        file = open('passmang.txt', 'a+') #open and append to file
        newpass = (sw+'|'+user+'|'+password)
        file.write('\n')
        file.write(newpass)
        file.close()

        print('\nYour password was created succesfullly. ')
    
    if menu == '2':
        file = open('passmang.txt','r') #open and read from file
        for i in file:
            data = i.split('|')
            print(data)

    if menu == '3':
        exit()


    

