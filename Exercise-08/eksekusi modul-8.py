'''#Metode capitalize()
str = "hello world"
s = str.capitalize()
print(s) #output: Hello world'''

'''#metode center()
str = "Hello world"
s = str.center(20, '*')
print(s) #output: ****Hello World****
s = str.center(19, '*')
print(s) #output: ****Hello World****
print()'''

'''#metode count
str = "Hello World"
s = str.count('l')
print(s) #output: 3
s = str.count('l', 0, 3) #menghitung jumlah substring "l" antara indeks ke-0 "H" hingga indeks ke-3 "l"
print(s) #output: 1
s = str.count('l', 0, len(str)) #menghitung jumlah substring 'l' dari indeks awal (indeks ke-0) hingga akhir
print(s) #output: 3
s = str.count('h')
print(s) #output: 0'''

'''#metode endswith()
str = "Hello World"
s = str.endswith('World')
print(s) #output: true
s = str.endswith('world')
print(s) #output: False
s = str.endswith('lo', 0, 4)#memeriksa string str dari indkes ke-0 sampai ke-4 diakhiri oleh substr 'lo' atau tidak
print(s) #output: False
s = str.endswith('lo', 0, 5)#memeriksa string str dari indkes ke-0 sampai ke-5 diakhiri oleh substr 'lo' atau tidak
print(s) #output: True'''

'''#metode find()
str = "Hello World"
s = str.find('World')
print(s) #output: 6
s = str.find('world')
print(s) #output: -1, kl ga ketemu outputnya emg -1
s = str.find('o', 0, 4)#memeriksa substring 'o' pd string str dari indkes ke-0 sampai ke-4
print(s) #output: -1
s = str.find('o', 0, 5)#memeriksa substring 'o' pd string  str dari indkes ke-0 sampai ke-5
print(s) #output: 4'''

'''#metode index()
str = "Hello World"
s = str.index('World')
print(s) #output: 6
s = str.index('world')
print(s) #output: error, kl ga ketemu outputnya emg error bakal stuck, yg dibawah sini gakebaca
s = str.index('o', 0, 4)#memeriksa substring 'o' pd string str dari indkes ke-0 sampai ke-4
print(s) #output: error
s = str.index('o', 0, 5)#memeriksa substring 'o' pd string  str dari indkes ke-0 sampai ke-5
print(s) #output: 4'''

'''#metode replace()
str = "Hello World"
replace1 = str.replace('Hello', 'Hai') #(old, new) ada juga (old, new, count)
print(replace1) #output: Hai World
replace1 = replace1.replace('World', 'Dunia')
print(replace1) #output: Hai Dunia
replace2 = str.replace('l', 'i')
print(replace2) #output: Heiio Worid
replace2 = str.replace('l', 'i', 1) #1 itu count, jumlah maks yg bakal direplace
print(replace2) #output: Heilo World'''

#metode upper() dan lower()
str = "Hello World"
s = str.upper()
print(s) #outpu: HEELO WORLD
s = str.lower()
print(s) #output: hello world
