# PROGRAM VALIDASI FORM INPUT
###### Nama   : JULIUS HUTABARAT
###### NIM    : 312410429
###### Kelas  : TI 24 A3

#### DESKRIPSI PROGRAM
Program ini digunakan untuk memvalidasikan data pendaftaran yaitu:
- Nama Lengkap (hanya huruf dan spasi).
- Nomor telepon (hanya angka, minimal 11 digit).
- Email (mengandung karakter @ dan . ).
Program memberikan pesan error jika ada validasi yang gagal, dan jika semua data valid, program menampilkan informasi pendaftaran.

### Fungsi-Fungsi Validasi
Deskripsi: Memastikan nama hanya mengandung huruf dan spasi.
###### Cara Kerja:
- Menghapus semua spasi menggunakan nama.replace(" ", "").
- Memeriksa apakah sisa karakter hanya berupa hurup dengan .isalpha() .
###### Hasil:
- Mengembalikan True jika valid, atau False jika tidak.

###### validasi_telepon(telepon)
Deskripsi: Memastikan nomor telepon hanya angka dan memiliki minimal 11 digit.
###### Cara Kerja:
- Memeriksa apakah semua karakter adalah angka dengan .isdigit() .
- Memastikan panjang string minimal 11 dengan len(telepon) >= 11.
###### Hasil:
- Mengembalikan True jika valid, atau False jika tidak.

###### validasi_email(email)
Deskripsi: Memastikan email mengandung karakter @ dan . .
###### Cara Kerja:
- Memeriksa apakah email berisi karakter @ dengan '@' in email.
- Memeriksa apakah email berisi karakter . dengan '.' in email.
###### Hasil:
- Mengembalikan True jika valid, atau False jika tidak.

### Fungsi Utama: validasi_pendaftaran()
a. Input Data
Program meminta pengguna untuk memasukkan:
- Nama lengkap.
- Nomor telepon (minimal 11 digit).
- Email.
Semua input disimpan dalam variabel:
- nama
- telepon
- email

### Validasi Input
Setiap input divalidasi menggunakan fungsi validasi:
- validasi_nama(nama)
- validasi_telepon(telepon)
- validasi_email(email)
Jika validasi gagal:
- Program mencetak pesan error yang sesuai.
- Variabel error diatur menjadi True .

### Tampilkan Hasil Validasi
Jika semua validasi berhasil ( error == False):
- Program mencetak pesan bahwa data pendaftaran valid.
- Menampilkan nama, nomor telepon, dan email yang dimasukkan.

### Blok if __name__ == "__main__":
- Menentukan bahwa program hanya akan dijalankan jika file ini dieksekusi langsung.
- Memanggil fungsi utama validasi_pendaftaran() .

## Contoh Jalannya Program
![Screenshot 2025-01-01 184409](https://github.com/user-attachments/assets/3e42bd6b-eb96-44b2-9c9a-8ebb0952ff24)
