''' 
Moving Zeros To The End
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

Example: move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''
def move_zeros(arr):
    new = []
    zeros = []
    for el in arr:
        if el != 0:
            new.append(el)
        else:
            zeros.append(el)
    return new + zeros
