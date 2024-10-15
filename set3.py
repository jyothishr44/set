'''
3) Write a program to print only the different values between two given sets.
Sample Input:
1 2 3 4
2 4 6 8
Sample Output:
1 3
'''
st1 = st2 = set()
st1 = set(map(int,input().split(" ")))
st2 = set(map(int,input().split(" ")))
res = st1.difference(st2)
for i in res:
    print(i,end=" ")
