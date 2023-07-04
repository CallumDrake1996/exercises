# LINE 2 is use to open the file in write mode. And then assigning it to a variable to use the write method.
pelicanW = open("pelican.txt", "w")

pelicanW.write("A wonderful bird is the pelican,\n")
# .close() is use to close the file. CLOSE files as it can cause a issue with larger files.
pelicanW.close() 

# pleicanA is use to open the file in append mode. while in append mode can use the write method to then add extra lines into the file that was opened
pelicanA = open("pelican.txt", "a")
pelicanA.write('His bill Holds more then his belican,\n')

# inList is the variable I have used to a list too which i have then used the appended to then add the list on to the file by using .writelines rather then just .write.
inList = ['he can take in his beak,\n', 'Enough food for a week, \n', 'But i\'m damned if i see how the helican.\n']

pelicanA.writelines(inList)
# REMEBER to close the file when you are done with it.
pelicanA.close()
