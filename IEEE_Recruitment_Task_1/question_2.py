#Testing for a palindrome

para= input("Enter a paragraph of maximum 100 words:") 
print("\n")                          #leaves a line after the text.
words= para.split()                   #splits and extracts the words from the paragraph
word_count=len(words)


if (word_count>100):
    print("Too many words. Para has more than a 100 words.")       # sends an error if too many words
else:
    palindrome_count=0
    for word in words:
  
        if len(word)>1:                                              #avoids single letter words like 'a' and 'I' 
         flipped_word= word[::-1]                                    #reverses the word
         if (word==flipped_word):                                    #checks if the number is palindrome by comparing with flipped word
             palindrome_count+=1
    
    if palindrome_count>0:
        print("The number of palindromes in the text is: ", palindrome_count,"\n")                  #printing the number of palindromes
    else:
        print("Number of palindromes is 0 \n")                                                      # returning 0 if no palindrome.
                                                  

                                                    
                                                     