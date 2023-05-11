def menghitung_pantulan_bola(ketinggian):
    # Inisialisasi variabel
    perhitungan = 0
    total_ketinggian = 0

    while ketinggian > 0.5:  # Loop selama bola masih dapat memantul
        perhitungan += 1  # Tambahkan jumlah bola yang memantul
        total_ketinggian += (
            ketinggian  # Tambahkan ketinggian bola yang sedang memantul
        )
        ketinggian /= 2  # Hitung ketinggian bola setelah memantul

    # Tambahkan ketinggian bola terakhir yang jatuh tanpa memantul
    total_ketinggian += ketinggian

    # Format output deret dan jumlah bola memantul
    output = "Bola memantul sebanyak {} kali dengan total jarak terjatuh {} meter.".format(
        perhitungan, total_ketinggian
    )

    return output

print(menghitung_pantulan_bola(5))
