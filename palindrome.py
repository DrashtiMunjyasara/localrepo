def reverse_string(og_string):
    rev_str=""
    for char in og_string:
        rev_str=char+rev_str
    return rev_str

og=input("Enter the string:")
og=og.replace(" ","").lower()
rev_str=reverse_string(og)
if(og==rev_str):
    print("palindrome")
else:
    print("Not palindrome")


#to check whether the string is palindrome or not ?.

#to check whether the string is palindrome or not .hii.

#to check whether the string is palindrome or not ?.


