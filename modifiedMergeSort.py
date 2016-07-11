def merge_sort(l):
    if len(l) <= 1:
        return (0, l)
    else:
        mid = len(l) / 2
        count_left, ll = merge_sort(l[0:mid])
        count_right, lr = merge_sort(l[mid:])
        count_merge, merged = merge(ll, lr)
        total = count_left + count_right + count_merge
        return total, merged

def merge(left, right):
    li, ri = 0, 0
    merged = []        
    count = 0
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            merged.append(left[li])
            li += 1
        else:
            count += 1
            merged.append(right[ri])
            ri += 1

    if li < len(left):
        merged.extend(left[li:])
    elif ri < len(right):
        merged.extend(right[ri:])
    return count, merged

if __name__ == '__main__':
    # example 
    l = [6, 1 , 2, 3, 4, 5]
    print 'inverse pair count is %s'%merge_sort(l)[0]