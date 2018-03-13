# This code creates random people who  may or may not have existed on Earth...
#Run again and again to see different results
#This code is Not Copied...!

#Plese like and give your suggestions...:-)

#More info coming soon..........
import random
import datetime


#____________________________________
#____________________________________
# Making a Phone no. from --> Stack Overflow   |
def phn(): #                                                                         |
    p = list('0000000000') #                                        |
    p[0] = str(random.randint(1,9)) #                       |
    for i in [1,2,6,7,8]: #                                                   |
        p[i] = str(random.randint(0,9)) #                    |
     #                                                                                         |
    for i in [3,4]: #                                                               |
        p[i] = str(random.randint(0, 8)) #                   |
         #                                                                                     |
    if p[3] == p[4] == 0: #                                                |
        p[5] = str(random.randint(1, 8))#                    |
    else : #                                                                               |
        p[5] = str(random.randint(0, 8)) #                  |
         #                                                                                     |
    n = range(10) #                                                             |
    if p[6] ==p[7] == p[8]:#                                            |
        n = (i for i in n if i != p[6]) #                                  |
     #                                                                                         |
    p[9] = str(random.choice(n)) #                             |
    p = ''.join(p) #                                
    return p[:3] + '-' + p[3:6] +'-' + p[6:] # 
#____________________________________



Fname = random.choice(["Janet", "Melaina", "Mary", "Celin", "Rachel", "Emily", "Emma", "Madison" , 'Olivia' ,"Sofia", "Ava"])

#*********************************************

Mname = random.choice(["Derek", "James", "Timothy", "Tom", "Jack", "Oliver", "Harry", "George", "Charlie", "Tony", "Jackson"])

name = random.choice([Fname, Mname])
#*********************************************
#  Gettin' the address right...
addr1 = str(random.randint(600, 4000))
addr2 = random.choice(["Stafford", "Chenoweth", "Flynn", "Bloomfield", "Tennyson", "Railway", "Purcell", "South", "North"])
addr3 = random.choice(["Street", "Road", "Avenue", "Place"])
addr4 = random.choice([ "AZ", "AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME" ])
addr = (addr1 + ", "+addr2 +" " +addr3 +", " + addr4)


#*********************************************
#His/Her surname
name2 = random.choice(["Muller", "Smith", "Cook" , "Jones", "Taylor" , "Root", "Brown" , "Wilson" , "Evans" , "Williams", "Swift"])

#*********************************************
#His/Her phone number
num = phn()

#*********************************************
#their country
county = random.choice(["USA", "United Kingdom", "Germany" , "France", "Italy" , "Australia", "Romania"])

#*********************************************
#their email id
mail1 = name.lower()
mail2 = str(random.randint(11, 99))
mail3 = random.choice(["gmail", "yahoo", "outlook" , "rediffmail", "iol" ])
mail4 = random.choice([".com", ".org"])
mail = (mail1+ mail2+ "@"+ mail3+ mail4)

#*********************************************
#their profession
proff = random.choice(["Software Engineer", "Teacher", "Self-Employed", "Accountant", "Writer","Artist", "Basketball Player", "Lawyer", "Physician", "Psychiatrist", "Technician" , "Police Officer" , "Dentist" , "Mechanic", "Scientist", "Physicist"])

#*********************************************
#their date of birth
year = random.randint(1955, 1985)
dob = datetime.date(year, random.randint(1, 12), random.randint(1,12))
age = 2017-year 

#__________________________________

#print("*"*35)

#printin' them out
print("Name :", name,name2, "\nAddress :", addr,"\nCountry :", county , "\nProfession :" , proff , "\nEmail :", mail, "\nBorn on :", dob, "(", age, "years )", "\nPhone No. :", num)

#print('*'*35)
