# Nama, Hobi, Sosmed, Lagu favorit,dan  Makanan favorit

dict = {'Nama'           : 'salsabila putri regina',
        'Hobi'           : ['streaming netflix','makan','rebahan'],
        'Sosmed'         : {'IG' : 'sasareginaa', 'line' : 'salsabila123456', 'twitter' : 'sasareginaa'},
        'Lagu favorit'   : ['mawar jingga','serta mulia','still into you'],
        'Makanan favorit': ['sate padang','bakso','soto']}

print ('Nama     :', dict['Nama'])
print ('Line     :', dict['Sosmed'].get('Line'))
print ('IG       :', dict['Sosmed'].get('IG'))
print ('Twiter   :', dict['Sosmed'].get('Twitter'))
print (*dict['Lagu favorit'], sep= ",")
print (*dict['Makanan favorit'], sep= ",")

# Mengubah salah satu hobi dan sosmed

dict['Hobi'][1] = 'nonton youtube'
dict['Sosmed']['IG2'] = 'doublesaa'

# Menghapus 2 makanan favorit

del dict['Makanan favorit'][0]
del dict['Makanan favorit'][1]


# Menambahkan 1 hobi

dict['Hobi'].append('scroll ig')
print (*dict['Hobi'], sep= ",")
print (dict)