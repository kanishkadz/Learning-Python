def lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
        
    return True

list_a = [1, 2, 3, 4]
list_b = [1, 2, 3, 4]

result = lists_equal(list_a, list_b)
print(result)
