# 1. UraiRajutKata
# class UraiRajutKata:
#     def urai(self, kata):
#         self.kata = kata
#         hasil = ''
#         for s in range(len(kata)):
#             hasil += kata[:s+1]
#         return hasil

#     def Rajut(self, kata):
#         self.kata = kata
#         hasil = ''
#         i = 2
#         for a in range(len(kata)):
#             if kata[a] == kata[a]:
#                 hasil += kata[:a+1]
#                 continue
#             if kata[a+1] == kata[a+1]:
#                 hasil += kata[:a+1]
#                 continue
#             if kata[a+2] == kata[a+2]:
#                 hasil += kata[:a+1]
#                 continue
#             if kata[a+3] == kata[a+3]:
#                 hasil += kata[:a+1]
#                 continue
# x = UraiRajutKata()
# print(x.urai('Code'))
# print(x.urai('Python'))
# print(x.urai('Purwadhika'))

# 2. Segitiga Excel


# segitigaExcel('Purwadhika')
# segitigaExcel('Purwadhika Startup and Coding School @BSD')
# segitigaExcel('kode')
# segitigaExcel('kode python')
# segitigaExcel('Lintang')
# import xlsxwriter
# book = xlsxwriter.Workbook('ujiansoal2.xlsx')
# sheet = book.add_worksheet('Sheet1')


# z = ''
# b = 0
# a = 'Purwadhika'

# for i in range(4):
#     for j in range(i + 1):
#         z += a[b]
#         b += 1
#     z += '\n'
# print(z)

# 3. API


import requests
#akses GET API http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json #"36" : "BANTEN"   #"32" : "JAWA BARAT" 

# apikey = 'CLEnneF0dT2kb0LzVv0dOmUWKdBGU5KoXaCsD3zbWFCClulFRX3weYiOEaUudnGf'
url = 'http://raw.githubusercontent.com/LintangWisesa/Ujian_Fundamental_JCDS08/master/data/provinsi.json'
# cari = input('ketik nama provinsi: ')

# headers = {
#     'user-key': apikey
# }

data = requests.get(url)
kodeprov = data.json()
print(kodeprov)
