'''
1) Write a program to get n number of values in separate line for set and print the values with space separation.
Sample Input:
5
3
1
4
5
2
Sample Output:
1 2 3 4 5 
'''
n = int(input())
st = set()
for i in range(n):
    val = int(input())
    st.add(val)
for i in st:
    print(i,end=" ")
