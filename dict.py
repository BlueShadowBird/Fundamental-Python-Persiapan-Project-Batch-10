# TIPE DATA DICTIONARY

kamus_eng_ind = {}
kamus_eng_ind['son'] = 'anak laki-laki'
kamus_eng_ind['daughter'] = 'anak perempuan'
kamus_eng_ind['mother'] = 'ibu'
kamus_eng_ind['father'] = 'bapak'

print(kamus_eng_ind)

print()

driver_gojek_information = {
    'tanggal': '2021-03-03',
    'driver_list': [
        {'name': 'eko', 'jarak': 30},
        {'name': 'budi', 'jarak': 10}
    ]
}

print(f"jarak driver pertama: {driver_gojek_information['driver_list'][0]['jarak']} meter")