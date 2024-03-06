from math import factorial

def pascal_triangle(n):
    """Return the nth row of Pascal's triangle as a list of lists."""
    if n <= 0:
        return []
    
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            # Use the formula for Pascal's triangle: n choose k = n! / (k! * (n - k)!)
            row.append(factorial(i) // (factorial(j) * factorial(i - j)))
        triangle.append(row)
    return triangle
