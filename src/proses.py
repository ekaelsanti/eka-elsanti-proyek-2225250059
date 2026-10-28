def hitung_rata_rata(nilai):
    """Menghitung rata-rata dari list nilai[cite: 5]."""
    if len(nilai) == 0:
        return 0
    return sum(nilai) / len(nilai)

def status_lulus(data_valid, batas=75):
    """Menentukan status kelulusan/ketuntasan berdasarkan KKM[cite: 5]."""
    hasil = []
    jumlah_lulus = 0
    for item in data_valid:
        lulus = item['nilai'] >= batas
        if lulus:
            jumlah_lulus += 1
        hasil.append({
            "nama": item['nama'],
            "nilai": item['nilai'],
            "status": "TUNTAS" if lulus else "BELUM TUNTAS"
        })
    return hasil, jumlah_lulus

def ringkasan(data_valid, batas=75):
    """Menghasilkan statistik ringkasan data[cite: 5]."""
    if not data_valid:
        return {
            "jumlah": 0,
            "rata_rata": 0,
            "minimum": None,
            "maksimum": None,
            "lulus": 0
        }

    nilai_list = [item['nilai'] for item in data_valid]
    _, total_lulus = status_lulus(data_valid, batas)

    return {
        "jumlah": len(nilai_list),
        "rata_rata": hitung_rata_rata(nilai_list),
        "minimum": min(nilai_list),
        "maksimum": max(nilai_list),
        "lulus": total_lulus
    }