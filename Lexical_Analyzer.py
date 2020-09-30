import re

operators = ["+","-","*","/","<",">","="]
delimeters = ["","{","}","[","]","(",")"]
keywords = ["if","else","do","while","break","continue","switch","case","short","int","long","double","float","char","return","void","NULL","struct"]

#in this part we opened the txt file
file = open("stringtoparse.txt","r")


#We convert txt file to array
for i in file:
    tokenArray = i.split()
   #print(tokenArray)


#Check the integer or not integer
def findInteger(element):
    identifier = re.compile(r"^[-+]?[0-9]+$", re.UNICODE)
    result = re.match(identifier, element)
    return result is not None


#check valid or not valid identifier
def notValidIdentifier(element):
    identifier = re.compile(r"^[^\d\W]\w*\Z", re.UNICODE)
    result = re.match(identifier, element)
    if((result is not None)== True):
        print(element, "-->", "IS A VALID IDENTIFIER")
    else:
        print(element, "-->", "IS NOT A VALID IDENTIFIER")


#we searched float number
def searchFloat(element):
    result = element.find(".")
    if (result != -1):
        return True

def checkFloat(element):
    result = isinstance(element,float)
    return result


print("***CENG2002 LEXICAL PARSER HOMEWORK FOR FINAL EXAM***")
print("***The String Is:")
print(i)

#Main function
#in this part we determine the type of array elements
def stringParser(tokenArray):
    print("***TOKENIZED VERSION IS***\n")
    for i in tokenArray:
        if(i in keywords):
            print(i,"-->","IS A KEYWORD")
        elif(i in operators):
            print(i,"-->","IS AN OPERATOR")
        elif(i in delimeters):
            print(i,"-->","IS A DELIMETER")
        elif(searchFloat(i)==True):
            i= float(i)
            if(checkFloat(i)==True):
                print(i,"-->","IS A REAL NUMBER")
        elif(findInteger(i)==True):
            print(i, "-->", "IS AN INTEGER")
        elif (notValidIdentifier(i) == True):
            print(i, "-->", "IS A VALID IDENTIFIER")


stringParser(tokenArray) #call function
file.close()






































