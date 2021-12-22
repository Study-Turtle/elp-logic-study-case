# Logic Challenge - Target Terdekat
## Problem
Diberikan sebuah function `targetTerdekat(lst)` yang menerima satu parameter berupa list yang terdiri dari karakter. Function akan me-return jarak spasi antar karakter 'o' dengan karakter 'x' yang terdekat. Contoh, jika list adalah ['x', ' ', 'o', ' ', ' ', 'x'], maka jarak terdekat dari 'o' ke 'x' adalah 2. Jika tidak ditemukan 'x' sama sekali, function akan me-return nilai 0.

## Code
```python
def targetTerdekat(lst) {
  # you can only write your code here!
}

# TEST CASES
print(targetTerdekat([' ', ' ', 'o', ' ', ' ', 'x', ' ', 'x'])); # 3
print(targetTerdekat(['o', ' ', ' ', ' ', 'x', 'x', 'x'])); # 4
print(targetTerdekat(['x', ' ', ' ', ' ', 'x', 'x', 'o', ' '])); # 1
print(targetTerdekat([' ', ' ', 'o', ' '])); # 0
print(targetTerdekat([' ', 'o', ' ', 'x', 'x', ' ', ' ', 'x'])); # 2