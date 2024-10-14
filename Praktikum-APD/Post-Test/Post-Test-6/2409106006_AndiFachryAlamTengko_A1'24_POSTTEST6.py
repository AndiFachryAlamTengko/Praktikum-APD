# Daftar pengguna dengan informasi: {username: {password, role}}
pengguna = {
    "admin": {"password": "admin123", "role": "admin"},
    "user1": {"password": "user123", "role": "user"},
}

# Daftar penjualan diamond: {username: {jumlah_diamond, harga}}
penjualan_diamond = {}

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
        if username in pengguna and pengguna[username]["password"] == password:
            role = pengguna[username]["role"]

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
                penjualan_diamond[username_user] = {"jumlah_diamond": jumlah_diamond, "harga": harga}
                print("Diamond berhasil ditambahkan.")
                
            elif opsi == "2":
                print("\n=== Daftar Penjualan Diamond ===")
                if penjualan_diamond:
                    for user, sale in penjualan_diamond.items():
                        print(f"Pengguna: {user}, Jumlah: {sale['jumlah_diamond']}, Harga: {sale['harga']}")
                else:
                    print("Tidak ada penjualan yang tersedia.")
            elif opsi == "3" and role == "admin":
                username_user = input("Masukkan username pengguna yang ingin diupdate: ")
                if username_user in penjualan_diamond:
                    jumlah_diamond = input("Masukkan jumlah diamond baru: ")
                    harga = input("Masukkan harga baru: ")
                    penjualan_diamond[username_user] = {"jumlah_diamond": jumlah_diamond, "harga": harga}
                    print("Penjualan berhasil diupdate.")
                else:
                    print("Pengguna tidak ditemukan.")
            elif opsi == "4" and role == "admin":
                username_user = input("Masukkan username pengguna yang ingin dihapus: ")
                if username_user in penjualan_diamond:
                    del penjualan_diamond[username_user]
                    print("Penjualan berhasil dihapus.")
                else:
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
        if username_baru in pengguna:
            print("Username sudah terdaftar.")
        else:
            pengguna[username_baru] = {"password": password_baru, "role": "user"}  # Default role adalah user
            print("Registrasi berhasil.")

    elif pilihan == "5":
        print("Keluar dari program.")
        break

    else:
        print("Opsi tidak valid. Silakan coba lagi.")


