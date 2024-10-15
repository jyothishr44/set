'''
7) Write a program to find the maximum and minimum value of given set values.
Sample Input:
1 2 3 4 5
Sample Output:
Maximum: 5
Minimum: 1
'''
st1 = set()
st1 = set(map(int,input().split(" ")))
print(f"Maximum:{max(st1)}")
print(f"Minimum:{min(st1)}")

