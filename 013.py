# 回溯法-八皇后问题


n = 8         # 定义八个皇后
X = [0] * n   # 表示列 


# 限界函数
# 如果一个皇后能放在第k行和x(k)列,则返回true;否则返回false.
# X是全程数组,进入此过程时已置了k个值,ABS(r)过程返回r的绝对值
def PLACE(k):
    i = 0
    while i < k:
        if X[i] == X[k] or abs(X[i]-X[k]) == abs(i-k):
            return False
        i += 1

    return True


# n皇后所有解的递归算法
def NQ(k):
    X[k] = 0

    while X[k]<n:
        if PLACE(k):
            if k == n-1:
                print(X[0], X[1], X[2], X[3], X[4], X[5], X[6], X[7])
            else:
                NQ(k+1)

        X[k] = X[k] + 1


# 测试代码
if __name__ == '__main__':
    NQ(0)
