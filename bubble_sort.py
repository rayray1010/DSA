def bubble_sort(li):
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] > li[j+1]:
                temp = li[j]
                li[j] = li[j+1]
                li[j+1] = temp
    return li


print(bubble_sort([4, 2, 6, 5, 1, 3]))


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
    
 """
