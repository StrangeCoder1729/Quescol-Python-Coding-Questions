#taking the input string from the user
string = input("Enter a String : ") 
result=''
for i in string:  
#iterating through each character of the string
    if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):  
     #seaching for vowels
        i = string.replace(i,string.upper(i)) 
#if vowel found replace it with empty string
    result += i 
    #concatenate rest of the string
print("String after removing the vowels :",result)


 