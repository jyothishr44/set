'''
8) Write a program to update the given set in another set.
Sample Input:
1 2 3
3 4 5
Sample Output:
1 2 3 4 5
'''
st1 = st2 = set()
st1 = set(map(int,input().split(" ")))
st2 = set(map(int,input().split(" ")))
st1.update(st2)
print(*st1)
