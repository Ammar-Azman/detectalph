str_1 = list('''

Once there was an elephant,
Who tried to use the telephant
No! No! I mean an elephone
Who tried to use the telephone

''')
#remove \n and \r
str_1 = list(filter(lambda a:a != '\n' and a != '\r' and a != " ", str_1))


# asking line from user 
line = int(input("How many lines will be there?:"))
if line == 4:
    print("Yes, you are right!")

else:
    print("I am sorry it's wrong, try again.")
    
# counting vowels and consonent
vow = []
symbol = []
consonants = []
for alp in str_1:
    if (alp == 'a' or alp == 'A' or 
        alp == 'e' or alp == 'E' or
        alp == 'i' or alp == 'I' or 
        alp =='o' or alp == 'O' or 
        alp =='u' or alp == 'U'):
        vow.append(alp)
        
    elif alp == "!" or alp == ",":
        symbol.append(alp)
    
    else:
        consonants.append(alp)
        
print("")
print("The result:")
print("")
print("Number of vowels:", len(vow))
print("")
print("Number of consonants:", len(consonants))
