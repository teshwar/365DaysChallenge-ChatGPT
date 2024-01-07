"""
  Day 6: File Handling
        Read from and write to a text file.
        Handle different file-related exceptions.
"""

"""
6 access mode in Python 
-Read Only('r')
-Read and Write('r+')
-Write Only('w')
-Write and Read('w+')
-Append Only('a')
-Append and Read('a+')

open file using open(r"path to file", "access mode")
can write using write() or writelines()
can read using read() or readlines()

seek(0):
seek take file handle to nth position, in this case to beginning
"""


#Write data in a file, creates one if does not exist
file1 = open("myfile.txt", "w")
L = ["Hi my name is \n", "My name is \n", "Shikishikichit slim shady \n"]

#\n is placed to indicated the EOL(end of a line)
file1.write("Hi \n")
file1.writelines(L)
file1.close() #file must be close to change  access mode



file1 = open("myfile.txt", "r+")
print("Output of read() is: ")
print(file1.read())
print

file1.seek(0)
print("Output for readline() is: ")
print(file1.readline())
print()
file1.seek(0)

#Difference between readline and read and readlines
print("Ouput of read(9) is: ")
print(file1.read(9))
print()

print("Output of readline(9) is: ")
print(file1.readline(9))
print()

print("Output of Readlines function is: ")
print(file1.readlines())
print()

file1.close()


#append mode
file1 = open("myfile.txt", "a+")
file1.write("the end \n")
file1.close()

file1 = open("myfile.txt", "r")
print("We can see after using append mode, write is at the end  of file: ")
print(file1.read())
file1.close()