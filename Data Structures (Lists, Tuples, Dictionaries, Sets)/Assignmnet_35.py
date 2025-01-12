# Count positive, negative, and zero 

numbers=input("Enter numbers: ").split()
numbers=[int(n) for n in numbers]
p_count=0
n_count=0
z_count=0
for n in numbers:
    if n > 0:
        p_count+=1
    elif n < 0:
        n_count+=1
    else:
        z_count+=1

print("Positive:",p_count)
print("Negative:",n_count)
print("Zero:",z_count)
