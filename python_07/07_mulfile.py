# multiple lines of user input into a file


f = open("data.txt", "w")

for i in range(3):
    line = input("Enter a line: ")
    f.write(line + "\n")

f.close()
print("Data saved")