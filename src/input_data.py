import os

def baca_data(path_file):
    """Membaca file teks dan mengembalikan list baris data mentah."""
    if not os.path.exists(path_file):
        print(f"[Error] File '{path_file}' tidak ditemukan!")
        return None

    data_baris = []
    with open(path_file, 'r', encoding='utf-8') as file:
        for baris in file:
            baris = baris.strip()
            if baris:
                data_baris.append(baris)
    return data_baris

def validasi_input(data_baris):
    """Memeriksa format data dan menyaring nilai valid (0-100)."""
    data_valid = []
    data_invalid = []

    for baris in data_baris:
        parts = baris.split(',')
        if len(parts) == 2:
            nama = parts[0].strip()
            try:
                nilai = float(parts[1].strip())
                if 0 <= nilai <= 100:
                    data_valid.append({"nama": nama, "nilai": nilai})
                else:
                    data_invalid.append({"nama": nama, "nilai": nilai, "alasan": "Di luar rentang 0-100"})
            except ValueError:
                data_invalid.append({"nama": nama, "nilai": parts[1], "alasan": "Format nilai bukan angka"})

    return data_valid, data_invalid