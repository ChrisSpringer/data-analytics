# Christopher Springer
# 11/19/2026
# Exercise 4A Lab 1 Practicing read/write

file = open('about_me.txt', 'r')
# print(file.read(50))      # Prints the First 50 chars
# print(file.read(50))      # Prints the NEXT 50 chars 

# print(file.readline(10))
# print(file.readline())

# for i in range(1,5):
#    print(file.readline())

# print(file.readlines(1))    # Returns a list item with the first line of the txt file
# print(file.readlines(1))    # Returns the next line as a list item
# print(file.readlines(10))   # Returns the 3rd line as a list item
# print(file.readlines(10))   # Returns the first two lines in the text file as list items separately

# print(file.readlines(100))  # Returns the next two entire lines as a list. rounds up to not return part of a line
# print(file.readlines(-1))   # Returns the rest of the file by lines in a list, separating each entry by new line

var1 = file.read(50)
var2 = []
for i in range(1,5):
    var2.append(file.readline())
var3 = file.readlines(100)

print(f'First 50 characters: {var1}')
print(f'Next four lines, as list by line: {var2}')
print(f'Next 100 characters, as list by line, rounded up to complete lines: {var3}')
file.close()