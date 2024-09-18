file = open("C:\\Users\\umara\\OneDrive\\Documents\\The Beauty and Importance of Nature.txt","r")
count= 0
for line in file:
    word = line.split(" ")
    count =+ len(word)
file.close()
print("no of words in a text file:",count)