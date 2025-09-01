data_siswa = []
while True:
       nama = input("masukkan nama siswa: ")
       try:
           umur = int(input("masukkan umur siswa: ")) 
           nilai = int(input("masukkan nilai siswa: "))  
       except ValueError:
           print("umur dan nilai harus angka!")
           continue
           
       siswa = {"nama": nama, "umur": umur, "nilai": nilai}
       data_siswa.append(siswa)

       #lanjut atau tidak?
       lanjut = input("ketik (y/n) untuk menambah siswa: ")
       if lanjut.lower() != "y":
          break

print("\nData Siswa")
for s in data_siswa:
    print(f"Nama: {s['nama']}, Umur: {s['umur']}, Nilai: {s['nilai']}")
