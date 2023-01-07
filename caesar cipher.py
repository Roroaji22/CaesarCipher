import string 

text = string.printable

def encrypt(isi):
    global text
    key = int(input('masukkan kunci : '))
    cipher=''
    for i in isi:
        if i in text:
            k = text.find(i)
            k = (k + key)%100
            cipher = cipher+text[k]
        else :
            cipher = cipher + i

    return cipher

def decrypt(cipher):
    global text
    key = int(input('masukkan kunci : '))
    isi=''
    for i in cipher:
        if i in text:
            k = text.find(i)
            k = (k - key)%100
            isi = isi+text[k]
        else :
            isi = isi + i

    return isi

while True:
    print('============================================')
    print('---------Kriptografi Caesar Cipher---------')
    print('program enkripsi dekripi menggunakan python')
    print('============================================')
    pilih = int(input('1. Enkripsi\n2. Dekripsi\n========================================\nPilih : '))

    if pilih == 1:
        isi = input('masukan isi : ') #plaintexy
        print(encrypt(isi))
    elif pilih == 2:
        cipher = input('masukan isi : ') #ciphertext
        print(decrypt(cipher))
    else:
        print('pilih 1 atau 2!')