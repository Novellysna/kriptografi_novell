def vigenere_cipher(teks, kunci):
    hasil = ""
    indeks_kunci = 0

    for karakter in teks:
        if karakter.isalpha():
            nilai_teks = ord(karakter.upper()) - ord('A')
            nilai_kunci = ord(kunci[indeks_kunci % len(kunci)].upper()) - ord('A')

            nilai_hasil = (nilai_teks + nilai_kunci) % 26

            hasil += chr(nilai_hasil + ord('A'))
            indeks_kunci += 1
        else:
            hasil += karakter

    return hasil


print("=== APLIKASI VIGENERE CIPHER ===")

teks = input("Masukkan teks: ")
kunci = input("Masukkan kunci: ")

hasil = vigenere_cipher(teks, kunci)

print("Hasil enkripsi:", hasil)