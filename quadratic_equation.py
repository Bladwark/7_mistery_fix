from math import sqrt


def get_roots(a, b, c):

    discriminant = b ** 2 - 4 * a * c

    #here was a problem
    if discriminant > 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return root1, root2

    elif discriminant == 0:
        root1 = (-b ) / (2 * a)

        return root1, None

    else:
        return None, None
