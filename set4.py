'''
4) Write a program to delete the given element in the given set values. If the given element is not in the set values, then print "Given value is not present in the set list.".
Sample Input:
1 2 3 4
2
Sample Output:
1 3 4 
Note: There is a trailing space at the end of the list.
'''
set1 = set()
set1 = set(map(int,input().split(" ")))
val = int(input())
if val in set1:
    set1.discard(val)
else:
    print("Given value is not present in the set list.")
for i in set1:
    print(i,end=' ')
