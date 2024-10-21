pengguna = {
    "admin": {"password": "admin123", "role": "admin"},
}

penjualan_diamond = {}

total_penjualan = 0
total_diamond = 0
login_attempts = 0

# Daftar isi diamond yang tersedia
daftar_diamond = {
    1: {"jenis": "Diamond 50", "jumlah": 50, "harga": 50000},
    2: {"jenis": "Diamond 100", "jumlah": 100, "harga": 90000},
    3: {"jenis": "Diamond 200", "jumlah": 200, "harga": 170000},
    4: {"jenis": "Diamond 500", "jumlah": 500, "harga": 400000},
}
9
def tampilkan_daftar_diamond():
    """Menampilkan daftar diamond yang tersedia."""
    print("\n=== Daftar Diamond yang Tersedia ===")
    for key, value in daftar_diamond.items():
        print(f"{key}. {value['jenis']} - Jumlah: {value['jumlah']} - Harga: Rp{value['harga']}")
    print("")

def tambah_penjualan(username_user, jumlah_diamond, harga):
    """Menambah penjualan diamond ke dalam daftar dan update total."""
    global total_penjualan, total_diamond
    penjualan_diamond[username_user] = {"jumlah_diamond": jumlah_diamond, "harga": harga}
    total_penjualan += 1
    total_diamond += jumlah_diamond
    print("Diamond berhasil ditambahkan.")
    print(f"Total penjualan saat ini: {total_penjualan}")
    print(f"Total diamond yang terjual: {total_diamond}")

def hapus_penjualan(username_user):
    """Menghapus penjualan diamond dan mengurangi total."""
    global total_penjualan, total_diamond
    if username_user in penjualan_diamond:
        data_terhapus = penjualan_diamond[username_user]
        total_penjualan -= 1
        total_diamond -= data_terhapus['jumlah_diamond']
        del penjualan_diamond[username_user]
        print("Penjualan berhasil dihapus.")
        print(f"Total penjualan saat ini: {total_penjualan}")
        print(f"Total diamond yang terjual: {total_diamond}")
    else:
        print("Pengguna tidak ditemukan.")

def update_penjualan(username_user, jumlah_diamond, harga):
    """Mengupdate penjualan diamond yang sudah ada dan memperbarui total."""
    global total_diamond
    if username_user in penjualan_diamond:
        data_lama = penjualan_diamond[username_user]
        # Menghitung selisih jumlah diamond
        selisih_diamond = jumlah_diamond - data_lama['jumlah_diamond']
        total_diamond += selisih_diamond
        # Update penjualan
        penjualan_diamond[username_user] = {"jumlah_diamond": jumlah_diamond, "harga": harga}
        print("Penjualan berhasil diupdate.")
        print(f"Total diamond yang terjual: {total_diamond}")
    else:
        print("Pengguna tidak ditemukan.")

def lihat_penjualan():
    """Menampilkan semua penjualan diamond."""
    print("\n=== Daftar Penjualan Diamond ===")
    if penjualan_diamond:
        for user, sale in penjualan_diamond.items():
            print(f"Pengguna: {user}, Jumlah: {sale['jumlah_diamond']}, Harga: {sale['harga']}")
        print(f"\nTotal penjualan: {total_penjualan}")
        print(f"Total diamond yang terjual: {total_diamond}")
    else:
        print("Tidak ada penjualan yang tersedia.")

def beli_diamond(username_user):
    """Prosedur bagi user untuk membeli diamond."""
    if username_user in pengguna:
        tampilkan_daftar_diamond()
        try:
            pilihan = int(input("Pilih jenis diamond (1-4): "))
            if pilihan in daftar_diamond:
                diamond_terpilih = daftar_diamond[pilihan]
                tambah_penjualan(username_user, diamond_terpilih["jumlah"], diamond_terpilih["harga"])
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")
        except ValueError:
            print("Pilihan harus berupa angka.")
    else:
        print("Pengguna tidak ditemukan.")

def proses_lihat_penjualan():
    """Prosedur untuk melihat penjualan diamond."""
    lihat_penjualan()

def menu_admin(role):
    """Menampilkan menu untuk admin dan meminta pilihan dari pengguna admin."""
    while True:
        print(
        """
        ==============================
        |           MENU ADMIN        |
        ==============================
        |  1. Tambah Diamond          |
        |  2. Lihat Daftar Diamond    |
        |  3. Update Diamond          |
        |  4. Hapus Diamond           |
        |  5. KELUAR                  |
        ==============================
        """
        )
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
                        # Menambahkan diamond baru
            jenis_diamond = input("Masukkan jenis diamond: ")
            jumlah_diamond = int(input("Masukkan jumlah diamond: "))
            harga_diamond = int(input("Masukkan harga diamond: "))
            # Mencari ID yang unik
            id_diamond = max(daftar_diamond.keys()) + 1 if daftar_diamond else 1
            daftar_diamond[id_diamond] = {"jenis": jenis_diamond, "jumlah": jumlah_diamond, "harga": harga_diamond}
            print(f"Diamond '{jenis_diamond}' berhasil ditambahkan.")
        elif pilihan == "2":
           tampilkan_daftar_diamond()
        elif pilihan == "3":
            # Mengupdate diamond yang ada
            id_diamond = int(input("Masukkan ID diamond yang ingin diupdate: "))
            if id_diamond in daftar_diamond:
                print("Data diamond yang ada:", daftar_diamond[id_diamond])
                jenis_diamond = input("Masukkan jenis diamond baru (kosongkan jika tidak ingin mengubah): ")
                jumlah_diamond = input("Masukkan jumlah diamond baru (kosongkan jika tidak ingin mengubah): ")
                harga_diamond = input("Masukkan harga diamond baru (kosongkan jika tidak ingin mengubah): ")

                # Update hanya jika input tidak kosong
                if jenis_diamond:
                    daftar_diamond[id_diamond]["jenis"] = jenis_diamond
                if jumlah_diamond:
                    daftar_diamond[id_diamond]["jumlah"] = int(jumlah_diamond)
                if harga_diamond:
                    daftar_diamond[id_diamond]["harga"] = int(harga_diamond)

                print(f"Diamond ID {id_diamond} berhasil diupdate.")
            else:
                print("ID diamond tidak ditemukan.")
        elif pilihan == "4":
            # Menghapus diamond
            id_diamond = int(input("Masukkan ID diamond yang ingin dihapus: "))
            if id_diamond in daftar_diamond:
                del daftar_diamond[id_diamond]
                print(f"Diamond ID {id_diamond} berhasil dihapus.")
            else:
                print("ID diamond tidak ditemukan.")
        elif pilihan == "5":
            print("Keluar dari menu admin.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")





def menu_user(username_user):
    """Menampilkan menu untuk user dan meminta pilihan dari pengguna."""
    while True:
        print(
        """
        ==============================
        |             MENU           |
        ==============================
        |     1. Beli Diamond        |
        |     2. Lihat Daftar Diamond|
        |     3. KELUAR              |
        ==============================
        """
        )
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            beli_diamond(username_user)
        elif pilihan == "2":
            tampilkan_daftar_diamond()
        elif pilihan == "3":
            print("Keluar dari program.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")


def login_sistem():
    """Sistem login dan register pengguna."""
    while True:
        print(
        """
        ==============================
        |        LOGIN / REGISTER     |
        ==============================
        |     1. Login               |
        |     2. Registrasi          |
        |     3. Keluar              |
        ==============================
        """
        )
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            role = login(username, password)

            if role == "admin":
                print(f"Login berhasil. Selamat datang, {username} (admin)!")
                menu_admin(role)
            elif role == "user":
                print(f"Login berhasil. Selamat datang, {username} (user)!")
                menu_user(username)
            else:
                print("Login gagal. Username atau password salah.")

        elif pilihan == "2":
            username_baru = input("Masukkan username baru: ")
            password_baru = input("Masukkan password baru: ")
            role = input("Masukkan role (admin/user): ").lower()

            if role in ["admin", "user"]:
                register(username_baru, password_baru, role)
            else:
                print("Role tidak valid. Harus 'admin' atau 'user'.")

        elif pilihan == "3":
            print("Keluar dari sistem.")
            break
        else:
            print("Opsi tidak valid. Silakan coba lagi.")

# Fungsi untuk login pengguna
def login(username, password):
    """Mengecek login pengguna dan mengembalikan role jika berhasil."""
    global login_attempts
    login_attempts += 1
    if username in pengguna and pengguna[username]["password"] == password:
        return pengguna[username]["role"]
    return None

# Fungsi untuk register pengguna
def register(username_baru, password_baru, role="user"):
    """Prosedur untuk registrasi pengguna baru."""
    if username_baru in pengguna:
        print("Username sudah terdaftar.")
    else:
        pengguna[username_baru] = {"password": password_baru, "role": role}
        print(f"Registrasi berhasil untuk {username_baru} dengan role {role}.")

# Memulai program dengan login sistem
login_sistem()
