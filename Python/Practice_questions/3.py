# Write a Python function Print 7 Pascal's triangle.

def is_triangle(n):
    """
    Prints the fast n rows of pascal's triangle.
    """
    
    triangle = []
    
    for i in range(n):
        row = []
        
        for j in range(i + 1):
            element = 1 if j == 0 or j == i else triangle[i -1][j]
            
            row.append(row)
            
            for row in triangle:
                print("".join(map(str,row)))
                
            is_triangle(7)
