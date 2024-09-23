Pilihan = int(input("Masukkan pilihan rumus BMR, 1 untuk Pria, 2 untuk Wanita = "))
Berat_Badan = float(input("Masukkan berat badan (dalam gram) = "))
Tinggi_Badan = float(input("Masukkan tinggi badan(KM) = "))
Umur = int(input("Masukkan umur = "))

Ubah_Berat_Badan = Berat_Badan / 1000
Ubah_Tinggi_Badan = Tinggi_Badan * 100000

# Level aktivitas harian
print("\nLevel Aktivitas Harian")
print("1. Aktivitas Minimal (jarang bergerak) = 1.25")
print("2. Aktivitas Sedang (olahraga 1-3 kali seminggu) = 1.36")
print("3. Aktivitas Tinggi (olahraga 4-7 kali seminggu) = 1.72")
pilihan_aktivitas = input("Pilihan (1/2/3): ")

level_aktivitas = 0
if pilihan_aktivitas == '1':
    level_aktivitas = 1.25
elif pilihan_aktivitas == '2':
    level_aktivitas = 1.36
elif pilihan_aktivitas == '3':
    level_aktivitas = 1.72

if Pilihan ==1:
    bmrpria = (10 * Ubah_Berat_Badan) + (6.25 * Ubah_Tinggi_Badan) - (5 * Umur) + 5
    print(f"\nKebutuhan Kalori Harian Anda (TDEE) adalah: {bmrpria} kalori.")
elif Pilihan ==2:
    bmrwanita = (10 * Ubah_Berat_Badan) + (6.25 * Ubah_Tinggi_Badan) - (5 * Umur) - 161
    print(f"\nKebutuhan Kalori Harian Anda (TDEE) adalah: {bmrwanita} kalori.")