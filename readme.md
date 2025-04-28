**LAMPIRAN PEMBAGIAN TUGAS & TEKNIK KONSTRUKSI**

**Judul Proyek**: API Quotes\
**Jumlah Anggota**: 5 orang\
**Teknik Konstruksi yang Digunakan**:

- f. API
- c. Parameterization / Generics
- e. Code reuse / Library

---

### Pembagian Tugas

| No  | Nama Anggota    | Tugas                                                                                | Teknik Konstruksi yang Digunakan |
| --- | --------------- | ------------------------------------------------------------------------------------ | -------------------------------- |
| 1   | Satria Ramadhan | Membangun server Flask, membuat endpoint `/quote` dan `/quotes`                      | f. API                           |
| 2   | Ghaza Zidane    | Mendesain dan mengisi file `quotes.json`, menyusun struktur data kutipan             | c. Parameterization / Generics   |
| 3   | Kelvin Ferdinan | Membuat fungsi `filter_by_lang()` dan logic pemrosesan parameter `?lang=`            | c. Parameterization / Generics   |
| 4   | Kevin Jonson    | Melakukan testing menggunakan Postman, validasi output, debug error                  | f. API                           |
| 5   | Gesa            | Menulis dokumentasi API (README), membuat `requirements.txt`, setup deploy ke Render | e. Code reuse / Library          |

---

### Penjelasan Teknik Konstruksi

1. **API (f)**\
   Digunakan dalam pembuatan dan pengujian endpoint `/quote` dan `/quotes` menggunakan Flask sebagai framework API.

2. **Parameterization / Generics (c)**\
   Digunakan untuk mendukung query parameter `?lang=`, yang memungkinkan client memilih bahasa quote yang diinginkan.

3. **Code reuse / Library (e)**\
   Digunakan oleh dokumentator/devops dalam mengatur dependency project, seperti `flask`, `gunicorn`, dan alat deploy ke platform cloud.
