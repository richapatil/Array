# T = [[1,2,3], [4,5,6], [7,8,9]]
# len(T) = 3
#len(T[0]) = 3 i.e 1,2,3

def spiralOrder(self, A):
    q = []  #list to store answer
    row = 0  #Top
    col = 0 #left
    n = len(A) - 1  #bottom #"2"
    m = len(A[0] - 1)  #right  #A[0] as each time one list  #"2"
    dir = 0 #direction initialize to 0
    # if dir = 0 go right
    # if dir = 1 go down
    # if dir = 2 go left
    # if dir = 3 go up

    while(row <= n and col <=m):
        if (dir == 0):
            for i in range (col,m+1):  # we need to move from left to right
                q.append(A[row][i])   #print first row
            row+=1
        elif (dir == 1):
            for i in range (row,n+1):  #we moved down side
                q.append(a[i][m])      #print the down value
            m-=1
        elif (dir == 2):
            for i in range (m,col-1,-1): #we moved from right to left
                q.append(A[n][i])        #print down row
            n-=1
        elif (dir == 3):
            for i in range (n,row-1,-1):   #we moved from bottom yo up
                q.append(A[i][col])
            col+=1
        dir = (dir + 1)%4   #dir will be added up after every iteration
    return q
