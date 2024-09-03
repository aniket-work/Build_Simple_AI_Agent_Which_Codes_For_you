def print_triangle(n):
    """
    Prints an ASCII triangle with n rows.

    :param n: Number of rows in the triangle
    :type n: int
    """
    for i in range(n):
        # Print leading spaces to center the triangle
        print(' ' * (n - i - 1), end='')

        # Print asterisks for each row
        print('* ' * (i + 1))

# Example usage:
print_triangle(5)