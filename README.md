# Diagnosa Penyakit dengan Forward dan Backward Chaining

Aplikasi ini adalah alat sederhana untuk mendiagnosa penyakit berdasarkan gejala yang dimasukkan oleh pengguna. Aplikasi ini menggunakan teknik forward chaining dan backward chaining untuk menentukan kemungkinan penyakit dan mengonfirmasinya.

## Fitur

- **Forward Chaining**: Menghitung persentase kecocokan antara gejala yang dimasukkan pengguna dengan gejala yang diketahui untuk setiap penyakit.
- **Backward Chaining**: Mengonfirmasi apakah semua gejala yang diketahui untuk suatu penyakit ada dalam gejala yang dimasukkan oleh pengguna.
- **GUI Sederhana**: Antarmuka pengguna yang mudah digunakan berbasis `tkinter`.

## Persyaratan Sistem

- Python 3.x

## Cara Menggunakan

1. **Clone repository ini**:
    ```bash
    git clone https://github.com/rahmataramadhan/diagnosa-penyakit.git
    cd diagnosa-penyakit
    ```

2. **Instalasi Dependensi**:
    Tidak ada dependensi eksternal yang diperlukan selain `tkinter` yang sudah termasuk dalam distribusi standar Python.

3. **Jalankan Aplikasi**:
    ```bash
    python main.py
    ```

## Cara Kerja

1. **Forward Chaining**:
   - Menghitung persentase kecocokan antara gejala yang dimasukkan pengguna dengan gejala yang diketahui untuk setiap penyakit dalam knowledge base.
   - Contoh: Jika gejala yang diketahui untuk penyakit `Flu` adalah `{'demam', 'batuk', 'sakit tenggorokan', 'lelah'}` dan pengguna memasukkan `{'batuk', 'demam'}`, maka persentase kecocokan adalah 50% (2 dari 4 gejala cocok).

2. **Backward Chaining**:
   - Mengonfirmasi apakah semua gejala yang diketahui untuk suatu penyakit ada dalam gejala yang dimasukkan oleh pengguna.
   - Contoh: Jika persentase kecocokan untuk penyakit `Flu` adalah 100% (semua gejala cocok), maka backward chaining akan memeriksa apakah semua gejala yang diketahui untuk `Flu` ada dalam gejala yang dimasukkan oleh pengguna.

## Struktur Kode

- `main.py`: Berisi implementasi logika forward chaining dan backward chaining serta kode untuk GUI menggunakan `tkinter`.

## Contoh Penggunaan

1. Masukkan gejala yang Anda alami, dipisahkan dengan koma (misalnya: `demam, batuk, sakit tenggorokan`).
2. Klik tombol "Diagnosa".
3. Aplikasi akan menampilkan kemungkinan penyakit beserta persentase kecocokannya.
4. Jika ada penyakit dengan persentase kecocokan 100%, aplikasi akan mencoba mengonfirmasinya menggunakan backward chaining.
