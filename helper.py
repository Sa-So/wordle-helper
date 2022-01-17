
with open('words.txt','r') as f:
    words = f.read().splitlines()

present_at = [] # green
present_but_not_at = [] # yellow
not_present = [] # black

def presentAt(word):
    # least complex
    # print(present_at)
    flag = True
    for i,j in present_at:
        if(word[j]!=i):
            flag = False
            break
    return flag

def presentButNotAt(word):
    # print(present_but_not_at)
    # every pair in present_but_not_at must be present in word but not at that location 

    flag = True
    for i,j in present_but_not_at:
        flag = False # there is a rule !
        for k in range(len(word)):
            if(word[k]==i):
                if(k!=j):
                    flag = True
                    break
                else:
                    flag = False
                    break
    return flag

def notPresent(word):
    # print(not_present)
    flag = True
    for i in not_present:
        if(i in word):
            flag = False
            break
    return flag


def followRules(word):
    # print("following rules ... ")
    # if()
    return ( presentAt(word) and presentButNotAt(word) and notPresent(word) )


def printList():
    print("hey")
    pl=0
    for word in words:
        # print(pl,end="")
        if(followRules(word)):
            print(word)
        pl+=1

        # print(i)
def fillList(word,colorString):
    for i in range(5):
        if(colorString[i]=='g'):
            present_at.append((word[i],i))
        elif(colorString[i]=='y'):
            present_but_not_at.append((word[i],i))
        else:
            not_present.append(word[i])
    

for i in range(5):
    inp = input("Enter the word string ")
    colorString = input("Enter the color string ")
    fillList(inp,colorString)
    print(not_present)
    printList()
# fillList("gggag","bbbyb")
# print(presentAt("abaca"))
# printList()




# for word in words:


# traversing the word 


# traverse the rules and see if they all are followed 
# if they are followed then add the word to the list
# if not then remove the word from the list





# previous words tend not to repea
# rank words on their usability in english - used more in daily conversations / general  
# AI - that reduces the no. of tries it requires to crack the password
# strategy -
# our strategy was to make sure every rule is staisfied after every iteratiion
# is to make / guess a word that uses all the letters that are not used till now
# so make use of letters not present in not_present list 


# 1. try to find the words that are present at all the locations
# 2. try to find the words that are present at all the locations but not at the same location
# 3. try to find the words that are not present in the word
# 4. try to find the words that are present at all the locations but not at the same location and not present in the word
