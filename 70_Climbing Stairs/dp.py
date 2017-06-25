def climbStairs_array(n):
    '''
    To reach nth steps:
        1. advance 1 step from n-1 th step
        2. advance 2 step from n-2 th step
    f(n) = f(n - 1) + f(n - 2)
    f(1) = 1
    f(2) = 2
    
    It looks like fibonacci number with base condition `n==2 ret 2`
    '''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        stair = [0] * (n + 1)
        stair[0] = 0
        stair[1] = 1
        stair[2] = 2
        for i in range(3, n + 1):
            stair[i] = stair[i - 1] + stair[i - 2]
        return stair[n]


def climbStairs_recur(n):
    '''
    Top-down approach
    Time Limit Exceeded
    '''
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return climbStairs_recur(n - 1) + climbStairs_recur(n - 2)


def climbStairs_no_space(n):
    current_step = next_step = 1
    for _ in range(n):
        current_step, next_step = next_step, current_step + next_step
        return current_step

print(climbStairs_recur(7))