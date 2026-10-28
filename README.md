# Program Rekap dan Analisis Nilai Matematika Kelas

## Deskripsi
Aplikasi ini dikembangkan untuk membantu pengajar/guru dalam merekapitulasi data nilai siswa, memvalidasi input agar sesuai dengan rentang nilai valid (0–100), menghitung statistik dasar kelas, serta menentukan status ketuntasan siswa berdasarkan KKM.

## Fitur
- **Validasi Data**: Menyaring nilai di luar rentang 0–100 dan mendeteksi data non-angka.
- **Analisis Statistik**: Menhitung nilai rata-rata, nilai minimum, dan nilai maksimum kelas.
- **Penentuan KKM**: Menentukan status ketuntasan siswa secara otomatis (default KKM = 75).
- **Ekspor Laporan**: Menampilkan ringkasan di terminal dan menyimpan laporan lengkap ke file teks (`output/laporan.txt`).

## Persyaratan
- Python 3.x

## Cara Menjalankan
1. Buka terminal pada direktori utama proyek.
2. Jalankan perintah berikut:
   ```bash
   python3 main.py

```

## Struktur Folder

├── README.md               # Dokumentasi utama proyek
├── .gitignore              # Daftar file/folder yang diabaikan oleh Git
├── main.py                 # File utama untuk menjalankan seluruh alur program
├── src/                    # Folder kode sumber utama (modules)
│   ├── __init__.py         # Penanda folder src sebagai paket Python
│   ├── input_data.py       # Modul pembacaan file dan validasi data (0-100)
│   ├── proses.py           # Modul kalkulasi statistik dan ketuntasan KKM
│   └── output.py           # Modul pencetakan ke terminal dan ekspor laporan
├── data/
│   └── contoh_data.txt     # File data mentah nilai siswa
├── tests/
│   └── test_case.md        # Dokumentasi pengujian (test case) dan bug log
└── docs/
    └── screenshot/         # Tangkapan layar bukti eksekusi program

```

## Test Case

| ID Test | Kategori | Input Data / Kondisi | Expected Result | Actual Result | Status |
| --- | --- | --- | --- | --- | --- |
| TC01 | Normal | Nilai `85, 78, 92` | Rata-rata 85.0, Min 78, Max 92 | Rata-rata 85.0, Min 78.0, Max 92.0 | **PASS** |
| TC02 | Batas | Nilai `0` dan `100` | Diterima sebagai nilai valid | Diterima sebagai nilai valid | **PASS** |
| TC03 | Invalid | Nilai `105` dan `-5` | Dipisahkan ke data invalid | Dipisahkan ke data invalid | **PASS** |
| TC04 | Non-Angka | String `"abc"` | Dipisahkan ke data invalid | Dipisahkan ke data invalid | **PASS** |
| TC05 | File Error | Path file tidak ditemukan | Tampil pesan error tanpa crash | Tampil pesan error tanpa crash | **PASS** |

## Known Issues

* Nilai batas KKM saat ini dikunci (*hardcode*) pada angka 75 di dalam modul `src/proses.py`.

## Anggota dan Kontribusi

* **Nama:** Eka Elsanti
* **NIM:** 2225250059
* **Kontribusi:** Pembuatan modul `input_data.py`, `proses.py`, `output.py`, alur utama `main.py`, pengujian *test case*, serta penyusunan seluruh dokumentasi proyek.

## Referensi/Bantuan

* Bahan Ajar & Modul Panduan Pertemuan 15
* Dokumentasi Resmi Python 3 (`docs.python.org`).
* Asisten AI (Gemini) untuk konsultasi struktur modular dan penataan dokumentasi Markdown.