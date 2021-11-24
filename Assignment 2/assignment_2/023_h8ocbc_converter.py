import msvcrt as m
import os

def Menu():
    print("Menu")
    print("1. Merubah suhu dari kelvin ke celcius atau celcius ke kelvin ")
    print("2. Merubah suhu dari kelvin atau celcius ke fahrenheit")
    print("3. Merubah suhu dari fahrenheit ke kelvin atau celcius")
    print("0. Exit")
    print("Choose : ")

def kelvin(temp, unit):
    '''
    Fungsi ini berguna untuk merubah suhu dari kelvin ke celcius atau dari celcius ke kelvin
    :param temp: Input berupa suhu | input berupa int
    :param unit: Input berupa satuan dari suhu untuk di convert apakah kelvin untuk dijadikan celcius atau celcius ke kelvin tergantung satuannya | input berupa string
    '''  
    if unit == 'kelvin':
        total = temp - 273
        print("suhu dari {0} °K menjadi ke {1} °C".format(temp,total))
    elif unit == 'celcius':
        total = temp + 273
        print("suhu dari {0} °C menjadi ke {1} °K".format(temp,total))

def toFahrenheit(temp, unit):
    '''
    Fungsi ini berguna untuk merubah suhu dari kelvin atau celcius menjadi fahrenheit tergantung pada satuan yang dipilih
    :param temp: Input berupa suhu | input berupa int
    :param unit: Input berupa satuan dari suhu untuk di convert menjadi fahrenheit dari kelvin/celcius | input berupa string
    ''' 
    if unit == 'kelvin': # convert from kelvin to fahrenheit
        total = (((temp - 273) * 9) / 5) + 32
        print("suhu dari {0} °K menjadi ke {1} °F".format(temp, total))
    elif unit == 'celcius': #convert from kelvin to celcius
        total = ((9*temp)/5) + 32
        print("suhu dari {0} °C menjadi ke {1} °F".format(temp, total))

def fromFahrenheit(temp, unit):
    '''
    Fungsi ini berguna untuk merubah suhu dari fahrenheit menjadi celcius atau kelvin tergantung pada satuan yang dipilih
    :param temp: Input berupa suhu | input berupa int
    :param unit: Input berupa satuan dari suhu untuk di convert dari fahrenheit menjadi kelvin/celcius | input berupa string
    '''
    if unit == 'kelvin': #convert from fahrenheit to kelvin
        total = ((temp - 32) *5 )/9 +273
        print("suhu dari {0} °F menjadi ke {1} °K".format(temp,total))
    elif unit == 'celcius': #convert from fahrenheit to celcius
        total = ((temp - 32) *5 )/9
        print("suhu dari {0} °F menjadi ke {1} °C".format(temp,total))

clear = lambda: os.system('cls')
Menu()
choose =  0
while choose > -1:
    choose = int(input())
    if(choose == 1):
        print("Masukkan suhu : ")
        suhu = int(input())
        print("Masukkan satuan suhu (kelvin atau celcius)") #menentukan suhu apakah kelvin atau celcius untuk menentukkan perubahan dari kelvin ke celcius atau celcius ke kelvin
        satuan = input()
        kelvin(suhu, satuan)
        print(kelvin.__doc__)
        print("press any key to continue...")
        m.getch()
        clear()         
        Menu()
    elif(choose == 2):
        print("Masukkan suhu : ")
        suhu = int(input())
        print("Masukkan suhu fahrenheit akan di convert menjadi apa(dari fahrenheit ke kelvin atau celcius)") #menentukkan satuan suhu yang akan di convert dari fahrenheit menjadi ke kelvin atau celcius
        satuan = input()
        toFahrenheit(suhu, satuan)
        print(toFahrenheit.__doc__)
        print("press any key to continue...")
        m.getch()   
        clear()               
        Menu()
    elif(choose == 3):
        print("Masukkan suhu  : ")
        suhu = int(input())
        print("Masukkan satuan suhu dari fahrenheit menjadi ke (celcius atau kelvin)") #menentukkan satuan suhu apakah kelvin atau celcius yang kemudian di convert menjadi fahrenheit
        satuan = input()
        fromFahrenheit(suhu, satuan)
        print(fromFahrenheit.__doc__)
        print("press any key to continue...")
        m.getch()
        clear()         
        Menu()
    elif(choose == 0):
        break
#float(temp) ==> untuk konversi menjadi float