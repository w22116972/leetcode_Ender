class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        ud = 0
        rl = 0
        for i in moves:
            if i == 'U':
                ud += 1
            elif i == 'D':
                ud -= 1
            elif i == 'L':
                rl -= 1
            elif i == 'R':
                rl += 1
        if ud == 0 and rl == 0:
            return True
        else:
            return False