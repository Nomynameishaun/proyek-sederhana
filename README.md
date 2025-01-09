# Pengelolaan Data Mahasiswa
Program ini adalah aplikasi sederhana berbasis Python untuk mengelola data mahasiswa menggunakan konsep Object-Oriented Programming (OOP) dan modular programming.

## Fitur Program
1. Menambah data mahasiswa (Nama, NIM, dan Nilai).
2. Menampilkan data mahasiswa dalam bentuk tabel.
3. Validasi input dengan penanganan kesalahan.
4. Struktur kode terpisah ke dalam beberapa file:
   * data.py: Mengelola penyimpanan data.
   * view.py: Menangani input dan output.
   * process.py: Mengelola proses utama program.
   * main.py: Menjalankan program.

## Cara Menggunakan Program
1. Clone repository ini ke komputer Anda.
2. Pastikan Python 3 telah terinstal di sistem Anda.
3. Jalankan file main.py menggunakan perintah:
``` ruby
python main.py
```
4. Ikuti petunjuk pada menu untuk menambah atau melihat data mahasiswa.

## Struktur Program
``` ruby
|-- data.py       # Mengelola data mahasiswa
|-- view.py       # Interaksi pengguna
|-- process.py    # Logika proses utama
|-- main.py       # Entry point program
```

## Contoh Ouput Program
### Menu Utama
``` ruby
1. Tambah Data Mahasiswa
2. Tampilkan Data Mahasiswa
3. Keluar
```
### Tampilkan Tabel
``` ruby
Daftar Nilai Mahasiswa:
========================================
Nama            NIM        Nilai
----------------------------------------
John Doe        123456     85.0
Jane Smith      654321     90.0
========================================
```

## Flowchart Program

![1](<Gambar/flowchart_program.png>)
### Langkah-Langkah Flowchart
1. Mulai program.
2. Tampilkan menu utama:
   * Tambah Data Mahasiswa.
   * Tampilkan Data Mahasiswa.
   * Keluar.
3. Pengguna memilih salah satu menu.
4. Jika memilih "Tambah Data Mahasiswa":
   * Meminta input data (Nama, NIM, Nilai).
   * Validasi input data.
   * Simpan data ke dalam penyimpanan.
5. Jika memilih "Tampilkan Data Mahasiswa":
   * Ambil data dari penyimpanan.
   * Tampilkan data dalam bentuk tabel.
6. Jika memilih "Keluar":
   * Program berhenti.
7. Ulangi hingga pengguna memilih "Keluar".
