password = input('Enetr a password :')

#check for lenght
if len(password) < 8 :
    print('too short!!!')

#check for uppercase
counter = 0
for word in password:
    if word.isupper() == True :
        counter += 1
if counter == 0 :
    print("it doesn't contaion upper case")

#check for uppercase
counter2 = 0
for word in password:
    if word.islower() == True :
        counter2 += 1
if counter2 == 0 :
    print("it doesn't contaion lower case")

#check for digit
counter3 = 0
for word in password :
    if word.isdigit() == True:
        counter3 += 1
if counter3 == 0 :
    print("it doesn't contaion digit")



