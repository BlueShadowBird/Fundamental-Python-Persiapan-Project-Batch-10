# PERULANGAN
jumlah_anak = 4
for index_anak in range(1,jumlah_anak+1):
    print(f'Hallo anak #{index_anak}')

# DATA LIST
anak = ['Toro', 'Dede', 'Faisyal', 'Ayu']


# CARA 1
print('CARA 1')
print(anak[0])
print(anak[1])
print(anak[2])
print(anak[3])

# CARA 2
print('CARA 2')
for nama_anak in anak:
    print(f'Hallo #{nama_anak}')

print('CARA 3')
for index_anak in range(0, len(anak)):
    print(f'Hallo #{anak[index_anak]}')