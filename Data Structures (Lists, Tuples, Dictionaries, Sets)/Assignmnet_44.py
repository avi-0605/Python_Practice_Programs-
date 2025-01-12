#Dictionary: Word Count Prompt the user for a string and build a dictionary that counts how many times each word appears.

ui=input("Enter a string: ")
words=ui.split()
wc={}
for word in words:
    if word in wc:
        wc[word] += 1
    else:
        wc[word] = 1  
print("Word Count:",wc)
