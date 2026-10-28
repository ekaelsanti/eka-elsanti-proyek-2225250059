# Dokumentasi Pengujian (Test Case) & Bug Log

## 1. Tabel Hasil Pengujian (Test Case)

| ID Test | Kategori | Input Data / Kondisi | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| TC01 | Normal | Baris data: `Ayu,85`, `Budi,78`, `Citra,92` | Rata-rata 85.0, Min 78, Max 92 | Rata-rata 85.0, Min 78.0, Max 92.0 | **PASS** |
| TC02 | Batas (Boundary) | Baris data: `SiswaA,0`, `SiswaB,100` | Diterima sebagai nilai valid | Diterima sebagai nilai valid | **PASS** |
| TC03 | Invalid (Rentang) | Baris data: `Eka,105`, `Fajar,-5` | Dipisahkan ke data invalid | Dipisahkan ke data invalid dengan alasan "Di luar rentang 0-100" | **PASS** |
| TC04 | Invalid (Format) | Baris data: `Budi,abc` | Ditolak dengan penanganan format | Dipisahkan ke data invalid dengan alasan "Format nilai bukan angka" | **PASS** |
| TC05 | Error (File) | Membaca path file `data/tidak_ada.txt` | Program tidak crash, tampilkan error penanganan file | Tampil pesan `[Error] File '...' tidak ditemukan!` | **PASS** |
| TC06 | Empty Data | File input kosong | Rata-rata bernilai 0, tidak ZeroDivisionError | Mengembalikan `None` / 0 secara aman | **PASS** |

---

## 2. Catatan Perbaikan Bug (Bug Log)

| ID Bug | Gejala Masalah | Penyebab Utama | Perbaikan yang Done | Status |
|---|---|---|---|---|
| BUG-01 | Output `laporan.txt` error saat folder `output/` belum ada | Path folder `output/` belum dibuat otomatis | Menambahkan `os.makedirs(os.path.dirname(path_output), exist_ok=True)` pada `output.py` | **Closed** |
| BUG-02 | Potensi `ZeroDivisionError` saat file kosong | Pembagian total nilai dengan `len(nilai)=0` | Menambahkan pengecekan `if len(nilai) == 0: return 0` pada `proses.py` | **Closed** |