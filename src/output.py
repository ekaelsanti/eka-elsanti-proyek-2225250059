import os

def tampilkan_ringkasan(stat):
    """Menampilkan ringkasan hasil analisis ke terminal[cite: 5]."""
    print("=== PROGRAM REKAP & ANALISIS NILAI ===")
    print(f"Siswa Valid  : {stat['jumlah']}")
    print(f"Rata-rata    : {stat['rata_rata']:.2f}")
    print(f"Min / Max    : {stat['minimum']} / {stat['maksimum']}")
    print(f"Jumlah Tuntas: {stat['lulus']}")

def simpan_laporan(stat, detail_lulus, path_output="output/laporan.txt"):
    """Menyimpan ringkasan laporan ke file teks[cite: 5]."""
    os.makedirs(os.path.dirname(path_output), exist_ok=True)
    with open(path_output, 'w', encoding='utf-8') as f:
        f.write("=== LAPORAN REKAP & ANALISIS NILAI MATEMATIKA ===\n\n")
        f.write(f"Jumlah Siswa Valid : {stat['jumlah']}\n")
        f.write(f"Rata-rata Kelas    : {stat['rata_rata']:.2f}\n")
        f.write(f"Nilai Terendah     : {stat['minimum']}\n")
        f.write(f"Nilai Tertinggi    : {stat['maksimum']}\n")
        f.write(f"Jumlah Tuntas      : {stat['lulus']}\n\n")
        f.write("--- Detail Ketuntasan Siswa ---\n")
        for item in detail_lulus:
            f.write(f"- {item['nama']}: {item['nilai']} ({item['status']})\n")
    print(f"\n[Sukses] Laporan berhasil disimpan ke '{path_output}'")