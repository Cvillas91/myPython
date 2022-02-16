numbers =[221, 466, 353, 34, 172, 463, 129, 1, 311, 94, 330, 113, 31, 121, 457, 258, 15, 378, 242, 446, 473, 359, 396, 429, 309, 374, 371, 118, 490, 284, 315, 307, 261, 317, 82, 326, 148, 44, 426, 133, 353, 251, 146, 86, 103, 494, 481, 424, 50, 358, 459, 220, 151, 144, 33, 270, 285, 10, 490, 60, 57, 33, 492, 365, 11, 71, 459, 189, 83, 382, 142, 461, 29, 247, 403, 184, 136, 283, 281, 352, 241, 338, 150, 456, 427, 492, 22, 56, 69, 32, 322, 447, 189, 281, 345, 63, 411, 37, 499, 413]

numbers.sort() 

counter = 0
def binary_search(numbers_list, number, left, right) :
    global counter
    counter += 1
    if left > right :
        return -1

    mid = (left + right) // 2
    if number == numbers_list[mid] :
        return mid
    elif number < numbers_list[mid] :
        return binary_search(numbers_list, number, left, mid-1)
    else :
        return binary_search(numbers_list, number, mid+1, right)

print(binary_search(numbers,459, 0, len(numbers) - 1))
print(counter)
