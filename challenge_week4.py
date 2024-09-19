#################################Extracting Sub-Strings###################################
# Extracting Sub-Strings Practice #1
# Extract the first word of the following sentence using slicing, and display it on the screen:
my_text = 'Controlling complexity is the essence of programming'
result1 = my_text
# Hint: "Controlling" is 11 characters long.
print(result1[0:12])


# Extracting Sub-Strings Practice #2
# Take every third character starting from the ninth to the end of the sentence, and print the result.
# "Never trust a computer you can't throw out a window"

text = "Never trust a computer you can't throw out a window"
start_index = 8  
substring = text[start_index:]  
result2 = substring[::3] 
print(result2)

# Extracting Sub-Strings Practice #3
# Reverses the position of all the characters in the following sentence and displays the result on the screen.
# "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"

sentence = "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
result3 = sentence[::-1]  
print(result3)