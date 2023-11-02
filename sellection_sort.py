def selection_sort(li):
    for i in range(len(li) - 1):
        min_index = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_index]:
                min_index = j
        if min_index != i:
            temp = li[i]
            li[i] = li[min_index]
            li[min_index] = temp
    return li


print(selection_sort([4, 2, 6, 5, 1, 3]))


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """
