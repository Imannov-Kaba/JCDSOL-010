listNilaiSiswa = [
    {
        "nama" : "Anto",
        "absen" : 1,
        "nilai" : 85
    },
    {
        "nama" : "Budi",
        "absen" : 2,
        "nilai" : 70
    },
    {
        "nama" : "Sukijan",
        "absen" : 17,
        "nilai" : 95
    }
]

def daftarNilaiSiswa() :
    print("Daftar Nilai Siswa\n")
    print("Nama\t| Absen\t| Nilai\n")
    for i in range(len(listNilaiSiswa)):
        print("{}\t| {}\t| {}\n".format(listNilaiSiswa[i]["nama"],listNilaiSiswa[i]["absen"],listNilaiSiswa[i]["nilai"]))
while True :
    print("Selamat datang di Aplikasi Input Data Siswa\n\n")
    print("List Menu :\n1. Menampilkan Daftar Siswa\n2. Menambah Data Siswa\n3. Menghapus Data Siswa\n4. Mengubah Data Siswa\n5. Exit Program\n")
    perintah = input("Masukkan angka menu yang ingin dijalankan : ")

    if(perintah == "1") :
        daftarNilaiSiswa()
    elif(perintah == "2") :
        namaSiswa = input("Masukkan nama siswa yang ingin dimasukkan datanya :")
        absenSiswa = input("\nMasukkan absen siswa yang ingin dimasukkan datanya :")
        nilaiSiswa = input("\nMasukkan nilai siswa yang ingin dimasukkan datanya :")
        listNilaiSiswaBaru = {
            "nama" : namaSiswa,
            "absen" : int(absenSiswa),
            "nilai" : int(nilaiSiswa)
            }
        listNilaiSiswa.append(listNilaiSiswaBaru)
        daftarNilaiSiswa()
    elif(perintah == "3") :
        daftarNilaiSiswa()
        hapusDataSiswa = input("Masukkan absen data siswa yang ingin dihapus : \n")
        for i in range(len(listNilaiSiswa)) :
            if listNilaiSiswa[i]["absen"] == int(hapusDataSiswa):
                del listNilaiSiswa[i]
                break
        daftarNilaiSiswa()
    elif(perintah == "4") :
        while True :
            daftarNilaiSiswa()
            siapaDataUbah = input("Masukkan absen siswa yang ingin diubah datanya: ")
            ubahNilai = input("Masukkan nilai yang seharusnya: ")
            for i in range(len(listNilaiSiswa)):
                if listNilaiSiswa[i]["absen"] == int(siapaDataUbah):
                    listNilaiSiswa[i]["nilai"] = int(ubahNilai)
                    break
            daftarNilaiSiswa()
            transaksiLain = input("Mau merubah data yang lain? (ya/tidak) = ")
            if(transaksiLain == "tidak") :
                break
    elif(perintah == "5") :
        break