# katla-solver

Yet another Katla solver, kali ini dengan sedikit bantuan statistik untuk memilih kata berikutnya yang paling potensial. Berdasarkan simulasi (menebak 10000 kata secara acak dari korpus), secara rata-rata program ini membutuhkan 4.7 tebakan untuk menebak kata yg benar.

## Cara memainkan

Coba kita mainkan Katla hari ke 41: https://katla.vercel.app/arsip/41

### Tebakan 1:

```
$ python main.py play

Saran kata tebakan berikutnya beserta skornya:
  kerai 17952
  kerau 17738
  etika 17683
  kaeti 17683
  .. dipotong ..
```

Sesuai saran di atas, masukkan kata **kerai** ke aplikasi Katla. Niscaya Anda akan mendapatkan hasil sbb:

⬜️🟨⬜️⬜️⬜️

Kita konversi hasil di atas dalam bentuk skor untuk masing2 posisi, dengan kriteria sbb:

- 0: karakter tidak ditemukan
- 1: karakter ditemukan di posisi lain
- 2: karakter dan posisi tepat

Jadi untuk hasil di atas, skornya adalah **01000**. Kita masukkan untuk tebakan berikutnya.

### Tebakan 2:

```
$ python main.py play kerai=01000
  1. kerai: ⬜️🟨⬜️⬜️⬜️

Saran kata tebakan berikutnya beserta skornya:
  suten 12536
  tulen 12409
  buset 11903
  pules 11856
  supel 11856
  mulet 11850
  .. dipotong ..
```

Sesuai daftar di atas, masukkan kata **suten** ke aplikasi Katla, karena kata ini skornya tertinggi. Niscaya Anda akan mendapatkan hasil sbb:

⬜️⬜️⬜️🟩⬜️

Jadi untuk hasil di atas, skornya adalah **00020**. Kita masukkan untuk tebakan berikutnya.

### Tebakan 3:

```
$ python main.py play kerai=kerai=01000 suten=00020
  1. kerai: ⬜️🟨⬜️⬜️⬜️
  2. suten: ⬜️⬜️⬜️🟩⬜️

Saran kata tebakan berikutnya beserta skornya:
  model  9875
  dobel  9801
  bogel  9672
  boleh  9615
  bopem  9567
  dogel  9433
  .. dipotong ..
```

Sesuai daftar di atas, masukkan kata **model** ke aplikasi Katla, karena kata ini skornya tertinggi dan cukup familiar. Niscaya Anda akan mendapatkan hasil sbb:

🟨🟩⬜️🟩🟩

### Tebakan 4:

```
  1. kerai: ⬜️🟨⬜️⬜️⬜️
  2. suten: ⬜️⬜️⬜️🟩⬜️
  3. model: 🟨🟩⬜️🟩🟩

Saran kata tebakan berikutnya beserta skornya:
  comel  9371
```

Cuma ada satu kemungkinan tebakan, yaitu **comel**, dan kalau dimasukkan Katla, niscaya hasilnya akan benar!
