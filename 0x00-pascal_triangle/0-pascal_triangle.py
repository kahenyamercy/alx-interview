def pascal_triangle(n):
    """Return a list of lists representing Pascal's triangle up to the nth row."""
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            # Each element (except the first and last) is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        if i > 0:
            row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle