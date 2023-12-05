def menghitung_kata():
    masukan_kata_kamu = input('Masukan Sebuah Kata: ')
    jadikan_list = masukan_kata_kamu.split()
    hitung_jumlah_kata = len(jadikan_list)
    print ('Jumlah Kalimat:', hitung_jumlah_kata)
    print ('Jumlah huruf:', len(masukan_kata_kamu))

menghitung_kata()