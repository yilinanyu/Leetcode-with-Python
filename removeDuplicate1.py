# Given an array of integers and an integer k, find out 
#[1,2,3,4,1]
#[1,2,3,4]

def RemoveDuplicate(lst):
    seen_ints = set()
    i = 0
    while i < len(lst):
        if lst[i] in seen_ints:
            lst.pop(i)
        else:
            seen_ints.add(lst[i])
            i += 1
lst = [1,3,4,2,4]
RemoveDuplicate(lst)
print lst
