# Check Vowel or Consonant
a=input("Enter string")
v=0
c=0
for i in a:
    if i in "aeiou":
        v+=1
    else:
        c=len(a)-v
print("vowel:",v)
print("Consonant:",c)
        