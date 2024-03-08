"""
pascal triangle function
"""
def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # first element of each row is always 1
        if i > 0:
            prev_row = triangle[-1]
            for j in range(1, i):
                row.append(prev_row[j - 1] + prev_row[j])
            row.append(1)  # last element of each row is always 1
        triangle.append(row)

    return triangle
