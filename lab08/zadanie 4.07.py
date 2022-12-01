"""
By Michał Matuszyk
on 01/12/2022
"""

def outer_product(x, y):
    result = [[0 for d in range(len(x))] for i in range(len(y))]
    for i in range(len(y)):
        for d in range(len(x)):
            result[i][d] = x[d] * y[i]
    return result



a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]

print(outer_product(a, b))