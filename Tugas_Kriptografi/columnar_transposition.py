def columnar_transposition(teks, kunci):
    teks = teks.replace(" ", "").upper()

    # Membuat baris berdasarkan panjang kunci
    baris = []
    for i in range(0, len(teks), kunci):
        baris.append(teks[i:i + kunci])

    # Jika baris terakhir tidak penuh, tambahkan X
    if len(baris[-1]) < kunci:
        baris[-1] = baris[-1].ljust(kunci, "X")

    # Membaca teks secara vertikal
    hasil = ""

    for kolom in range(kunci):
        for baris_data in baris:
            hasil += baris_data[kolom]

    return hasil


print("=== APLIKASI COLUMNAR TRANSPOSITION CIPHER ===")

teks = input("Masukkan teks: ")
kunci = int(input("Masukkan panjang kunci: "))

hasil = columnar_transposition(teks, kunci)

print("Hasil enkripsi:", hasil)