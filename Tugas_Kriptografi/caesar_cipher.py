def caesar_cipher(teks, k):
    hasil = ""

    for karakter in teks:
        if karakter.isalpha():
            if karakter.isupper():
                hasil += chr((ord(karakter) - ord('A') + k) % 26 + ord('A'))
            else:
                hasil += chr((ord(karakter) - ord('a') + k) % 26 + ord('a'))
        else:
            hasil += karakter

    return hasil


print("=== APLIKASI CAESAR CIPHER ===")

teks = input("Masukkan teks: ")
k = int(input("Masukkan kunci/pergeseran: "))

hasil = caesar_cipher(teks, k)

print("Hasil enkripsi:", hasil)