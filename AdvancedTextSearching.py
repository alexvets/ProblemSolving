"""     
     Given a list of strings of the same length,which will be named 'wordsList', and a string, which will be named 'sentence', determine 
     if any concatenation of the strings in the list occurrs inside the sentence. It supports finding multiple occurrences of any concatenation
     and printing their beginning and the whole substring. It doesn't support the case when the wordlist has words with more than one occurrence. 
     It can be easily modified to advance text searching, by appending blank string in front and at the end of the concatenation.
"""

sentence=input('Insert the string you want to test : ')

wordsList=input("Insert the list of strings, by separating them with the character (,) : ")
wordsList=wordsList.split(',')


print('The string we are checking is : ', sentence)
print('The list with the strings is :', wordsList)

#This is the length of words.
wordLen=len(wordsList[0]) 

#Number of words.
numberOfWords=len(wordsList)

#Length of the string.
sentenceLen=len(sentence)


print('Length of words : ',wordLen)
print('Number of words : ',numberOfWords)
print('Length of the string :',sentenceLen)

#Creating a list of tuples (word,number) where word is a string from list of words and number is an integer. 

wordsList1=[]          
i=0
for word in wordsList:
    i+=1
    wordsList1.append((word,i))

#Creating a dictionary with this list of tuples, so that deletion can be done through the string : del wordsList1_dict['{word}']
wordsList1_dict=dict(wordsList1) 

# We create a copy of the previous dictionary so that we can use it for temporary modifications, without losing the whole dictionary.
words_dict = wordsList1_dict.copy()   

print('The dictionary is : ',wordsList1_dict)




#Here is the whole story. Checking if concatenations exist and printing their beggining index and the substrings themselves.

indexList=[] #This is the list which is gonna save the beginning index of each concatenation. 

number=0 #This number counts the strings that appear inside the temporary concatenation.
j=0
while j<= sentenceLen-wordLen:
        
        substring=''
        for k in range(0,wordLen,1):
                substring=substring+sentence[k+j]

               
        if substring in words_dict:        #Here we check if the temporary sequence of chars from the string belongs to the dictionary of words. If yes, j goes two positions after
                number+=1              
                j=j+wordLen           
                del words_dict[substring]

        elif number>0 and (not (substring in words_dict)) and substring in wordsList1_dict:   #Here we check the case that we had a partial concatenation but it failed in the next step.
               j=j-(len(words_dict)-1)*wordLen
               words_dict = wordsList1_dict.copy()

               number=0
               continue
        elif number>0 and (not (substring in words_dict)) and (not substring in wordsList1_dict):
               j=j+1 
        else:
                j+=1
                words_dict = wordsList1_dict.copy()
                continue
                    
        # If the dictionary is empty, it means there is success. We modify some parameters to prepare for next iteration.    
        if not words_dict:
                      
                beginIndex=(j-numberOfWords*wordLen)+1         
                indexList.append(f'{beginIndex}')               
               
                words_dict = wordsList1_dict.copy()                  
                j=j-(numberOfWords-1)*wordLen
                
                print("A successful substring is : ",sentence[(j-2):(j-2+wordLen*numberOfWords)])
                print("         Beginning index : ", beginIndex)
                print("Let's go for next success.")
print(indexList)