N = 4                   # 4物品
P = [0, 10, 10, 12, 18]  # 效益
W = [0,  2,  4,  6,  9]  # 重量
M = 15                  # 可放入背包的重量

# 父结点;        结点所在的层;   最优解的值;   背包剩余质量;已获得的效益;可能的最大效益
PARENT = dict(); LEVEL = dict(); TAG = dict(); CU = dict(); PE = dict(); UB = dict()

LBB = UBB = 0      # LBB代表下界;UBB代表上界
Lnode = []         # 活结点列表


# 计算下界和上界的算法
def LUBOUND(P, W, rw, cp, N, k):
    # rw是背包的剩余容量;cp为已获得的效益;还有物品k,...,N要考虑;
    global LBB, UBB
    LBB = cp; c = rw
    for i in range(k, N+1):
        if c < W[i]:
            UBB = LBB + c * P[i]/W[i]   # 可能的最大效益
            for j in range(i+1, N+1):   # 可能最大的实际效益
                if c >= W[j]:
                    c = c - W[j]
                    LBB = LBB + P[j]
            return 

        c = c - W[i]; LBB = LBB + P[i]

    UBB = LBB                           # 全部装满背包,实际效益就是最大效益


# 生成一个新结点
def NEWNODE(par, lev, t, cap, prof, ub, I):
    PARENT[I] = par; LEVEL[I] = lev; TAG[I] = t   # 父结点;结点所在的层;最优解序列
    CU[I] = cap; PE[I] = prof; UB[I] = ub         # 背包的剩余的重量;已获得的效益值;可能的最大效益
    Lnode.append((I, UB[I]))                      # 加入活结点


# 打印答案
def FINISH(L, ANS, N):
    print('Value of optimal filling is:', L)    # 最佳效益的值
    print('Objects in knapsack are:')           # 背包的结果为
    for j in range(N, 0, -1):
        if TAG[ANS] == 1:
            print(j)
        ANS = PARENT[ANS]


# UB值最大的结点
def LARGEST():
    E = max(Lnode, key= lambda x: x[1])         # 取活结点表中的最佳效益的最大值
    Lnode.remove(E)                             # 取出活结点表
    return E[0]


# LC分枝-限界算法
def LCKNAP(P, W, M, N, e=0.0001):

    L=cap=prof=0                                 # 真实效益值;剩余背包重量;可能的最佳效益
    ANS = 0
    E = 1                                        # 根结点
    count = 1                                    # 结点计数器

    PARENT[E]=0; LEVEL[E]=1; CU[E]=M; PE[E]=0    # 根结点无父亲; 所处层为1层; 背包剩余质量为M; 已获得的效益为0
    LUBOUND(P, W, M, 0, N, 1)                    # 此结点的下界和上界

    L = LBB-e; UB[E] = UBB

    while True:
        i = LEVEL[E]; cap = CU[E]; prof = PE[E]

        if i == N+1:             # 解结点
            if prof > L:
                L = prof; ANS = E
        else:                    # E有两个儿子
            if cap >= W[i]:      # 左儿子可行
                NEWNODE(E, i+1, 1, cap-W[i], prof+P[i], UB[E], count+1)
                count += 1

            # 看右儿子是否会活
            LUBOUND(P, W, cap, prof, N, i+1)

            if UBB > L:           # 右儿子会活
                NEWNODE(E, i+1, 0, cap, prof, UBB, count+1)
                count += 1
                L = max(L, LBB-e)
    
        # 不再有活结点则退出
        if Lnode == []:
            break

        # 下一个E-结点是UB值最大的结点
        E = LARGEST()

        if UB[E] <= L:
            break

    FINISH(L, ANS, N)             # 打印答案


if __name__ == '__main__':
    LCKNAP(P, W, M, N)
