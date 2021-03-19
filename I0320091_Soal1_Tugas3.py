#list nama 10 teman
teman_sasa = ['rara', 'ryan', 'ano', 'stefany', 'naufal', 'funny', 'vizal', 'tazkia', 'alvin', 'attar']

#Tampilkanlah isi list indeks nomor 4,6,7.
print("list indeks nomor 4,6,7 yaitu", teman_sasa[4], "," , teman_sasa[6], ",dan",  teman_sasa[7])

#Gantilah nama teman mu yang berada di list 3,5,9
teman_sasa[3] = 'odrey'
teman_sasa[5] = 'dinda'
teman_sasa[9] = 'nadia'

#tambah 2 nama teman
teman_sasa.append ('cecen')
teman_sasa.append ('regina')

#Tampilkan semua teman kamu dengan perulangan
print (teman_sasa)

#Tampilkan panjang list
print (len(teman_sasa))