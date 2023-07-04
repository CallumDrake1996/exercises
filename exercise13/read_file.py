# assigned output to open the file in read only mode and then read it as it is on the .txt file.
output = open('pelican.txt', 'r').read()


# printed the file type of it below.
print('the type of data on this file is:', type(output))
# break to seperate code unnecessary but to help me see what is going on better. print('')
print('')
# then printed it out using .read() method.
print(output)

print('')

# assigned output2 to open the file in read only mode and then read it and then convert it into a list.
output2 = open('pelican.txt', 'r').readlines()
print('the type of data on this file is:', type(output2))

print('')
# printed the var output2 to show it as the list.
print(output2)

print('')
# using the len function to count the amount of items in the list.
print('the amout of items that are in the list is:',len(output2))

print('')


# using a for loop to print each item in the list. but aslo used the .strip() method to remove the extra spaces. so there is no blanklines in the print.
for x in output2:
    x = x.strip()
    print(x)
