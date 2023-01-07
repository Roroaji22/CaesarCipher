def enkripsi(pesan):
    global text
    kunci = int(input('masukkan kunci : '))
    cipher=''
    for i in pesan:
        if i in text:
            j = text.find(i)
            j = (j + kunci)%100
            cipher = cipher+text[j]
        else :
            cipher = cipher + i

    return cipher

def dekripsi(cipher):
    global text
    kunci = int(input('masukkan kunci : '))
    pesan=''
    for i in cipher:
        if i in text:
            j = text.find(i)
            j = (j - kunci)%100
            pesan = pesan+text[j]
        else :
            pesan = pesan + i

    return pesan

import string 

text = string.printable

while True:
    pilih = int(input('1. Enkripsi\n2. Dekripsi\n3. Exit\n========================\nPilih : '))

    if pilih == 1:
        pesan = input('masukan Pesan : ') #plaintext
        print('Hasil Enkripsi :', enkripsi(pesan))
    elif pilih == 2:
        cipher = input('masukan Pesan : ') #ciphertext
        print('Hasil Dekripsi :', dekripsi(cipher))
    elif pilih == 3:
        break
    else:
        print('pilih 1 atau 2!')