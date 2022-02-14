#1.) QUESTION1:
print("THE SOLUTION OF QUESTION1 :\n")
input_value = input("Enter the string: ").lower().split()
if len(input_value) == 1:
    input_value = input_value[0]
occurences = {}
for i in input_value:
    if i not in occurences:
        occurences[i] = 1
    else:
        occurences[i] += 1
print("The occurence(s) of:")
for i in occurences:
     print(f"\t\t\"{i}\"    is/are   {occurences[i]} ")

###################################################################################################################################

#QUESTION 2
print("\nTHE SOLUTION OF QUESTION2 :\n")
# DEFINING A FUNCTION TO CHECK IF GIVEN YEAR IS LEAP YEAR OR NOT
def is_leap_year(year):                                                                              
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    date = int(input("Day - "))
    month = int(input("Month - "))
    year = int(input("Year - "))
# CONDITION FOR GIVEN CONSTRAINTS IN THE QUESTION 
    if (date < 1) or (date > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                  
        print("Please use the given conditions for entering the current date\nC1 : 1<=month<=12\nC2 : 1<=day<=31\nC3 : 1800<=year<=2025")
        continue
# CONDITION FOR 31 DAYS IN 30 DAYS MONTH 
    if month in (4,6,9,11) and date == 31:                                                                         
        print("The given month has only 30 days\nPlease enter a valid date")
        continue
# CONDITION FOR FEBRUARY AND LEAP YEAR
    elif month == 2 and date >= 29:                                                                                
        if is_leap_year(year) and date != 29:
            print("The given month has only 29 days\nPlease enter a valid date")
            continue
        elif not is_leap_year(year):
            print("The given month has only 28 days\nPlease enter a valid date")
            continue
    break
# DEFINING MAX_DAYS FOR OUR COMFORT
if month == 2:                                                                                                      
    if is_leap_year(year):
        max_days = 29
    else:
        max_days = 28
elif month in (4,6,9,11):
    max_days = 30
else:
    max_days = 31
#  IF DATE IS MAX_DATE THEN CHANGING IT TO 1
if date == max_days:                                                                                               
    date = 1
# IF MONTH IS 12 THEN CHANGING IT TO 1 AND INCREASE THE YEAR BY 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    date += 1
# IF MONTH IS LESS THAN 10 THEN PRINTING WITH LEADING 0
if month<10:
    print("Next Date is: %d/0%d/%d" % (date,month,year))
else:
    print("Next Date is: %d/%d/%d" % (date,month,year))

###########################################################################################################################################

#3.) question3 :
print("\nTHE SOLUTION OF QUESTION3 :\n")
# TAKING INPUT LIST
list_in = eval(input("Enter the list: "))
list_out = []
for i in list_in:
    list_out.append((i, i**2))                                                                                     
print("Output:", list_out)

########################################################################################################################################

#Question 4
print("\nThe solution of Question 4 is:\n")
'''given_table is a list of lists'''
given_table = [ ["A+","Outstanding",10],
                ["A","Excellent",9],
                ["B+","Very Good",8],
                ["B","Good",7],
                ["C+","Average",6],
                ["C","Below Average",5],
                ["D","Poor",4] ]
while True:                                                                                                         #loop for making sure the user inputs the value between 4 and 10
    grade_point = eval(input("Enter the grade point of the student: "))
    if 4 <= grade_point <= 10:
        break
    else:
        print("The grade point must be between 4 and 10")
for i in given_table:                                                                                               #i is for iterating through the lists in the list and j is for iterating through the elements of each list
    for j in i:
        if j == int(grade_point):
            print("Your Grade is '%s' and %s Performance" % (i[0],i[1]))
            break

######################################################################################################################################

#5.) QUESTION 5 :

for i in range(6):
    initial=ord('A')
    for j in range(11):
        if i<=j<11-i:
         print(chr(initial),end='')
         initial+=1
        else:
            print(" ",end='')
    print()

###########################################################################################################################################

#Question 6
print("\nThe solution of Question 6 is:\n")
dict1 = {}
while True:                                                                                                         #Loop for inputting values
    name = input("Enter the name of the student: ")
    SID = int(input("Enter the SID of %s: " % name))
    dict1[SID] = name
    print("\nYou have entered %d value(s) till now" % len(dict1))
    while True:
        more_data = input("Do you want to enter more data? ")
        if more_data in ("N","n","No","no","NO"):
            more_data = 0
            break
        elif more_data in ("Y","y","Yes","yes","YES"):
            more_data = 1
            break
        else:
            print("\nPlease say yes or no")
            continue
    if more_data == 0:
        break
print("\na. Student Details:")                                                                                      #Q6(a)
for i in dict1:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict1[i],i))
dict2 = {}
for sorted_value in sorted(dict1.values()):                                                                         #Sorting the dictionary using student names
    for key,value in dict1.items():
        if value == sorted_value:
            dict2[key] = value
print("\nb. Student Details (sorted with respect to names):")                                                       #Q6(b)
for i in dict2:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict2[i],i))
dict3 = {}
for sorted_key in sorted(dict1):                                                                                    #Sorting the dictionary using SIDs
    for key,value in dict1.items():
        if key == sorted_key:
            dict3[key] = value
print("\nc. Student Details (sorted with respect to SIDs):")                                                        #Q6(c)
for i in dict3:
    print("The SID of \033[1m%s\033[0m is \033[1m%d\033[0m" % (dict3[i],i))
print("\nd. ", end="")                                                                                              #Q6(d)
while True:
    search_SID = int(input("Enter the SID of the student: "))
    if search_SID in dict1:
        print("The name of student whose SID is %d is \033[1m%s\033[0m" % (search_SID,dict1[search_SID]))
        break
    else:
        print("The SID you entered isn't entered\nPlease enter a valid SID to be searched\nList of valid SIDs: %s\n" % list((dict1.keys())))
        continue

########################################################################################################################################################
    
#7.) QUESTION 7 :
n=int(input("ENTER A NUMBER : "))
sum=0
def fab(n):
    if n==0 or n==1:
        return 1
    else:
        return fab(n-1)+fab(n-2)
for i in range(n):
    print(f"{fab(i)}",end=" ")
    sum=sum+fab(i)

average=sum/n
print(f"\nAverage is : {average}")

###################################################################################################################################################3

#Question 8
print("\nThe solution of Question 8 is:\n")
set1 = {1,2,3,4,5}
set2 = {2,4,6,8}
set3 = {1,5,9,13,17}
print("a. Set of all elements that are in Set1 and Set2 but not both:",end=" ")
set4 = set1^set2
print(set4)
print("b. Set of all elements that are in only one of the three sets Set1, Set2 and Set3:",end=" ")
set5 = set1^set2^set3
print(set5)
print("c. Set of elements that are in exactly two of the sets Set1, Set2 and Set3:",end=" ")
set6 = (set1|set2|set3) - (set1^set2^set3) - (set1&set2&set3)
print(set6)
print("d. Set of all integers in the range 1 to 10 that are not in Set1:",end=" ")
set7 = set()
for i in range(1,11):
    if i not in set1:
        set7.add(i)
print(set7)
print("e. Set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3:",end=" ")
set8 = set(range(1,11)) - (set1|set2|set3)
print(set8)
