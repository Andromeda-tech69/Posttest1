#Perkenalkan saya Andromeda di sini saya akan membuat login sederhana dan program hitung volume bangun ruang
#Pada bagian login saya ingin membuat 3 input (nama, nim, password)
#Disini saya ingin membuat login yang jika salah satu dari parameter/input dari 3 di atas salah
#saya ingin output nya mengatakan secara spesifik letak kesalahannya seperti di bawah ini

def login():

    print("===============")
    print("SELAMAT DATANG")
    print("===============")
    # 3 Baris di atas tidak memiliki fungsi apa-apa selain hiasan
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    password = input("Masukkan password: ")
    

    if nama == "Andromeda HD" :
        if nim == "2309116038" :
            if password == "andromeda2511":
                print(f"Login berhasil, Selamat datang {nama} NIM: {nim}.")
                #Output : Login berhasil, Selamat datang Anromeda HD NIM :2309116038
            else :
                #Kondisi jika password yang dimasukkan salah maka akan menampilkan password salah, coba lagi
                #Lalu mengulang login dari awal
                print("password salah, coba lagi")
                login()
        else :
            #Kondisi jika NIM yang dimasukkan salah maka akan menampilkan NIM salah, coba lagi
            #Lalu mengulang login dari awal
            print("NIM salah, coba lagi")
            login()
    else :
        #Kondisi jika nama yang dimasukkan salah maka akan menampilkan nama salah, coba lagi
        #Lalu mengulang login dari awal
        print("nama salah, coba lagi")
        login()
    
def main():
    
    login()

    #Bagian dari tampilan menu program yang dimana didalamnya terdapat 4 opsi yang dapat dipilih
    #Lalu dilanjutkan ke langkah berikutnya
    print("========================================")
    print("Program menghitung volume bangun ruang")
    print("========================================")
    print("\nMenu Program:")
    print("1. Hitung Volume Bola")
    print("2. Hitung Volume Tabung")
    print("3. Hitung Volume Limas Segitiga")
    print("4. Keluar")

    pilihan = int(input("Pilih bangun ruang (1-4): "))

    #Jika pilihan setara/sama dengan opsi 1 maka output akan menampilkan langkah berikutnya yaitu
    #Input nilai dan mulai kalkulasi volume bola sesuai rumus
    if pilihan == 1:
        hitung_volume_bola()
    #Jika pilihan setara/sama dengan opsi 2 maka output akan menampilkan langkah berikutnya yaitu
    #Input nilai dan mulai kalkulasi volume tabung sesuai rumus
    elif pilihan == 2:
        hitung_volume_tabung()
    #Jika pilihan setara/sama dengan opsi 3 maka output akan menampilkan langkah berikutnya yaitu
    #Input nilai dan mulai kalkulasi volume limas segitiga sesuai rumus
    elif pilihan == 3:
        hitung_volume_limas()
    #Jika pilihan setara/sama dengan opsi 4 yang dimana itu akan mengarahkan pengguna keluar dari progam
    elif pilihan == 4:
        print("Terima kasih sampai jumpa kembali")
    #Jika pengguna salah memasukkan input (lebih dari atau kurang dari 1-4) maka akan gagal dan diminta mengulagi
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        main()

#Rumus hitungan volume bangun ruang dari bola, tabung, dan limas segitiga
def hitung_volume_bola():
    jari_jari = int(input("Masukkan jari-jari bola(cm): "))
    volume = (4/3) * 3.14 * (jari_jari ** 3)
    print("Volume bola adalah", volume)

def hitung_volume_tabung():
    jari_jari = int(input("Masukkan jari-jari tabung(cm): "))
    tinggi = int(input("Masukkan tinggi tabung(cm): "))
    volume = 3.14 * (jari_jari ** 2) * tinggi
    print("Volume tabung adalah", volume)

def hitung_volume_limas():
    alas = int(input("Masukkan panjang alas limas(cm): "))
    tinggi_alas = int(input("Masukkan tinggi alas limas(cm): "))
    tinggi_limas = int(input("Masukkan tinggi limas(cm): "))
    volume = (1/3) * alas * tinggi_alas * tinggi_limas
    print("Volume limas adalah", volume)


#Disini saya menggunakan instance yang dimana fungsinya mirip seperti operator perbandingan(comparasion)
#Namun yang dibandingkan di sini adlah 2 argument yang berbeda dimana name itu class dan main sebagai objek
if __name__ == "__main__":
    main()


print("Selesai.")
