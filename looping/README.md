## 1. Melakukan Looping Menggunakan ``While``
### Problem
Pada tugas ini kamu diminta untuk melakukan looping dalam Python dengan menggunakan syntax while. Untuk membuat tantangan ini lebih menarik, kamu juga diminta untuk membuat suatu looping yang menghitung maju dan menghitung mundur. Jangan lupa tampilkan di console juga judul 'LOOPING PERTAMA' dan 'LOOPING KEDUA'.

### Output
```bash
LOOPING PERTAMA
2 - I love coding
4 - I love coding
6 - I love coding
8 - I love coding
10 - I love coding
12 - I love coding
14 - I love coding
16 - I love coding
18 - I love coding
20 - I love coding
LOOPING KEDUA
20 - I will become fullstack developer
18 - I will become fullstack developer
16 - I will become fullstack developer
14 - I will become fullstack developer
12 - I will become fullstack developer
10 - I will become fullstack developer
8 - I will become fullstack developer
6 - I will become fullstack developer
4 - I will become fullstack developer
2 - I will become fullstack developer
```

## 2. Melakukan <i>Looping</i> Menggunakan ``For``
### Problem
Pada tugas ini kamu diminta untuk melakukan looping dalam Python dengan menggunakan syntax ``for``. Untuk membuat tantangan ini lebih menarik, kamu juga diminta untuk membuat suatu looping yang menghitung maju dan menghitung mundur. Jangan lupa tampilkan di console juga judul 'LOOPING PERTAMA' dan 'LOOPING KEDUA'.

### Hints
Operator ``++`` disebut dengan operator <i>Increment</i> Operator ``--`` disebut dengan operator <i>Decrement</i>

### Output
```bash
LOOPING PERTAMA
1 - I love coding
2 - I love coding
3 - I love coding
4 - I love coding
5 - I love coding
6 - I love coding
7 - I love coding
8 - I love coding
9 - I love coding
10 - I love coding
11 - I love coding
12 - I love coding
13 - I love coding
14 - I love coding
15 - I love coding
16 - I love coding
17 - I love coding
18 - I love coding
19 - I love coding
20 - I love coding
LOOPING KEDUA
20 - I will become fullstack developer
19 - I will become fullstack developer
18 - I will become fullstack developer
17 - I will become fullstack developer
16 - I will become fullstack developer
15 - I will become fullstack developer
14 - I will become fullstack developer
13 - I will become fullstack developer
12 - I will become fullstack developer
11 - I will become fullstack developer
10 - I will become fullstack developer
9 - I will become fullstack developer
8 - I will become fullstack developer
7 - I will become fullstack developer
6 - I will become fullstack developer
5 - I will become fullstack developer
4 - I will become fullstack developer
3 - I will become fullstack developer
2 - I will become fullstack developer
1 - I will become fullstack developer
```

## 3. Angka Ganjil dan Genap
Hint: kamu akan menggunakan kondisional juga di kasus ini.

### Problem
1. Buatlah sebuah perulangan 1 - 100 dengan pertambahan counter sebanyak 1
2. Di dalam perulangan, periksa setiap angka <i>counter</i>:
- Apabila angka counter adalah angka genap, tuliskan <b>GENAP</b>
- Apabila angka counter adalah angka ganjil, tuliskan <b>GANJIL</b>
3. Buatlah 3 perulangan baru dari 1 - 100, dengan pertambahan <i>counter</i> sebesar 2, 5, dan 9.
4. Pada 3 perulangan baru ini periksa setiap angka <i>counter</i>:
- Apabila bukan kelipatan yang ditentukan tidak perlu menuliskan apa-apa
- Apabila angka <i>counter</i> adalah kelipatan 3 dengan pertambahan 2, kelipatan 6 dengan pertambahan 5, dan kelipatan 10 dengan pertambahan 9, tuliskan:
`"3 kelipatan 3"` dan seterusnya.
### output
```bash
# contoh - ganjil genap
# counter sekarang = 1,
# output
"GANJIL"
# counter sekarang = 2,
# output
"GENAP"
#  dan seterusnya :)

# contoh - untuk pertambahan counter 2
# counter sekarang = 1,
# output
""
# counter sekarang = 3,
# output
"3 KELIPATAN 3"
#  dan seterusnya :)

# contoh - untuk pertambahan counter 5
# counter sekarang = 1,
# output
""
# counter sekarang = 6,
# output
"6 KELIPATAN 6"
#  dan seterusnya :)

# contoh - untuk pertambahan counter 9
# counter sekarang = 1,
# output
""
# counter sekarang = 10,
# output
"10 KELIPATAN 10"
#  dan seterusnya :)
```

## 4. Menyusun Barisan Bintang
### Problem
Pada tugas ini kamu diminta untuk melakukan looping dalam Python untuk menampilkan di console barisan asterisks (bintang). Setiap baris memiliki 1 simbol '*'.

### Skeleton Code
```python
rows1 # input the number of rows

# do loops to display asterisks in the console.
```
### Output
jika rows1 = 5
```bash
*
*
*
*
*
```
## 5. Menyusun Barisan Bintang Dengan Nested Looping
### Problem
Pada tugas ini kamu diminta untuk melakukan looping dalam Python untuk menampilkan di console barisan asterisks (bintang). Setiap baris memiliki jumlah simbol '*' sesuai dengan jumlah baris. Manfaatkan nested loop atau loop di dalam loop untuk menyelesaikan kasus ini.

### Skeleton Code
```python
rows2 # input the number of rows

# do loops to display asterisks in the console.
```
### Output
jika rows2 = 5
```bash
*****
*****
*****
*****
*****
```
### 6. Menyusun Barisan Tangga Bintang Dengan Nested Looping
### Problem
Pada tugas ini kamu diminta untuk melakukan looping dalam Python untuk menampilkan di console barisan asterisks (bintang) dalam bentuk tangga. Setiap baris memiliki jumlah simbol '*' sesuai dengan nomor baris. Baris pertama, hanya ada satu bintang. Baris kedua, dua bintang, baris ketiga tiga bintang, dan seterusnya. Manfaatkan nested loop atau loop di dalam loop untuk menyelesaikan kasus ini.

### Skeleton Code
```python
rows3 # input the number of rows

# do loops to display asterisks in the console.
```
## Output
jika rows3 = 5
```bash
*
**
***
****
*****
```