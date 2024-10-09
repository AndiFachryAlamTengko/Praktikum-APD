Daftar_Buku = {
    "Buku1" : "Herry Poter",
    "Buku2" : "Percy Jackson",
    "Buku3" : "Twilight"
}

#print(Daftar_Buku["Buku2"])
#print(Daftar_Buku["Buku1"])
#print(Daftar_Buku["Buku3"])


Biodata = {
    "Nama" : "andi fachry alam tengko",
    "NIM" : 2409106006,
    "KRS" : ["Program web", "Struktur Data"],
    "Mahasiswa_Aktiv" :True,
    "Social Merdia" : {
        "Instagram" : "@a.fachry__",
        "Discord" : "\'andifachry"
    }

}
\
Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}

#Film["ZombieLend"] = "comedy"
Film.update({"hour" : "Thriller"})
print(Film)

print("Jumlah data dalam dict Biodata = ")

data = {
"Nama" : "Aldy",
"Umur" : 19,
"Jurusan" : "Informatika"
}
print("Jumlah Data = ", len(data))


Buku = {
"No Longer Human" : "Osamu Dazai",
"Harry Potter" : "J.K. Rowlings",
"Hamlet" : "William Shakespeare"
}
pinjam = Buku.copy()
print("Dictionary yang Telah Disalin : ", pinjam)

{'Nama': 'Aldy', 'Umur': 19, 'Jurusan': 'Informatika'}
{}
data = {
"Nama" : "Aldy",
"Umur" : 19,
"Jurusan" : "Informatika"
}
print("Jumlah Data = ", len(data))

Buku = {
"No Longer Human" : "Osamu Dazai",
"Harry Potter" : "J.K. Rowlings",
"Hamlet" : "William Shakespeare"
}
pinjam = Buku.copy()
print("Dictionary yang Telah Disalin : ", pinjam)

key = "apel", "jeruk", "mangga"
value = 1
buah = dict.fromkeys(key, value)
print(buah)
{'apel': 1, 'jeruk': 1, 'mangga': 1}

###
Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81,
"Kimia" : 78,
"Fisika" : 80
}
#menggunakan keys
for i in Nilai.keys():
print(i)
print("")
#menggunakan value
for i in Nilai.values():
print(i)

Matematika
B. Indonesia
B. Inggris
Kimia
Fisika
80
90
81
78
80

Nilai = {
"Matematika" : 80,
"B. Indonesia" : 90,
"B. Inggris" : 81
}
#sebelum Setdefault
print(Nilai)
print("")
#menggunakan setdefault
print("Nilai : ", Nilai.setdefault("Kimia", 70))
print("")
#setelah menggunakan setdefault
print(Nilai)

{'Matematika': 80, 'B. Indonesia': 90, 'B. Inggris':
81}

Nilai : 70
{'Matematika': 80, 'B. Indonesia': 90, 'B. Inggris':
81, 'Kimia': 70}

##
Musik = {
"The Chainsmoker" : ["All we Know", "The
Paris"],
"Alan Walker" : ["Alone", "Lily"],
"Neffex" : ["Best of Me", "Memories"]
}
for i, j in Musik.items():
print(f"Musik milik {i} adalah : ")
for song in j:
print(song)
print("")
Musik milik The Chainsmoker adalah :
All we Know
The Paris

Musik milik Alan Walker adalah :
Alone
Lily

Musik milik Neffex adalah :
Best of Me
Memories

Biodata = {}

while True:
    print("1. Tambah")
    print("2. Tampilakan")
    print("3. Exit")
    pilihan =  int(input("(1/2/3) : "))

    if pilihan == 1:
        nama = input("Masukkan nama :")
        umur = input("Masukkan umur :")
        alamat = input("Masukkan alamat :")

        Biodata[nama] = { 
            'Umur' : umur,
            'Alamat' : alamat
        }

    elif pilihan == 2:
        for nama, info in Biodata.items():
            print(f"Nama : {nama}")
            print(f"Umur : {info['Umur']}")
            print(f"Alamat : {info['Alamat']}")

    elif pilihan == 3:
        print("exit ...")
        break

    else:
        print("Invalid ... ... ")

