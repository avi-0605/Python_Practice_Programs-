# Tower of Hanoi Write a recursive function to solve the Tower of Hanoi puzzle for n disks.
def tower_of_hanoi(n,source,target,helper ):
    if n == 1:
        print("Move disk 1 from", source, "to", target)
        return
    tower_of_hanoi(n-1,source,helper,target)
    print("Move disk", n,"from",source,"to",target)
    tower_of_hanoi(n-1,helper, target, source)
#Test the function with user input.
n = int(input("Enter the number of disks: "))
tower_of_hanoi(n, 'A', 'C', 'B')
