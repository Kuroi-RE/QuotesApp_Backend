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
| 5   | Aulia Ahmad     | Menulis dokumentasi API (README), membuat `requirements.txt`, setup deploy ke Render | e. Code reuse / Library          |

---

### Penjelasan Teknik Konstruksi

1. **API (f)**\
   Digunakan dalam pembuatan dan pengujian endpoint `/quote` dan `/quotes` menggunakan Flask sebagai framework API.

2. **Parameterization / Generics (c)**\
   Digunakan untuk mendukung query parameter `?lang=`, yang memungkinkan client memilih bahasa quote yang diinginkan.

3. **Code reuse / Library (e)**\
   Digunakan oleh dokumentator/devops dalam mengatur dependency project, seperti `flask`, `gunicorn`, dan alat deploy ke platform cloud.

<br>

---

<!-- Gesa -->
# QuotesApp Backend Documentation

Backend sederhana menggunakan Flask yang menyediakan API Quotes muti-bahasa (Indonesia, Jawa, Sunda) dari berbagai tokoh dari kelas 07-01.

## Fitur

- Mendapatkan quotes secara generate (acak).
- Mendapatkan Quotes berdasarkan bahasa Indonesia, Jawa, Sunda.
- Dukungan CORS untuk frontend lintas domain.

---

## Menjalankan Program

### 1. Buat Virtual Environment

```bash
python -m venv venv
```

### 2. Aktifkan Virtual Environment

#### Git Bash
```bash
source venv/Scripts/activate
```

#### Command Prompt
```cmd
venv\Scripts\activate
```

### 3. Install Dependencies

#### requirements.txt

```txt
Flask==2.3.2
flask-cors==3.0.10
```
#### Git Bash

```bash
pip install -r requirements.txt
```

### 4. Jalankan Server

```bash
flask run
```

---
<!-- Gesa -->
# QuotesApp API Documentation
ini Adalah Dokumentasi API QuotesApp API yang digunakan untuk mendapatkan Quotes Dari Beberapa Tokoh Kelas SE-07-01. <a href="https://documenter.getpostman.com/view/44345250/2sB2j4eVpk">**QuotesApp API Documentation -Postman-**</a>

#

**Endpoint Secara Default:**  
```json
{
  "message": "Endpoints: /quote"
}
```

---

### `GET` Generated Quotes

````txt
http://127.0.0.1:5000/quote
````

**Deskripsi:**  
Mengambil satu kutipan secara acak, ini adalah Method GET untuk generated API secara random melalui endpoint '/quote', untuk saat ini program dijalankan di localhost.

**Output:**

```json
{
  "person": "Gesa",
  "quote": "Udah berjuang, udah bertahan, tapi tetap bukan jadi pilihan.",
  "lang": "id"
}
```
---

### `GET` Generated Quotes With Bahasa Indonesia

````txt
http://127.0.0.1:5000/quote?lang=id
````

**Deskripsi:**  
Generate Quotes hanya menggunakan bahasa indonesia dengan endpoint '/quote?lang=id', berdasarkan parameter: 'lang' value: 'id' dengan ini API mengembalikan quotes dalam bahasa indonesia.

**Query Params**
| Parameter | Value  |
| --- | --------------- |
| lang  | id |

**Output:**

```json
{
  "person": "Fajar Budiawan",
  "quote": "Masa lalu adalah pelajaran, bukan tempat untuk menetap",
  "lang": "id"
}
```
---

### `GET` Generated Quotes With Bahasa Jawa

````txt
http://127.0.0.1:5000/quote?lang=javanese
````

**Deskripsi:**  
Generate Quotes hanya menggunakan bahasa jawa dengan endpoint '/quote?lang=javanese', berdasarkan parameter: 'lang' value: 'javanese' dengan ini API mengembalikan quotes dalam bahasa Jawa.

**Query Params**
| Parameter | Value  |
| --- | --------------- |
| lang  | javanese |

**Output:**

```json
{
  "person": "Satria Ramadhan",
  "quote": "Ora Madang Ora Hidup",
  "lang": "javanese"
}
```
---

### `GET` Generated Quotes With Bahasa Sunda

````txt
http://127.0.0.1:5000/quote?lang=Sundanese
````

**Deskripsi:**  
Generate Quotes hanya menggunakan bahasa jawa dengan endpoint '/quote?lang=Sundanese', berdasarkan parameter: 'lang' value: 'Sundanese' dengan ini API mengembalikan quotes dalam bahasa Sunda.

**Query Params**
| Parameter | Value  |
| --- | --------------- |
| lang  | Sundanese |

**Output:**

```json
{
  "person": "Ghaza Zidane Nuraihan",
  "quote": "Awewe mah loba, lamun nu setia teh jarang euy",
  "lang": "Sundanese"
}
```
---

## Program Dibuat oleh

### Kelompok TUBES KPL  
Anggota: Satria Ramadhan, Kelvin Ferdinand, Kevin Jonson, Ghaza Zidane Nurraihan, Aulia Ahmad Ghaus Adzam.

