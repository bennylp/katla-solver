# katla-solver

Yet another Katla solver, kali ini dengan sedikit bantuan statistik untuk memilih kata berikutnya yang paling potensial. Berdasarkan simulasi (menebak seluruh 8311 kata di korpus), secara rata-rata program ini membutuhkan 4.5 tebakan untuk menebak kata yg benar, dengan tingkat kegagalan 6.6% (gagal menebak dalam 6 langkah).

## Cara memainkan

Coba kita mainkan Katla hari ke 41: https://katla.vercel.app/arsip/41

### Tebakan 1:

```
$ python main.py play

Saran kata tebakan berikutnya beserta valuenya:
  kerai 17952
  kerau 17738
  etika 17683
  kaeti 17683
  .. dipotong ..
```

Sesuai saran di atas, masukkan kata **kerai** ke aplikasi Katla. Niscaya Anda akan mendapatkan hasil sbb:

⬜️🟨⬜️⬜️⬜️

Kita konversi hasil di atas dalam bentuk skor untuk masing2 posisi karakter (ada 5 posisi), dengan kriteria sbb:

- 0: bila karakter tidak ditemukan
- 1: bila karakter ditemukan di posisi lain
- 2: bila karakter dan posisi tepat

Jadi untuk hasil di atas, skornya adalah:

- ⬜️ 🟨 ⬜️ ⬜️ ⬜️ => 0 1 0 0 0

Kita masukkan kata dan skornya untuk tebakan berikutnya.

### Tebakan 2:

```
$ python main.py play kerai=01000
  1. kerai: ⬜️🟨⬜️⬜️⬜️

Saran kata tebakan berikutnya beserta valuenya:
  lotus 11313
  tonus 11297
  pluto 10639
  muton 10595
  solum 10589
  .. dipotong ..
```

Sesuai daftar di atas, masukkan kata **lotus** ke aplikasi Katla, karena kata ini valuenya tertinggi. Niscaya Anda akan mendapatkan hasil sbb:

🟨🟩⬜️⬜️⬜️

Jadi untuk hasil di atas, skornya adalah 🟨 🟩 ⬜️ ⬜️ ⬜️ ==> **1 2 0 0 0**. Kita masukkan untuk tebakan berikutnya.

### Tebakan 3:

```
$ python main.py play kerai=01000 lotus=12000
  1. kerai: ⬜️🟨⬜️⬜️⬜️
  2. lotus: 🟨🟩⬜️⬜️⬜️

Saran kata tebakan berikutnya beserta valuenya:
  polen 10775
  molen 10747
  monel 10747
  model  9875
  dobel  9801
  .. dipotong ..
```

Sesuai daftar di atas, kali ini kita masukkan kata **molen** ke aplikasi Katla, karena kata ini lebih familiar dibanding **polen** dan valuenya tidak jauh berbeda. Niscaya Anda akan mendapatkan hasil sbb:

🟨🟩🟨🟩⬜️ => 1 2 1 2 0

### Tebakan 4:

```
$ python main.py play kerai=01000 lotus=12000 molen=12120
  1. kerai: ⬜️🟨⬜️⬜️⬜️
  2. lotus: 🟨🟩⬜️⬜️⬜️
  3. molen: 🟨🟩🟨🟩⬜️

Saran kata tebakan berikutnya beserta valuenya:
  comel  9371
```

Kita beruntung, kali ini cuma ada satu kemungkinan tebakan, yaitu **comel**, dan kalau dimasukkan Katla, niscaya hasilnya akan benar!

🟩🟩🟩🟩🟩

## Simulasi menebak 1 kata

```
$ python main.py guess kedai
Secret word: kedai
  1. kerai [chance:    ]: 🟩🟩⬜️🟩🟩
  2. ketai [chance: 14%]: 🟩🟩⬜️🟩🟩
  3. kelai [chance: 17%]: 🟩🟩⬜️🟩🟩
  4. kepai [chance: 20%]: 🟩🟩⬜️🟩🟩
  5. kebai [chance: 25%]: 🟩🟩⬜️🟩🟩
  6. kedai [chance: 33%]: 🟩🟩🟩🟩🟩
```
```
$ python main.py guess tupai
Secret word: tupai
  1. kerai [chance:    ]: ⬜️⬜️⬜️🟩🟩
  2. lotus [chance:    ]: ⬜️⬜️🟨🟨⬜️
  3. tunai [chance: 50%]: 🟩🟩⬜️🟩🟩
  4. tupai [chance:100%]: 🟩🟩🟩🟩🟩

```

## Simulasi menebak bbr kata secara random

Bisa melakukan simulasi untuk melihat langkah-langkah:

```
$ python main.py sim -c 5
Guessing 5 random words
Secret word: geret
  1. kerai [chance:    ]: ⬜️🟩🟩⬜️⬜️
  2. lotus [chance:    ]: ⬜️⬜️🟨⬜️⬜️
  3. terem [chance: 14%]: 🟨🟩🟩🟩⬜️
  4. beret [chance: 25%]: ⬜️🟩🟩🟩🟩
  5. deret [chance: 33%]: ⬜️🟩🟩🟩🟩
  6. geret [chance: 50%]: 🟩🟩🟩🟩🟩
Secret word: teguk
  1. kerai [chance:    ]: 🟨🟩⬜️⬜️⬜️
  2. lotus [chance:    ]: ⬜️⬜️🟨🟩⬜️
  3. tekun [chance: 11%]: 🟩🟩🟨🟩⬜️
  4. tepuk [chance: 33%]: 🟩🟩⬜️🟩🟩
  5. tebuk [chance: 50%]: 🟩🟩⬜️🟩🟩
  6. teguk [chance:100%]: 🟩🟩🟩🟩🟩
Secret word: tarak
  1. kerai [chance:    ]: 🟨⬜️🟩🟩⬜️
  2. lotus [chance:    ]: ⬜️⬜️🟨⬜️⬜️
  3. tarak [chance:100%]: 🟩🟩🟩🟩🟩
Secret word: injil
  1. kerai [chance:    ]: ⬜️⬜️⬜️⬜️🟨
  2. lotus [chance:    ]: 🟨⬜️⬜️⬜️⬜️
  3. cling [chance:  8%]: ⬜️🟨🟨🟨⬜️
  4. pilin [chance: 25%]: ⬜️🟨🟨🟩🟨
  5. injil [chance:100%]: 🟩🟩🟩🟩🟩
Secret word: ronce
  1. kerai [chance:    ]: ⬜️🟨🟨⬜️⬜️
  2. lotus [chance:    ]: ⬜️🟩⬜️⬜️⬜️
  3. nomer [chance:  8%]: 🟨🟩⬜️🟨🟨
  4. ronde [chance: 50%]: 🟩🟩🟩⬜️🟩
  5. ronce [chance:100%]: 🟩🟩🟩🟩🟩
Average: 5.0 tebakan
Failed : 0 (0.0%)
```


## Benchmarking

Menebak seluruh kata dalam korpus:

```
$ time python main.py sim -c 8311 --verbosity=0
Guessing all 8311 words
Average: 4.5 tebakan
Failed : 661 (6.6%)

real	5m14.354s
user	5m14.308s
sys	0m0.016s
```

