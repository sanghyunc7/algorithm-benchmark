def quickselect(left, right, k):
    print(left, right, k)
    if k == 0 and len(left) == 1:
        return left[k]
    if k == 0 and not left and len(right) == 1:
        return right[k]
    
    next_left = []
    next_right = []
    # pick pile
    if k < len(left):
        # pick left pile
        # sort pile into two
        for i in left:
            if left[k] < i:
                next_right.append(i)
            else:
                next_left.append(i)
    else:
        k = k - len(left)
        for i in right:
                if right[k] < i:
                    next_right.append(i)
                else:
                    next_left.append(i)
    return quickselect(next_left, next_right, k)




def find_median(arr):
    if len(arr) % 2 == 1:
        return quickselect(arr, [], len(arr) // 2)
    left_median = quickselect(arr, [], len(arr) // 2)
    right_median = quickselect(arr, [], len(arr) // 2 + 1)
    return (left_median + right_median) / 2


# 1, 1, 3, 4, 5
print(find_median([4, 1, 5, 3, 1]))