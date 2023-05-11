def bilangan_prima(n):
    prima = []
    bilangan = 2  # Dimulai dari bilangan 2
    while len(prima) < n:  # Loop hingga list prima memiliki panjang n
        ini_prima = True
        for i in range(
            2, int(bilangan**0.5) + 1
        ):  # Loop untuk memeriksa bilangan prima
            if (
                bilangan % i == 0
            ):  # Jika bilangan habis dibagi i, berarti bukan bilangan prima
                ini_prima = False
                break
        if (
            ini_prima
        ):  # Jika predikat bilangan masih prima, tambahkan ke list prima
            prima.append(bilangan)
        bilangan += 1  # Cek bilangan selanjutnya
    return prima  # Mengembalikan list bilangan prima

def bilangan_prima_seris(n):
    prima = bilangan_prima(n)  # Mendapatkan n bilangan prima
    seris = [0]  # List untuk menyimpan deret, dimulai dari 0
    for i in range(n):
        seris.append(
            seris[-1] + prima[i]
        )  # Tambahkan elemen baru dengan menjumlahkan bilangan prima sebelumnya
    return seris  # Mengembalikan list deret bilangan prima

print(bilangan_prima_seris(4))
print(bilangan_prima_seris(6))
