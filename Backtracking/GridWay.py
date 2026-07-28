def gridway(i,j,n,m):
    if(i==n-1 and j==m-1):
        return 1
    if(i==n or j==m):
        return 0
    return gridway(i+1,j,n,m)+gridway(i,j+1,n,m)
n=4
m=4
print(gridway(0,0,n,m))