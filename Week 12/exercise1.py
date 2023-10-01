# Create a text file called  pi_digits.txt 
# 1. Read the file 
# 2. use readline() method 
# 3. write a number to the existing file 

f = open("pi_digits.txt", "r")

print(f.readline())
print(f.readline())
print(f.readline())

f.close()

f = open("pi_digits.txt", "a")
f.write("1279")
f.close()
