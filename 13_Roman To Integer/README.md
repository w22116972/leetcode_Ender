    # Solution

    ## Approach #1 Hash Table with 1 Scan[Accpeted]

    **Intuition**

    We can find a rule:
    - e.g. `IX=19` when we examined it from left to right, we found that if next digit is greater than current digit, we have to minus total by current digit.

    **Algorithm**

    1. according to `roman_to_int` (just google it) to build up hash table
    2. iterate through `s`
    3. we have to check index of next digit whether exceed `s` to aovid indexError
    4. we compare current digit to next digit to decide whether we need to minus `total` by current digit
    5. if current digit reaches end of `s`, we just add it to `total`

    **Python**

    ```python
    class Solution(object):
        def romanToInt(self, s):
            """
            :type s: str
            :rtype: int
            """
            roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            total = 0
            for i in range(len(s)):
                current_digit = roman_dict[s[i]]
                if i + 1 < len(s):  # index of next digit is out of `s`
                    if roman_dict[s[i+1]] > current_digit:
                        total -= current_digit
                    else:
                        total += current_digit
                else:
                    total += current_digit
            return total
    ```

    **Complexity Analysis**

    * Time complexity : $$O(len(s)) = O(n)$$.

    - `for _ in range(len(s))`: O(n)

    So time complexity is $O(n) + O(n) = O(n)$

    * Space complexity : $$O(1)$$.

    - hash table: O(1), only 7 key/value pairs in here.
    - `total`: O(1)

    So space complexity is $O(1) + O(1) = O(1)$

    ---
