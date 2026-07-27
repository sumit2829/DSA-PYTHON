# Brute Force
"""
def searchMatrix(matrix, target):
    row = len(matrix)
    col = len(matrix[0])
    
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == target:
                return True
    return False

matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]

target = 9

print(searchMatrix(matrix, target))

"""

# optimal
def searchMatrix(matrix,target):
    row = len(matrix)
    col = len(matrix[0])
    
    st = 0
    end = row*col-1
    
    while(st <= end):
        mid = st+(end-st)//2
        
        row = mid // col
        col = mid % col
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            end = mid+1
        else:
            st = mid-1
    return False

matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]

target = 9

print(searchMatrix(matrix, target))