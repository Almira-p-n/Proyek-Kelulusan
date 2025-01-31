import random

def angka_dadu():
    angka = random.randint(1, 6)
    if angka == 1:
        return "1 (satu) "
    elif angka == 2:
        return "2 (dua) "
    elif angka == 3:
        return "3 (tiga) "
    elif angka == 4:
        return "4 (empat) "
    elif angka == 5:
        return "5 (lima) "
    elif angka == 6:
        return "6 (enam) "