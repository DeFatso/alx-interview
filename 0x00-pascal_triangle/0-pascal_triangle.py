def pascal_triangle(n):
    """
        returns a list of lists of integers representing the Pascal’s triangle
    """
    if (n <= 0):
        return []

    triangle = [[1]]

    for _ in range(1, n):
        last_row = triangle[-1]
        new_row = [1]

        for j in range(1, len(last_row)):
            new_row.append(last_row[j - 1] + last_row[j])
        new_row.append(1)
        triangle.append(new_row)

    return triangle
