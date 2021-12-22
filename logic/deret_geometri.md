# Logic Challenge - Tentukan Deret Geometri

## Problem

Diberikan sebuah function `tentukanDeretGeometri(lst)` yang menerima satu parameter berupa list yang terdiri dari angka. Function tersebut akan mengembalikan truejika list dari parameter tersebut merupakan deret geometri. Deret geometri adalah sebuah deret dimana perbedaan setiap angka di deret tersebut konsisten secara perkalian. Contoh, [1, 3, 9, 27, 81] adalah deret aritmatika dengan pertambahan nilai sebesar pengalian 3, dan [1, 3, 9, 27, 48] bukanlah deret aritmatika karena tidak perbedaan selisih antar angka yang tidak konsisten secara perkalian (27 \* 3 bukanlah 48!).

## Code

```python
def tentukanDeretGeometri(lst):
  # you can only write your code here!

# TEST CASES
print(tentukanDeretGeometri([1, 3, 9, 27, 81])); # True
print(tentukanDeretGeometri([2, 4, 8, 16, 32])); # True
print(tentukanDeretGeometri([2, 4, 6, 8])); # False
print(tentukanDeretGeometri([2, 6, 18, 54])); # True
print(tentukanDeretGeometri([1, 2, 3, 4, 7, 9])); # False
```
