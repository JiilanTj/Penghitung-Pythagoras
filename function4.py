def login():
    nama = input("Masukkan nama Anda: ")
    nim = input("Masukkan NIM Anda: ")
    
    if nama == "Your Name" and nim == "999":
        return True
    else:
        return False

def hitung_alas():
    sisi_tegak = float(input("Masukkan panjang sisi tegak: "))
    sisi_miring = float(input("Masukkan panjang sisi miring: "))
    alas = (sisi_miring**2 - sisi_tegak**2)**0.5
    return alas

def hitung_sisi_tegak():
    alas = float(input("Masukkan panjang alas: "))
    sisi_miring = float(input("Masukkan panjang sisi miring: "))
    sisi_tegak = (sisi_miring**2 - alas**2)**0.5
    return sisi_tegak

def hitung_sisi_miring():
    alas = float(input("Masukkan panjang alas: "))
    sisi_tegak = float(input("Masukkan panjang sisi tegak: "))
    sisi_miring = (alas**2 + sisi_tegak**2)**0.5
    return sisi_miring

def main():
    if login():
        print("Berhasil Login!")

        print("Pilih sisi yang ingin Anda hitung :")
        print("1. Alas")
        print("2. Sisi Tegak")
        print("3. Sisi Miring")

        pilihan = input("Masukkan nomor pilihan Anda (1, 2, atau 3): ")

        if pilihan == "1":
            alas = hitung_alas()
            print("Panjang alas adalah:", alas)
        elif pilihan == "2":
            sisi_tegak = hitung_sisi_tegak()
            print("Panjang sisi tegak adalah:", sisi_tegak)
        elif pilihan == "3":
            sisi_miring = hitung_sisi_miring()
            print("Panjang sisi miring adalah:", sisi_miring)
        else:
            print("Pilihan tidak valid. Hanya dapat memilih 1, 2, atau 3.")
    else:
        print("Login gagal. Anda tidak memiliki akses ke program ini.")

if __name__ == "__main__":
    main()
