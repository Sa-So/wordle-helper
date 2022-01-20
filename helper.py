
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
    # for rule in present_but_not_at:
    #     if(rule[0] not in word or rule[1] in word):
    #         return False

    # flag = True
    # for i,j in present_but_not_at:
    #     flag = False # there is a rule !
    #     for k in range(len(word)):
    #         if(word[k]==i):
    #             if(k!=j):
    #                 flag = True
    #                 break
    #             else:
    #                 flag = False
    #                 break
    # return flag
    '''debugged something below'''
    # print(present_but_not_at)

    # now the problem is if there are 2 rules which say that a letter is present 
    # but not at that location
    # like a is present but not at location 0 
    # and another rule says that a is present but not at location 1
    # then we cannot say that a is present at location 0 and 1
    # so we need to check if there are any rules which say that a is present at location 0 and 1
    
    #we need a list as 2nd argument ? 

    # adding rules 2 rules same letter 'a' 
    # abade
    # 'a' not at 2 our code will return true
    # 'a' not at 0 our code will return true
    #  abcde string satisfies the rules a is not present at 2 
    #  cbade string satisfies the rules a is not present at 0
    # this is not a bug : we are checking if every rule  is satisfied
    
    # 2 rules with yellow

    # prev rules that have been implemented , new word list should be gen .
    # then only new rules added should be checked
    # no need to check for prev rules
    # no need to check on all 13k words

    # 'l'


    present_flag = True
    not_at = True

    for i,j in present_but_not_at:
        if(i in word):
            # print(i,word)
            present_flag = True
            if(word[j]!=i):
                not_at = True
            else:
                not_at = False
                break;
        else:
            present_flag = False
            break;

    return (present_flag and not_at)
    '''awesome'''

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
    # print("hey")
    ct=0
    for word in words:
        # print(pl,end="")
        if(followRules(word)):
            print(word);ct+=1
    print(ct)

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
    print(present_at,not_present,present_but_not_at)
    printList()
'''debug statements below'''
# fillList("adieu","bbbbb")
# fillList("snort","bbyyg")
# listi = ["croft", "crypt" , "grypt" ,"wroot"] # wrong displayed !!!!
# for i in listi:
#     print(presentButNotAt(i))
'''debug statements above'''


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

