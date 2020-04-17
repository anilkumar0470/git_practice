#String is a collection of ordered characters represented in single or double quotes
st = "Welcome to every one"
#Built in methods
print len(st)
#it is used to display the length of the given string including space as a single character
print st.lower()
#it will print the entire string in lower case
print st.upper()
#it will print the entire string in lower case
print st.islower()
#If the string contain only lower case then it will return true otherwise false
print st.isupper()
#If the string contain only upper case then it will return true otherwise false
print st.title()
#it is used to convert the every starting letter of the word in the entire string into upper case
print st.istitle()
#it return true if the string contain every word in uppercase other wise it will return false
print st.isdigit()
##If the string contain only digit then it will return true otherwise false
print st.isalpha()
##If the string contain only alphabets then it will return true otherwise false
print st.isalnum()
#If the string contain any digit or alphabet or both then it will return true otherwise false
print st.count('l')
print st.count("all")
#it is used to find the occurances of the character or string in given piece of text
print st.find('e')
#it is used to find the index of character or string in given piece of string
print st.startswith("wel")
#if the string startswith given pattern then it will return true otherwise false
print st.endswith("all")
#if the string endswith  given pattern then it will return true otherwise false
print st.lstrip()
#it used to remove or strip or escape  the blank space in the left side
print st.rsplit()
#it used to remove or strip or escape  the blank space in the right side
print st.split()
#it used to remove or strip or escape  the blank space in the both sides i.e right or right
#st[lowerindex:upperindex]
#Then it will print from lower index to (upper index) - 1
print st[1:5]

#the indication of [] is used to take the certain part of the string
#output is:"el",because it will print from lower index 1 to upper index 4(5-1)
#IN python index is always start from zero
print str.index('o')
#it is used to find the index of character or string in given piece of string
print st.split()
#Method is used to split the given string into words


