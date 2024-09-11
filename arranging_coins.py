#you have n coins, and you want to build a staircase with these coins,the staircase consists of k rows where the ith row has exactly i coins.
# the last row of the staircase may be incomplete. Given the integer n, return the number of complete rows ont eh staircase tou will build


def arranging_coins(n):
    left, right = 0, n
    while left <= right:
        k = (left + right) // 2
        current = k * (k + 1) // 2
        if current == n:
            return k
        if n < current:
            right = k - 1
        else:
            left = k + 1
    return right

x=arranging_coins(8)
print(x)
