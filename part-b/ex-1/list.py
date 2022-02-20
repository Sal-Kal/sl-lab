#Write a python program to read in a list of numbers.
#Use one-line comprehensions of create a new list of even numbers.
#Create another list reversing the elements.
S = [] # read elements  to list
n = int(input("Enter the size of the list \n"))
print("Enter the list elements")
for i in range(0,n):
    ele = int(input())
    S.append(ele)
print("The list contains the following elements")
print(S)
N = []
for i in S:
    if i not in N:
        N.append(i)
print("Unique elements are")
print(N)
M = [x for x in S if x % 2 == 0]
print("Even elements are")
print(M)
S.reverse()
print("List after reversing")
print(S)
 