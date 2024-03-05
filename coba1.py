# memanggil/membangkitkan bilangan random integer
from random import randint as rnd


def comb(string,times):
    """ fungsi dengan 2 parameter string sebagai 'string' dan times sebagai
    'pangkat dari string' """
    
    # membuat array untuk menampung kombinasi
    arr=[]
    
    # melakukan perulangan dengan kondisi "selama panjang array tidak sama
    # dengan panjang string dipangkatkan 'pangkat' maka lakukan perintah di bawah
    # ini"
    while not (len(arr)==(len(string)**times)):
        
        # membuat variabel dummy yang akan menyimpan kombinasi dari string secara
        # random
        dummy = "".join([string[rnd(0,len(string)-1)] for _ in range(times)])
        
        # membuat kondisi agar tidak ada kombinasi berulang
        while dummy in arr:
            dummy = "".join([string[rnd(0,len(string)-1)] for _ in range(times)])
        
        # masukkan kombinasi yang sudah benar benar unik ke dalam array
        arr.append(dummy)
    
    # urutkan kombinasi string berdasarkan karakter secara 'ascending'
    arr.sort()
    
    # membuat variabel kosong untuk menyimpan hasil konversi array kombinasi
    # string ke string
    dummy = ""
    # melakukan perulangan untuk mengkonversi data dari array ke dalam string
    for i in range(len(string)**int(times/2)):
        # karena baris kode terlalu panjang, maka di turunkan dengan cara
        # menambahkan karakter backspace di akhir baris
        for j in range(int(((len(string)**times)/len(string)**int(times/2))*i), \
            int(((len(string)**times)/(len(string)**int(times/2)))*(i+1))):

            # tambahkan string dengan indeks tertentu ke string (konkatenasi)
            dummy += arr[j]+", "
        
        # tambahkan 'enter untuk mempercantik tampilan'
        dummy+="\n"
    
    # kembalikan variabel dummy
    return dummy
        
# main program
# ini akan memanggil fungsi comb(string,times) sebanyak 4 kali dengan parameter
# variabel 'i' dan variabel konstan 'ndra'
for i in range(1,5):
    print(f"E^{i}")
    print(comb("ndr", i))
    print()
    print()