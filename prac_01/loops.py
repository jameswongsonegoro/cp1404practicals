"""a. count in 10s from 0 to 100"""

for i in range(0, 101, 10):
    print(i, end=" ")
print()

"""b. count down from 20 to 1"""
for j in range(20, 0, -1):
    print(j, end=" ")
print()

"""c. print n stars"""
star = int(input("Number of stars: "))
for m in range(star):
    print("*", end="")
print()

"""d. print n lines of increasing stars"""
star = int(input("Number of stars: "))
k = 1
for n in range(0, star):
    for o in range(0, k):
        print("*", end="")
    k = k + 1
    print()




