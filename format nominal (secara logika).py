def format_nominal(nominal):
    # Pisahkan bagian bilangan bulat dan desimal
    bilangan_bulat = int(nominal)
    desimal = int(round((nominal - bilangan_bulat) * 100))

    # Konversi bagian bilangan bulat menjadi string
    bilangan_bulat_str = str(bilangan_bulat)

    # Lakukan pemisahan ribuan
    ribuan = []
    while bilangan_bulat_str:
        ribuan.append(bilangan_bulat_str[-3:])
        bilangan_bulat_str = bilangan_bulat_str[:-3]
    bilangan_bulat_diformat = ",".join(ribuan[::-1])

    # Gabungkan kembali bilangan bulat yang sudah diformat
    nominal_diformat = (
        bilangan_bulat_diformat + "." + "{:02d}".format(desimal)
    )

    return nominal_diformat

print(format_nominal(2500000.90))
print(format_nominal(1200.00))
print(format_nominal(1200))
