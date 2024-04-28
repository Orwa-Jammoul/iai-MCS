
#==========================================
# import libs

# pip install pyDatalog
from pyDatalog import pyDatalog as dl
import sys

#==========================================
# pyDatalog section

# --------- Create terms ---------
# --------- 1-Create Variable ---------
X = dl.Variable()
Y = dl.Variable()
Z = dl.Variable()
W = dl.Variable()
V = dl.Variable()

# --------- 2-Create Family Members (FACTS) ---------
name = dl.Variable()
father = dl.Variable()
mother = dl.Variable()
male = dl.Variable()
female = dl.Variable()
adopted = dl.Variable()

# --------- 3-Create Basic Relationships (RULES) ---------
parent = dl.Variable()
child = dl.Variable() 
son = dl.Variable()
daughter = dl.Variable()
sibling = dl.Variable()
brother = dl.Variable()
sister = dl.Variable()

# --------- 4-Create Advanced Relationships (RULES) ---------
uncle = dl.Variable()
aunt = dl.Variable()
maternal_uncle = dl.Variable()
maternal_aunt = dl.Variable()
paternal_uncle = dl.Variable()
paternal_aunt = dl.Variable()
cousin = dl.Variable()
niece = dl.Variable() 
nephew = dl.Variable() 

# --------- 5-Create In-law Relationships (RULES) ---------
spouse = dl.Variable() 
husband = dl.Variable() 
wife = dl.Variable() 
sisterSpouse_brother_in_law = dl.Variable() 
brotherSpouse_sister_in_law = dl.Variable() 
father_in_law = dl.Variable() 
mother_in_law = dl.Variable() 

# --------- 6-Create Step Relationships (RULES) ---------
step_parent = dl.Variable() 
step_father = dl.Variable() 
step_mother = dl.Variable() 
step_brother = dl.Variable() 
step_sister = dl.Variable() 


# --------- 7-Create Grandparent and Great-Grandparent Relationships (RULES) ---------
grandparent = dl.Variable()
grandfather = dl.Variable()
grandmother = dl.Variable()
great_grandparent = dl.Variable()
great_grandfather = dl.Variable()
great_grandmother = dl.Variable()

# --------- 8-Create Half-Sibling Relationships (RULES) ---------
half_sibling  = dl.Variable()
half_brother = dl.Variable()
half_sister = dl.Variable()

# --------- 9-Create Siblings-In-Law and Niece/Nephew-In-Law Relationships (RULES) ---------
sibling_in_law = dl.Variable() 
brother_in_law = dl.Variable() 
sister_in_law = dl.Variable() 
niece_in_law = dl.Variable() 
nephew_in_law = dl.Variable() 

# --------- 10-more complex Relationships (RULES)---------
step_son = dl.Variable() 
step_daughter = dl.Variable() 
step_uncle = dl.Variable() 
step_aunt = dl.Variable() 
adoptive_sibling = dl.Variable() 
adoptive_brother = dl.Variable() 
adoptive_sister = dl.Variable() 

# --------- Set Facts ---------
def setFacts():
    for person in dataSet:
        + name(person['id'], person['name'])
        + male(person['id']) if person['gender']=='m' else + female(person['id'])
        + father(person['father'], person['id'])
        + mother(person['mother'], person['id'])
        if person['isAdopted'] : + adopted(person['id'])

# --------- Set Rules ---------
def setRules():

    # --------- 3-Handling Basic Relationships ---------

    parent(X, Y) <= father(X, Y)                                     #علاقة الأب أو الأم (أحد الآباء) 
    parent(X, Y) <= mother(X, Y)                                     #علاقة الأب أو الأم (أحد الآباء) 
    child(X, Y) <= parent(Y, X)                                      #علاقة الابن 
    son(X, Y) <= child(X, Y) & male(X)                               #علاقة الابن الذكر
    daughter(X, Y) <= (child(X, Y) & female(X))                      #علاقة الابن الأنثى
    sibling(X, Y) <= father(Z, X) & father(Z, Y) & mother(W, X) & mother(W, Y) & (X != Y)  #علاقة الشقيق 
    brother(X, Y)<= sibling(X, Y) & male(X)                          #علاقةالأخ الشقيق 
    sister(X, Y)<= sibling(X, Y) & female(X)                         #علاقة الأخت الشقيقة 

    # --------- 4-Handling Advanced Relationships ---------
    uncle(X, Y) <= parent(Z, Y) & brother(Z, X)                      #علاقة العم/الخال
    aunt(X, Y) <= parent(Z, Y) & sister(Z, X)                        #علاقة العمة/الخالة
    maternal_uncle(X, Y) <=  mother(Z, Y) & brother(Z, X)            #علاقة الخال
    maternal_aunt(X, Y) <=  mother(Z, Y) & sister(Z, X)              #علاقة الخالة
    paternal_uncle(X, Y) <=  father(Z, Y) & brother(Z, X)            #علاقة العم
    paternal_aunt(X, Y) <=  father(Z, Y) & sister(Z, X)              #علاقة العمة

    cousin(X, Y) <= uncle(Z, Y) & parent(Z, X)                       #علاقة ابن/ابنة  العم/الخال/العمة/الخالة
    cousin(X, Y) <= aunt(Z, Y) & parent(Z, X) 

    niece(X, Y) <= sibling(Z, Y) & daughter(X, Z)                    #علاقة ابنة الشقيق
    nephew(X, Y) <= sibling(Z, Y) & son(X, Z)                        #علاقة ابن الشقيق

    # --------- 5-Handling In-law Relationships ---------
    spouse(X, Y) <= parent(X, Z) & parent(Y, Z) & (X != Y)              #علاقة الزوج/الزوجة
    husband(X, Y) <= spouse(X, Y) & male(X)                             #علاقة الزوج
    wife(X, Y) <= spouse(X, Y) & female(X)                              #علاقة الزوجة
    sisterSpouse_brother_in_law(X, Y) <= sister(Z, Y) & spouse(X, Z)    #علاقة زوج الأخت
    brotherSpouse_sister_in_law(X, Y) <= brother(Z, Y) & spouse(X, Z)   #علاقة زوجة الأخ
    father_in_law(X, Y) <= spouse(Z, Y) & father(X, Z)                  #علاقة الحمى
    mother_in_law(X, Y) <= spouse(Z, Y) & mother(X, Z)                  #علاقة الحماية

    # --------- 6-Handling Step Relationships ---------
    step_parent(X, Y) <= parent(Z, Y) & spouse(Z, X) & ~parent(X, Y)    #علاقة زوجة الأب /زوج الأم
    step_father(X, Y) <= mother(Z, Y) & spouse(Z, X)                    #علاقة زوج الأم
    step_mother(X, Y) <= father(Z, Y) & spouse(Z, X)                    #علاقة زوجة الأب
    step_brother(X, Y) <= step_parent(Z, Y) & son(X, Z)                 #علاقة الأخ من زوج الأم/زوجة الأب
    step_sister(X, Y) <= step_parent(Z, Y) & daughter(X, Z)             #علاقة الأخت من زوج الأم/زوجة الأب

    # --------- 7-Handling Grandparent and Great-Grandparent Relationships ---------
    grandparent(X, Y) <= parent(Z, Y) & parent(X, Z)                 #علاقة الجد/الجدة
    grandfather(X, Y) <= grandparent(X, Y) & male(X)                 #علاقة الجد
    grandmother(X, Y) <= grandparent(X, Y) & female(X)               #علاقة الجدة
    great_grandparent(X, Y) <= grandparent(Z, Y) & parent(X, Z)      #علاقة الجد/الجدة من الدرجة الثانية
    great_grandfather(X, Y) <= great_grandparent(X, Y) & male(X)     #علاقة الجد من الدرجة الثانية
    great_grandmother(X, Y) <= great_grandparent(X, Y) & female(X)   #علاقة الجدة من الدرجة الثانية


    # --------- 8-Handling Half-Sibling Relationships ---------
    half_sibling(X, Y) <= parent(Z, Y) & parent(Z, X) & ~sibling(X, Y)    #علاقة أخوة غير أشقاء
    half_brother(X, Y) <= half_sibling(X, Y) & male(X)                    #علاقة أخ غير شقيق
    half_sister(X, Y) <= half_sibling(X, Y) & female(X)                   #علاقة أخت غير شقيقة

    # --------- 9-Handling Siblings-In-Law and Niece/Nephew-In-Law Relationships ---------
    sibling_in_law(X, Y) <= spouse(Z, Y) & sibling(X, Z)                  #علاقة ابن الحمى/ابنة الحمى
    brother_in_law(X, Y) <= sibling_in_law(X, Y) & male(X)                #علاقة ابن الحمى
    sister_in_law(X, Y) <= sibling_in_law(X, Y) & female(X)               #علاقة ابنة الحمى
    niece_in_law(X, Y) <= sibling_in_law(X, Y) & daughter(X, Z)           #علاقة ابنة ابن الحمى
    nephew_in_law(X, Y) <= sibling_in_law(X, Y) & son(X, Z)               #علاقة ابن ابن الحمى

    # --------- 10-more complex Relationships ---------
    step_son(X, Y) <= spouse(Z, Y) & son(X, Z) & ~son(X, Y)                 #علاقة ابن الزوج/الزوجة
    step_daughter(X, Y) <= spouse(Z, Y) & daughter(X, Z) & ~daughter(X, Y)  #علاقة ابنة الزوج/الزوجة
    step_uncle(X, Y) <= step_parent(Z, Y) & brother(X, Z)                   #علاقة العم/الخال من زوج الأم/زوجة الأب
    step_aunt(X, Y) <= step_parent(Z, Y) & sister(X, Z)                     #علاقة العمة/الخالة من زوج الأم/زوجة الأب
    adoptive_brother(X, Y) <= brother(X, Y) & adopted(X)                    #علاقة الأخ بالتبني
    adoptive_sister(X, Y) <= sister(X, Y) & adopted(X)                      #علاقة الأخت بالتبني

#==========================================
# public variables and functions
dataSet= []

def getData():
    with open('data.csv', 'r') as file:
        i=0
        for line in file:
            i+=1
            if i==1:      # ignore first row
                continue
            record = line.rstrip(';\n').split(';')
            tempD = {
                'id': record[0],
                'name':record[1], 
                'gender':record[2], 
                'father':record[3],
                'mother':record[4],
                'isAdopted':record[5]=='1',
            }
            dataSet.append(tempD)

def getNames(ids):
    # listIds= [id for id, in ids]
    # names= [name(id,X) for id, in listIds]
    names= [name(id,X) for id, in ids]
    return names

def getNumber(label):
    while True:
        try:
            numInput=input(label)
            numInput= int(numInput)
            if(numInput>=0):
                    return numInput
        except:
            print("  ❌ '" + numInput + "' is invalid value! \n")
            command=input("type 0 to exit, or any to reEnter: ")
            if command=="0":
                    exitProgram()
            print("--------------- reEnter ----------------\n")

def allOrOne():
    command=input("1.   all.\n2.   for specific person.\nany. Exit.\n>>> ")
    if(command=="1"):
        return -1
    elif(command=="2"):
        return getNumber("please enter the person id: ")
    else:
        exitProgram()

#==========================================
# User Interface functions

def sayHello():
    print('\nWelcome')
    print('==================================================================')

def exitProgram():
    print("\n=================================================================="+
        "\nGood bye.\n")
    sys.exit()

def backToHome():
    print("\n==================================================================")
    command=input("Back to home page (1). Exit (any): ")
    if(command!="1"):
        exitProgram()

    parent(X, Y) <= father(X, Y)                                     #علاقة الأب أو الأم (أحد الآباء) 
    parent(X, Y) <= mother(X, Y)                                     #علاقة الأب أو الأم (أحد الآباء) 
    child(X, Y) <= parent(Y, X)                                      #علاقة الابن 
    son(X, Y) <= child(X, Y) & male(X)                               #علاقة الابن الذكر
    daughter(X, Y) <= (child(X, Y) & female(X))                      #علاقة الابن الأنثى
    sibling(X, Y) <= father(Z, X) & father(Z, Y) & mother(W, X) & mother(W, Y) & (X != Y)  #علاقة الشقيق 
    brother(X, Y)<= sibling(X, Y) & male(X)                          #علاقةالأخ الشقيق 
    sister(X, Y)<= sibling(X, Y) & female(X)                         #علاقة الأخت الشقيقة 

def mainMenu():
    getData()
    setFacts()
    setRules()
    print("-------------------------------------")
    print("------------- Home Page -------------")
    print("-------------------------------------")
    print("1.   Basic Relationships.")
    print("2.   Advanced Relationships.")
    print("3.   In-law Relationships.")
    print("4.   Step Relationships.")
    print("5.   Grandparent and Great-Grandparent Relationships.")
    print("6.   Half-Sibling Relationships.")
    print("7.   Siblings-In-Law and Niece/Nephew-In-Law Relationships.")
    print("8.   More Complex Relationships.")
    print("any. Exit.")
    print("---------------------------")
    command=input("Please type your choice number: ")
    # --------- Queries ---------
    if(command=="1"):
        inp = allOrOne()
        if inp==-1 :
            print("\nfather:")
            print(father(X, Y))
            print("\nmother:")
            print(mother(X, Y))
            print("\nbrother:")
            print(brother(X, Y))
            print("\nsister:")
            print(sister(X, Y))
        else:
            print("\nfather:")
            print(father(X, str(inp)))
            print("\nmother:")
            print(mother(X, str(inp)))
            print("\nbrother:")
            print(brother(X, str(inp)))
            print("\nsister:")
            print(sister(X, str(inp)))
    elif(command=="2"):
        inp = allOrOne()
        if inp==-1 :
            print("\nuncle:")
            print(uncle(X, Y))
            print("\naunt:")
            print(aunt(X, Y))
            print("\ncousin:")
            print(cousin(X, Y))
            print("\nniece:")
            print(niece(X, Y))
            print("\nnephew:")
            print(nephew(X, Y))

        else:
            print("\nuncle:")
            print(uncle(X, str(inp)))
            print("\naunt:")
            print(aunt(X, str(inp)))
            print("\ncousin:")
            print(cousin(X, str(inp)))
            print("\nniece:")
            print(niece(X, str(inp)))
            print("\nnephew:")
            print(nephew(X, str(inp)))
    elif(command=="3"):
        inp = allOrOne()
        if inp==-1 :
            print("\nsisterSpouse_brother_in_law:")
            print(sisterSpouse_brother_in_law(X, Y))
            print("\nbrotherSpouse_sister_in_law:")
            print(brotherSpouse_sister_in_law(X, Y))
            print("\nfather_in_law:")
            print(father_in_law(X, Y))
            print("\nmother_in_law:")
            print(mother_in_law(X, Y))
        else:
            print("\nsisterSpouse_brother_in_law:")
            print(sisterSpouse_brother_in_law(X, str(inp)))
            print("\nbrotherSpouse_sister_in_law:")
            print(brotherSpouse_sister_in_law(X, str(inp)))
            print("\nfather_in_law:")
            print(father_in_law(X, str(inp)))
            print("\nmother_in_law:")
            print(mother_in_law(X, str(inp)))
    elif(command=="4"):
        inp = allOrOne()
        if inp==-1 :
            print("\nstep_father:")
            print(step_father(X, Y))
            print("\nstep_mother:")
            print(step_mother(X, Y))
            print("\nstep_brother:")
            print(step_brother(X, Y))
            print("\nstep_sister:")
            print(step_sister(X, Y))
        else:
            print("\nstep_father:")
            print(step_father(X, str(inp)))
            print("\nstep_mother:")
            print(step_mother(X, str(inp)))
            print("\nstep_brother:")
            print(step_brother(X, str(inp)))
            print("\nstep_sister:")
            print(step_sister(X, str(inp)))
    elif(command=="5"):
        inp = allOrOne()
        if inp==-1 :
            print("\ngrandfather:")
            print(grandfather(X, Y))
            print("\ngrandmother:")
            print(grandmother(X, Y))
            print("\ngreat_grandfather:")
            print(great_grandfather(X, Y))
            print("\ngreat_grandmother:")
            print(great_grandmother(X, Y))
        else:
            print("\ngrandfather:")
            print(grandfather(X, str(inp)))
            print("\ngrandmother:")
            print(grandmother(X, str(inp)))
            print("\ngreat_grandfather:")
            print(great_grandfather(X, str(inp)))
            print("\ngreat_grandmother:")
            print(great_grandmother(X, str(inp)))
    elif(command=="6"):
        inp = allOrOne()
        if inp==-1 :
            print("\nhalf_brother :")
            print(half_brother (X, Y))
            print("\nhalf_sister:")
            print(half_sister(X, Y))
        else:
            print("\nhalf_brother :")
            print(half_brother (X, str(inp)))
            print("\nhalf_sister:")
            print(half_sister(X, str(inp)))
    elif(command=="7"):
        inp = allOrOne()
        if inp==-1 :
            print("\nbrother_in_law:")
            print(brother_in_law(X, Y))
            print("\nsister_in_law:")
            print(sister_in_law(X, Y))
            print("\nniece_in_law:")
            print(niece_in_law(X, Y))
            print("\nnephew_in_law:")
            print(nephew_in_law(X, Y))
        else:
            print("\nbrother_in_law:")
            print(brother_in_law(X, str(inp)))
            print("\nsister_in_law:")
            print(sister_in_law(X, str(inp)))
            print("\nniece_in_law:")
            print(niece_in_law(X, str(inp)))
            print("\nnephew_in_law:")
            print(nephew_in_law(X, str(inp)))
    elif(command=="8"):
        inp = allOrOne()
        if inp==-1 :
            print("\nstep_son:")
            print(step_son(X, Y))
            print("\nstep_daughter:")
            print(step_daughter(X, Y))
            print("\nstep_uncle:")
            print(step_uncle(X, Y))
            print("\nstep_aunt:")
            print(step_aunt(X, Y))
            print("\nadoptive_sibling:")
            print(adoptive_sibling(X, Y))
        else:
            print("\nstep_son:")
            print(step_son(X, str(inp)))
            print("\nstep_daughter:")
            print(step_daughter(X, str(inp)))
            print("\nstep_uncle:")
            print(step_uncle(X, str(inp)))
            print("\nstep_aunt:")
            print(step_aunt(X, str(inp)))
            print("\nadoptive_sibling:")
            print(adoptive_sibling(X, str(inp)))
    else:
        exitProgram()   
    
    backToHome()


while(True):
    sayHello()
    mainMenu()
