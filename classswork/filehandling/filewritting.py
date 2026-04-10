#program writting data into the file
# opening file for write operation
filev = open("firstfile.txt","w")
#writing file sentence into the file
print("Enter any file sentence : ")
for x in range(5):
    #input of data from user
    sentence = input()
    #writing sentence into the file
    filev.write(sentence)
    print("-------------------------------------------")
    #------------------------------------------------------

    print("data successfully written")
    #closing the file
    filev.close()
