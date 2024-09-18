##
cuaca = str(input("Masukkan cuaca hari ini: "))
if cuaca == "cerah":
    ptint("pergi ke sekolah")
elif cuaca == "hujan":
    print("tetap di rumah")
else:
    print("invalid")


##
print("===menu===")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
pilihan = int(input("Masukkan pilihan: "))
if pilihan == 1:
    input1 = int(input("Masukkan angka pertama: "))
    input1 = int(input("Masukkan angka kedua: "))
    print(f"Hasil penjumlahan {input1} + {input2} = {input1} + {input2}")
elif pilihan == 2:
    input1 = int(input("Masukkan angka pertama: "))
    input1 = int(input("Masukkan angka kedua: "))
    print(f"Hasil penjumlahan {input1} - {input2} = {input1} - {input2}")
elif pilihan == 3:
    input1 = int(input("Masukkan angka pertama: "))
    input1 = int(input("Masukkan angka kedua: "))
    print(f"Hasil penjumlahan {input1} * {input2} = {input1} * {input2}")

##
masukkan = int(input("Masukkan angka: "))
if masukkan == 1:
    print("1")
elif masukkan == 2:
    print("2")
elif masukkan == 3:
    print("3")
elif masukkan == 4:
    print("4")
else:
    print("Invalid")

##
cuaca = str(input("masukkan cuaca hari ini: "))

if cuaca =="cerah":
    print("belajar di sekolah")
elif cuaca == "hujan":
    print("belajar di rumah")
else :
    print("invalid")

##
angka =  int(input("masukkan angka antara 1 dan 4: "))
if angka == 1:
    print ("memasukkan angka 1.")
elif angka in [2, 3]:
    print ("masukkan angka 2 atau 3.")    
elif angka == 4:
    print ( "masukkan angka 4.")
else :
    print ("angka yang dimasukkan tidak valid. Harus antara 1 dan 4")

##
a = int(input("masukkan angka 1 : "))
b= int(input("masukkan angka kedua 2 : "))

if a > b :
    print("kelinci")
if a < b :
        print("kura-kura")
if a == b :
            print("kerbau")
else:
    print("invalid")
