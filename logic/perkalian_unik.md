# Logic Challenge - Perkalian Unik

## Problem

Diberikan sebuah function `perkalianUnik(lst)` yang menerima satu parameter berupa list yang berisikan angka. Function akan me-return list baru yang mengandung angka yang setiap nilainya merupakan hasil kali angka lain yang bukan angka itu sendiri. Contoh, jika lst adalah [1, 2, 3, 4, 5], maka function akan mereturn [120, 60, 40, 30, 24], karena

- 120 adalah 2 \* 3 \* 4 \* 5,
- 60 adalah 1 \* 3 \* 4 \* 5,
- 40 adalah 1 \* 2 \* 4 \* 5,
- dan seterusnya.

## Code

```python
def perkalianUnik(lst):
  # you can only write your code here!

# TEST CASES
print(perkalianUnik([2, 4, 6])); # [24, 12, 8]
print(perkalianUnik([1, 2, 3, 4, 5])); # [120, 60, 40, 30, 24]
print(perkalianUnik([1, 4, 3, 2, 5])); # [120, 30, 40, 60, 24]
print(perkalianUnik([1, 3, 3, 1])); # [9, 3, 3, 9]
print(perkalianUnik([2, 1, 8, 10, 2])); # [160, 320, 40, 32, 160]
```
