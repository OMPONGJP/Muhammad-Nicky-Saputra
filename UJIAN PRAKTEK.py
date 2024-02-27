def penambahan (a,b) :
    hasil = a+b
    print(f"Hasil dari nilai yang anda masukan adalah : {hasil} ")
    
def pengurangan (a,b) :
    hasil = a-b
    print(f"Hasil dari nilai yang anda masukan adalah : {hasil}")
    
def pembagian (a,b) :
    hasil = a/b
    print(f"Hasil dari nilai yang anda masukan adalah : {hasil}")
    
def perkalian (a,b) :
    hasil = a*b
    print(f"Hasil dari nilai yang anda masukan adalah : {hasil}")
    
while True :
    
    print ("  ---------- SELAMAT DATANG ----------  ")
    print ("       Pilih Menu Yang Anda Inginkan                                   ")
    print ("1.Kalkulator")
    print ("2.Keluar")
    Pil1 =int(input("Masukan Pilihan Anda (1/2) :"))
    
    if Pil1 == 1 :
        
        print("----------- MASUKAN NILAI -----------                              ")
        a = int(input("Masukan Angka Pertama :"))
        b = int(input("Masukan Angka Kedua :"))
        print("   -------- METODE HITUNG --------\n1.Penjumlahan\n2.Pengurangan\n3.Pembagian\n4.Perkalian\n5.Keluar")
        o = str(input("Pilih Operasi :"))
        
        if o == '1':
            penambahan(a,b)
        elif o == '2':
            pengurangan(a,b)
        elif o == '3':
            pembagian(a,b)
        elif o == '4':
            perkalian(a,b)
        elif o == '5':
            print("Terima Kasih")
            break
        else:
            print("Pilihan Anda Tidak Ada")
            break
    elif Pil1 == 2 :
        
        print("---------- TERIMA KASIH TELAH MENGGUNAKAN APLIKASI SEDERHANA INI ----------")
        break
    else:
        print("Eror")
        break
    
    
    
        