def reg_match(s, p):
    '''
    1, If p.charAt(j) == s.charAt(i) :  dp[i][j] = dp[i-1][j-1];
    2, If p.charAt(j) == '.' : dp[i][j] = dp[i-1][j-1];
    3, If p.charAt(j) == '*': 
    here are two sub conditions:
        1   if p.charAt(j-1) != s.charAt(i) : dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
        2   if p.charAt(i-1) == s.charAt(i) or p.charAt(i-1) == '.':
            dp[i][j] = dp[i-1][j]    //in this case, a* counts as multiple a 
            or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
            or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty
    '''
    reg = ['*', '.']
    i = 0
    while i <= len(s):
        # case 0: p[i] is '*' or '.' and p[i + 1] == '*' or '.'
        if p[i] == '.' and p[i + 1] == '*':
            # reg_match(s[1:], p[1:]) # case when * == zero 
            i ++
            p[i] = s[i]
            reg_match(s[1:], p[i])
        # case 1: pattern is '*' or '.' and p[i + 1] != '*' or '.'
        elif p[i] == '.' and p[i + 1] != '*':
            p[i] = s[i]
            reg_match(s[1:], p[i])
        # case 2: s[i] match p[i] and p[i + 1] == '*' or '.'
        elif s[i] == p[i] and p[i + 1] == '*':
            reg_match(s[1:], p[1:]) # case when * == zero 
            p[i] = s[i]
            reg_match(s[1:], p[i])
        elif s[i] == p[i] and p[i + 1] != '*':
            reg_match(s[1:], p[1:])
        # case 4: s[i] doesn't match p[i]
        elif s[i] != p[i]:
            return False
        
        
