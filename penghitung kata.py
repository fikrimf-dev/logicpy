def hitung_huruf(kata):
    # Mensetting kata yang akan di hitung
    karakter_unik = set(kata)
    hitung = len(karakter_unik)
    huruf = " ".join(sorted(karakter_unik))
    result = f"Jumlah huruf yang ada adalah {hitung} ({huruf})"
    return result  # Megembalikan hitungan huruf yang didapat

print(hitung_huruf("STRESS"))
print(hitung_huruf("SELASA"))
print(hitung_huruf("INTERNET"))
