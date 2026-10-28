from src.input_data import baca_data, validasi_input
from src.proses import ringkasan, status_lulus
from src.output import tampilkan_ringkasan, simpan_laporan

def main():
    path_input = "data/contoh_data.txt"
    
    # 1. Alur Input Data
    data_raw = baca_data(path_input)
    if data_raw is None:
        return

    # 2. Alur Validasi & Processing Logika
    data_valid, _ = validasi_input(data_raw)
    stat = ringkasan(data_valid, batas=75)
    detail_lulus, _ = status_lulus(data_valid, batas=75)

    # 3. Alur Output & Export Laporan
    tampilkan_ringkasan(stat)
    simpan_laporan(stat, detail_lulus)

if __name__ == "__main__":
    main()