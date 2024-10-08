# Daftar pengguna dengan informasi: [username, password, role]
pengguna = [
    ["admin", "admin123", "admin"],
    ["user1", "user123", "user"],
]

# Daftar penjualan diamond: [username, jumlah_diamond, harga]
penjualan_diamond = []

# Menu utama
while True:
    print(
"""
==============================
|             MENU           |
==============================
|     1. Tambah Diamond      |
|     2. Lihat Penjualan     | 
|     3. Update Penjualan    |
|     4. Hapus Penjualan     |
|     5. KELUAR              |
==============================
"""
)
    pilihan = input("Pilih opsi: ")

    if pilihan == "1":
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")

        # Cek login
        role = None
        for user in pengguna:
            if user[0] == username and user[1] == password:
                role = user[2]
                break
        
        if role is None:
            print("Login gagal. Username atau password salah.")
            continue
        
        print(f"Selamat datang, {username} ({role})!")

        while True:
               print(
                   """
                   ==============================
                   |             MENU           |
                   ==============================
                   |     1. Tambah Diamond      |
                   |     2. Lihat Penjualan     | 
                   |     3. Update Penjualan    |
                   |     4. Hapus Penjualan     |
                   |     5. KELUAR              |
                   ==============================
                   """
                   )
               opsi = input("Pilih opsi: ")
               
               if opsi == "1" and role == "admin":
                username_user = input("Masukkan username pengguna: ")
                jumlah_diamond = input("Masukkan jumlah diamond: ")
                harga = input("Masukkan harga: ")
                penjualan_diamond.append([username_user, jumlah_diamond, harga])
                print("Diamond berhasil ditambahkan.")
                
               elif opsi == "2":
                print("\n=== Daftar Penjualan Diamond ===")
                if penjualan_diamond:
                    for sale in penjualan_diamond:
                        print(f"Pengguna: {sale[0]}, Jumlah: {sale[1]}, Harga: {sale[2]}")
                else:
                    print("Tidak ada penjualan yang tersedia.")
               elif opsi == "3" and role == "admin":
                username_user = input("Masukkan username pengguna yang ingin diupdate: ")
                ditemukan = False
                for sale in penjualan_diamond:
                    if sale[0] == username_user:
                        ditemukan = True
                        jumlah_diamond = input("Masukkan jumlah diamond baru: ")
                        harga = input("Masukkan harga baru: ")
                        sale[1] = jumlah_diamond
                        sale[2] = harga
                        print("Penjualan berhasil diupdate.")
                        break
                if not ditemukan:
                    print("Pengguna tidak ditemukan.")
                elif opsi == "4" and role == "admin":
                    username_user = input("Masukkan username pengguna yang ingin dihapus: ")
                ditemukan = False
                for sale in penjualan_diamond:
                    if sale[0] == username_user:
                        penjualan_diamond.remove(sale)
                        ditemukan = True
                        print("Penjualan berhasil dihapus.")
                        break
                if not ditemukan:
                    print("Pengguna tidak ditemukan.")
                elif opsi == "5":
                    print("Anda telah logout.")
                break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")
    elif pilihan == "2":
        username_baru = input("Masukkan username baru: ")
        password_baru = input("Masukkan password baru: ")
        
        # Cek registrasi
        ditemukan = False
        for user in pengguna:
            if user[0] == username_baru:
                ditemukan = True
                break
        
        if ditemukan:
            print("Username sudah terdaftar.")
        else:
            pengguna.append([username_baru, password_baru, "user"])  # Default role adalah user
            print("Registrasi berhasil.")

    elif pilihan == "3":
        print("Keluar dari program.")
        break

    else:
        print("Opsi tidak valid. Silakan coba lagi")
