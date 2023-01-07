def encode(kalimat,cipher_key):
  kalimat = kalimat.lower()
  hasil_encode = ''
  for karakter in kalimat:
    if karakter in abjad:
      index_lama = abjad.index(karakter)
      index_baru = (index_lama + cipher_key ) % len(abjad)
      abjad_baru = abjad[index_baru]
      hasil_encode = hasil_encode + abjad_baru 
    else:
       hasil_encode = hasil_encode + ' ' 
  return hasil_encode

import string 

text = string.printable
abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print('============================================')
print('program enkripsi dekripi menggunakan python')
print('============================================')
while True:
    pilih = int(input('1. Enkripsi\n2. Dekripsi\n3. Exit\n========================================\nPilih : '))

    if pilih == 1:
        key = int(input('Masukkan key: '))
        kalimat = input('masukan Pesan : ') #plaintext
        kalimat_hasil = encode(kalimat,key)
        print('Kalimat yang dimasukkan adalah:',kalimat)
        print('Hasil enkripsi kalimat menggunakan Caesar Cipher dengan key:',key, 'adalah', kalimat_hasil)
    elif pilih == 2:
        kalimat_awal = encode(kalimat_hasil,-key)
        print('Jika hasil dienkripsi ulang menggunakan nilai negatif dari cipher key sebelumnya maka kalimat hasilnya adalah:',-key, 'adalah, ', kalimat_awal)
    elif pilih == 3:
        break
    else:
        print('pilih 1 atau 2!')