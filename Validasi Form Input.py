def validasi_nama(nama):
    """Validasi nama hanya mengandung huruf dan spasi"""
    return nama.replace(" ", "").isalpha()

def validasi_telepon(telepon):
    """Validasi nomor telepon hanya mengandung angka dan minimal 11 digit"""
    return telepon.isdigit() and len(telepon) >= 11

def validasi_email(email):
    """Validasi email mengandung @ dan ."""
    return '@' in email and '.' in email

def validasi_pendaftaran():
    # Input data
    print("=== Form Pendaftaran ===")
    nama = input("Masukkan nama lengkap: ")
    telepon = input("Masukkan nomor telepon (minimal 11 digit): ")
    email = input("Masukkan email: ")
    
    # Validasi input
    error = False
    
    if not validasi_nama(nama):
        print("Error: Nama hanya boleh berisi huruf!")
        error = True
    
    if not validasi_telepon(telepon):
        print("Error: Nomor telepon harus berisi angka dan minimal 11 digit!")
        error = True
    
    if not validasi_email(email):
        print("Error: Email harus mengandung karakter @ dan .")
        error = True
    
    # Tampilkan hasil validasi
    if not error:
        print("\nData pendaftaran valid.")
        print("Nama:", nama)
        print("Telepon:", telepon)
        print("Email:", email)

# Jalankan program
if __name__ == "__main__":
    validasi_pendaftaran()