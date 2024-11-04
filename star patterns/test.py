# size=int(input("enter size: "))
# for i in range(0,size):
#     print("HI"*i,end='')
#     print("LO",end='')
# size = 5
# for i in range(size):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(size, i, -1):
#         print("*", end="")
#     print()

# size = 100
# for j in range(size,0,-1):
#     print('*'*j, end="\n")
# print()

# n = 5
# for i in range(1,n+1):
#     for j in range(i):
#         if j==0 or j==i-1:
#             print('*',end='')
#         elif i==n:
#             print('*',end='')
#         else:
#             print(" ",end='')
#     print()
# right triangle
# n=5
# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*i)

# right reverse triangle
# n=5 
# for i in range(1,n+1):
#     print(' '*(i-1)+'*'*(n-i+1))

#pyramid
# n=5
# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*(2*i-1))

# hollow pyramid
# n=5
# for i in range(0,n):
#     print(" "*(n-i),end='')
#     for j in range(0,2*i+1):
#         if j==0 or j == 2*i:
#             print('+',end='')
#         elif i==n-1:
#             print('+',end='')
#         else:
#             print(' ',end='')
#     print()

# reverse pyramid

# n=5
# for i in range(n):
#     print(" "*i,end='')
#     for j in range((n-i)*2-1,0,-1):
#         print('*',end='')
#     print()

# reverse hollow pyramid
n=5
for i in range(n):
    print(" "*i,end='')
    for j in range(0,(n-i)*2):
        if j==0 or j==((n-i)*2)-2:
            print('*',end='')
        elif i==0 and j<9:
            print('*',end='')
        else:
            print(' ',end='')
    print()

# diamond?
# n=10
# n=n/2
# n=int(n)
# for i in range(1,n+1):
#     print(' '*(n-i)+'*'*(2*i-1))

# for i in range(n):
#     print(' '*i,end='')
#     for i in range((n-i)*2-1,0,-1):
#         print('*',end='')
#     print()

# holow diamond
# n=10
# n=n/2
# n=int(n)
# for i in range(1,n+1):
#     print(' '*(n-i),end='')
#     for j in range(0,2*i-1):
#         if j==0 or j==2*i-2:  #or j==2*i-2
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()
# for i in range(0,n):
#     print(' '*i,end='')
#     for j in range(0,2*(n-i)-1,1):
#         if j==0 or j==2*(n-i)-2:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()

# hourglass
# n=30
# for i in range(n-1):
#     print(' '*i,end='')
#     for j in range(0,2*(n-i)-1):
#         print('+',end='')
#     print()
# for i in range(n):
#     print(' '*((n-i-1))+':'*(i*2+1))


# left pascal triangular
# n=9
# for i in range(n):
#     print('*'*i)
# for i in range(n,0,-1):
#     print('*'*i)

# right pascal triangle
# n=5
# for i in range(n):
#     print(' '*(n-i)+'*'*i)
# for i in range(n+1):
#     print(' '*i+'*'*(n-i))

# heart
# n=10
# q=int(n//3)
# # upper part
# for i in range(q+1):
#     print(' '*(q-i+1)+"+"*(2*(i+1)-1),end=' '*(2*(q-i)))
#     print('+'*(2*(i+1)-1))
# # lower part
# for i in range(n):
#     print(' '*i+'*'*(2*(n-i)-1))

# plus pattern 
# n=5
# m=int(5//2)+1
# for i in range(n):
#     for j in range(n):
#         if i==m-1 or j==m-1:
#             print('+',end='')
#         else:
#             print(' ',end='')
#     print()

# cross
# size = 5

# for i in range(size):
#     for j in range(size):
#         if i == j or i + j == size - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# +++++++++++++++++
#  +++++++++++++++
#   +++++++++++++
#    +++++++++++
#     +++++++++
#      +++++++
#       +++++
#        +++
#         :
#        :::
#       :::::
#      :::::::
#     :::::::::
#    :::::::::::
#   :::::::::::::
#  :::::::::::::::
# :::::::::::::::::

n=10
list=[]
for i in range(n):
    templist=[]
    for j in range(i+1):
        if j==0 or j==i:
            templist.append(1)
        else:
            templist.append(list[i-1][j-1]+list[i-1][j])
    list.append(templist)
print(list)