# If Else
## Objectives
* Mengerti Cara Menggunakan If-Else
* Mengerti Logika If-Else
* Mengerti Cara Menggunakan Operator Evaluasi `===`, `!==`

## Directions

Kamu diminta untuk memprogram suatu game sederhana, Proxytia namanya. Untuk memulai game itu diperlukan 2 variabel (untuk sekarang), yaitu namadan peran. Variabel peranharus memiliki isi data, bila kosong pemain akan diberikan peringatan berupa "Pilih Peranmu untuk memulai game". Terdapat 3 peranberbeda yaitu Ksatria, Tabib, dan Penyihir. Tugas Anda adalah untuk membuat program yang mengecek isi variabel peranserta mengeluarkan respon sesuai isi variabel tersebut.

### Hints
* Variabel tetap di-input secara manual.
* Variabel namadan perandapat diisi apa saja.
* Nama tidak perlu dicek sama persis seperti contoh input/output
* Buat `If-Else` berbeda masing-masing untuk mengecek `peran`
### Input
```python
# Contoh input
nama = 'Mikael'
peran = ''
# Silakan ganti nilai nama dan peran untuk mengetes kondisi!
```

### Output
```python
# Output untuk Input nama = '' dan peran = ''
"Nama harus diisi!"


# Output untuk Input nama = 'Mikael' dan peran = ''
"Halo Mikael, Pilih peranmu untuk memulai game!"

# Output untuk Input nama = 'Nina' dan peran 'Ksatria'
"Selamat datang di Dunia Proxytia, Nina"
"Halo Ksatria Nina, kamu dapat menyerang dengan senjatamu!"

# Output untuk Input nama = 'Danu' dan peran 'Tabib'
"Selamat datang di Dunia Proxytia, Danu"
"Halo Tabib Danu, kamu akan membantu temanmu yang terluka."

# Output untuk Input nama = 'Zero' dan peran 'Penyihir'
"Selamat datang di Dunia Proxytia, Zero"
"Halo Penyihir Zero, ciptakan keajaiban yang membantu kemenanganmu!"
```

# Switch Case
## Objectives
* Mengerti Cara Menggunakan `Switch-Case`
* Mengerti Logika `Switch-Case`

## Directions

Kamu akan diberikan sebuah tanggal dalam tiga variabel, yaitu hari, bulan, dan tahun. Disini kamu diminta untuk membuat format tanggal. Misal tanggal yang diberikan adalah hari 1, bulan 5, dan tahun 1945. Maka, output yang harus kamu proses adalah menjadi 1 Mei 1945.

Gunakan switch case untuk kasus ini!

Contoh:

var hari = 21; var bulan = 1; var tahun = 1945;

Maka hasil yang akan tampil di console adalah: '21 Januari 1945';

## Skeleton Code / Code yang dicontohkan yang perlu diikuti dan dimodifikasi

```python
tanggal; # assign nilai variabel tanggal disini! (dengan angka antara 1 - 31)
bulan; # assign nilai variabel bulan disini! (dengan angka antara 1 - 12)
tahun; # assign nilai variabel tahun disini! (dengan angka antara 1900 - 2200)
```