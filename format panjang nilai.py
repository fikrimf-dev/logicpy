def format_string(n, nilai):
    # Mengubah nilai menjadi string
    nilai_str = str(
        int(nilai * 100)
    )  # Konversi ke integer dan kali 100 agar nilai desimal menjadi integer

    # Memastikan panjang nilai sama dengan N
    while len(nilai_str) < n:
        nilai_str = "0" + nilai_str

    return nilai_str[:n]

print(format_string(5, 1))
print(format_string(5, 12.35))
print(format_string(10, 350))
print(format_string(7, 215.3))
