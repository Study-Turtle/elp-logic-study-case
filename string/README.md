## 1. Let's Form a Sentence
### Problem
Pada tugas ini kamu diminta untuk melakukan penambahan string menggunakan simbol +. Disediakan variable word. Tambahkan nilai word satu per satu dengan nilai variable lain untuk membentuk sebuah kalimat. Jangan lupa menambahkan spasi di setiap kata, dan tampilkan di console hasil penggabungannya! <b>Kamu tidak perlu membuat variable baru!</b>

### Skeleton Code
```python
word = 'Python'
second = 'is'
third = 'awesome'
fourth = 'and'
fifth = 'I'
sixth = 'love'
seventh = 'it!'
```

### Output
```bash
Python is awesome and I love it!
```

## 2. Index Accessing - 1 by 1
### Problem
Pada tugas ini kamu diminta untuk "memecah" sebuah kalimat dan menampilkan setiap kata didalamnya. Untuk soal nomor ini, gunakan akses satu per satu karakter dari string untuk mengambil setiap huruf dalam kata. Terasa manual? Tidak apa-apa, kita coba ini dulu untuk saat ini.
### Hints
Saat kamu mendapatkan tiap huruf, untuk membentuk setiap kata kamu tinggal menggunakan simbol + untuk membentuk kata tersebut!
### Skeleton Code
```python
word = 'wow Python is so cool'
exampleFirstWord = word[0] + word[1] + word[2]
secondWord; # do your own!
thirdWord; # do your own!
fourthWord; # do your own!
fifthWord; # do your own!

print('First Word: ' + exampleFirstWord)
print('Second Word: ' + secondWord)
print('Third Word: ' + thirdWord)
print('Fourth Word: ' + fourthWord)
print('Fifth Word: ' + fifthWord)
```
### Output
```bash
First Word: wow
Second Word: Python
Third Word: is
Fourth Word: so
Fifth Word: cool
```

## 3. Breaking Sentence (Again) using Substring
### Problem
Mirip seperti soal nomor 2, namun kali ini gunakan substring untuk mengambil potongan dari tiap kata!
`string[start: end: step]`

Note: https://www.freecodecamp.org/news/how-to-substring-a-string-in-python/

### Skeleton Code
```python
word3 = 'wow Python is so cool'
exampleFirstWord3 = word3[0, 3]
secondWord3 # do your own!
thirdWord3 # do your own!
fourthWord3 # do your own!
fifthWord3 # do your own!

print('First Word: ' + exampleFirstWord3)
print('Second Word: ' + secondWord3)
print('Third Word: ' + thirdWord3)
print('Fourth Word: ' + fourthWord3)
print('Fifth Word: ' + fifthWord3)
```

### Output
```bash
First Word: wow
Second Word: Python
Third Word: is
Fourth Word: so
Fifth Word: cool
```

## 4. Breaking Sentence (yet Again) and Count Each Length
### Problem
Mirip seperti soal nomor 3, tapi tampilkan juga panjang kata masing-masingnya!

### Skeleton Code

Buatlah variable-variable baru untuk menyimpan panjang string, dan ubah console dibawah untuk menampilkan nya.

```python
word4 = 'wow Python is so cool'
exampleFirstWord4 = word4[0, 3]
secondWord4 # do your own!
thirdWord4 # do your own!
fourthWord4 # do your own!
fifthWord4 # do your own!

firstWordLength = len(exampleFirstWord4)
# create new variables around here

print('First Word: ' + exampleFirstWord + ', with length: ' + firstWordLength)
print('Second Word: ' + secondWord)
print('Third Word: ' + thirdWord)
print('Fourth Word: ' + fourthWord)
print('Fifth Word: ' + fifthWord)
```

### Output
```bash
First Word: wow, with length: 3
Second Word: Python, with length: 6
Third Word: is, with length: 2
Fourth Word: so, with length: 2
Fifth Word: cool, with length: 4
```