# 归并排序的递归算法

def Merge(r, r1, s, m, t):
    i = s
    j = m + 1
    k = s

    while i <= m and j <= t:
        if r[i] <= r[j]:
            r1[k] = r[i]
            k += 1
            i += 1
        else:
            r1[k] = r[j]
            k += 1
            j += 1

    while i <= m:        # 第一子序列收尾
        r1[k] = r[i]
        k += 1
        i += 1

    while j <= t:        # 第二子序列收尾
        r1[k] = r[j]
        k += 1
        j += 1

def MergeSort2(r, r1, s, t):
    r2 = list([0]*30)
    # print(r2, end = '')
    if s == t:
        r1[s] = r[s]
    else:
        m = (s + t) // 2
        MergeSort2(r, r2, s, m)
        MergeSort2(r, r2, m+1, t)
        Merge(r2, r1, s, m, t)

a = [9, 2, 4, 5, 1, 8, 9]
MergeSort2(a, a, 0, 6)
print(a)
