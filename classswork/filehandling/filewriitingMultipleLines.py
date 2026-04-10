#program to take 20 sentences from the user and write them in new file ensuring each sentence is written in new line

sentences = []   # list to store sentences

# Taking input
for i in range(1, 21):
    sentence = input(f"Enter sentence {i}: ")
    sentences.append(sentence + "\n")   # add newline to each sentence

# Writing to file
filev = open("sentences.txt", "w")
filev.writelines(sentences)
#-----------------------------------------------------------
print("---------------------------------------------------")
print("All sentences have been written to 'sentences.txt'")
#closing file
filev.close()
