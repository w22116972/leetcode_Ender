# Write a function that takes a string as input and returns the string reversed.
> https://leetcode.com/problems/reverse-string/tabs/description

Given s = "hello", return "olleh"

# Slicing

```python
s[::-1]
```

# recursion

把字串的後半跟前半串接在一起

```python
return s[len/2:] + s[:len/2]
```

## 範例

#### s = abcde
1. cde + ab
2. de + c + b + a
3. e + d + c + b + a

# swap

轉成list後，對index做i, j逼近，對value做交換

```python
while i < j:
    lst[i], lst[j] = lst[j], lst[i]
    i += 1
    j -= 1
```