# Logic Challenge - Tentukan Deret Aritmatika

## Problem

Diberikan sebuah function `tentukanDeretAritmatika(lst)` yang menerima satu parameter berupa list yang terdiri dari angka. Function tersebut akan mengembalikan truejika list dari parameter tersebut merupakan deret aritmatika. Deret aritmatika adalah sebuah deret dimana perbedaan setiap angka di deret tersebut konsisten. Contoh, [2, 4, 6, 8] adalah deret aritmatika dengan pertambahan nilai sebesar 2, dan [2, 4, 6, 9] bukanlah deret aritmatika karena tidak perbedaan selisih antar angka yang tidak konsisten.

## Code

```python
def tentukanDeretAritmatika(lst):
  # you can only write your code here!

# TEST CASES
print(tentukanDeretAritmatika([1, 2, 3, 4, 5, 6])); # True
print(tentukanDeretAritmatika([2, 4, 6, 12, 24])); # False
print(tentukanDeretAritmatika([2, 4, 6, 8])); # True
print(tentukanDeretAritmatika([2, 6, 18, 54])); # False
print(tentukanDeretAritmatika([1, 2, 3, 4, 7, 9])); # False
```
