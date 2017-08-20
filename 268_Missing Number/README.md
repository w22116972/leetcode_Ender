#### Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
> https://leetcode.com/problems/missing-number/tabs/description

- For example,Given nums = [0, 1, 3], return 2.

# Sumup 

概念: 0+...+n的和減去目前的和

```python
n * (n+1) / 2 - sum(nums)
```

# Set

概念: 用集合(Set)把原本應有的0~n去除目前的集合

```python
set(range(len(nums) + 1)) - set(nums)
```

最後再把set剩下的值pop出來
