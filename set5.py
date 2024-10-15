'''
5) Write a program to print the values which are similar in both given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
2 4 
Note: Trailing spaces are there at the end of the output.
'''
st1 = st2 = set()
st1 = set(map(int,input().split(" ")))
st2 = set(map(int,input().split(" ")))
res1 = st1.intersection(st2)
res2 = st1 & st2
for i in res1:
    print(i,end=" ")
print()
for j in res2:
    print(j,end=" ")
