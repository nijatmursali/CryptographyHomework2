#!/usr/bin/python3
from Crypto.Cipher import AES
from tkinter import *
import tkinter
from Crypto import Random

"""
FIRST PART | DIFFIE - Hellman KEY EXCHANGE
#input variables
primenum = int(input('Enter prime number:'))
#print(primenum)
generator = int(input('Enter generator:'))
#print(generator)
# secret keys of persons
secretkeyofAlice = int(input("Enter Alice's secret key:"))
secretkeyofBob = int(input("Enter Bob's secret key:"))


#demo
primenum = 17
generator = 3
secretkeyofAlice = 15
secretkeyofBob = 13


#function for Diffie-Hellman
#PublicKeyExchange
publicKeyofAlice = (generator ** secretkeyofAlice) % primenum
#print("Public Key of Alice",publicKeyofAlice)
publicKeyofBob = (generator ** secretkeyofBob) % primenum
#print("Public Key of Bob",publicKeyofBob)

#sharedkeys

SecretKeyofAlice = (publicKeyofBob ** secretkeyofAlice) % primenum
SecretKeyofBob = (publicKeyofAlice ** secretkeyofBob) % primenum

#print("Secret Key of Alice", SecretKeyofAlice)
#print("Secret Key of Bob", SecretKeyofBob)

print("\n")
#if SecretKeyofBob == SecretKeyofAlice:
    #print("Common secure key is:",SecretKeyofBob)
"""

def Encrpt():
    InputforPlainText = int(EntryforAddingPlainText.get())

    #AES = KEY, MODE, IV
    IV = Random.new().read(16)
    key = firstfirst

    cipher = AES.new(key, AES.MODE_CBC, IV)
    msg = IV + cipher.encrypt(InputforPlainText)

    LabelforEncryptedText = Label(CrptoGUI, text = msg)
    LabelforEncryptedText.grid(row = 10, column = 1,  sticky = W )
    result.append(LabelforEncryptedText)

result=[]
def KeyExchange():
    for res in result:
        res.destroy()
    try:
        InputPrimeNumber=int(EntryforPrimeNumber.get())
        InputGenerator=int(EntryforGenerator.get())
        InputPublicKeyofAlice=int(EntryforPublicKeyAlice.get())
        InputPublicKeyofBob=int(EntryforPublicKeyBob.get())
        InputforPlainText = int(EntryforAddingPlainText.get())
        output1=''
        output2=''

    except:
        LabelforResult = Label(CrptoGUI, text ='Enter an positive integer!' )
        LabelforResult.grid(row = 13, sticky = W)


    #Function for DH
    first = (InputGenerator ** InputPublicKeyofAlice) % InputPrimeNumber
    second = (InputGenerator ** InputPublicKeyofBob) % InputPrimeNumber

    firstfirst = (second ** InputPublicKeyofAlice) % InputPrimeNumber
    secondsecond = (first ** InputPublicKeyofBob) % InputPrimeNumber

    LabelforDH = Label(CrptoGUI, text = firstfirst)
    LabelforDH.grid(row = 6, column = 1,  sticky = W )
    result.append(LabelforDH)

def KeyExch():
    #global plaintext
    #global firstfirst
    KeyExchange()


def QuittheApplication():
        CrptoGUI.destroy()
        return

#End of Functions


#Python GUI

#Menu
CrptoGUI = tkinter.Tk()
CrptoGUI.title("Homework 2 by Nijat Mursali")
CrptoGUI.minsize(width=300, height= 300)
CrptoGUI.maxsize(width=400, height=400)
CrptoGUI.configure(background = 'red')

#Labels
LabelforTeam = Label(CrptoGUI, text = 'This is the project of Team 6(I think)', relief = 'raise')
LabelforBoshluq = Label(CrptoGUI, text = '\n', relief = 'raise')
LabelforPrimeNumber = Label(CrptoGUI, text = 'Enter the prime number:')
LabelforGenerator = Label(CrptoGUI, text = '   Enter the generator:     ', padx = 2, pady = 2)
LabelforPublicKeyAlice  = Label(CrptoGUI, text = 'Enter Public Key of Alice:')
LabelforPublicKeyBob  = Label(CrptoGUI, text = 'Enter Public Key of Bob: ', padx = 2, pady = 2)
LabelforAddingPlainText  = Label(CrptoGUI, text = 'Enter the Plain Text: ', padx = 2, pady = 2)
LabelforResult = Label(CrptoGUI, text = 'Result of the Cipher')
LabelforDH = Label(CrptoGUI, text = 'Result of the DH')
LabelforEncryptedText = Label(CrptoGUI, text = 'Result of the Encryption:')

EntryforPrimeNumber = Entry(CrptoGUI)
EntryforGenerator = Entry(CrptoGUI)
EntryforPublicKeyAlice = Entry(CrptoGUI)
EntryforPublicKeyBob = Entry(CrptoGUI)
EntryforAddingPlainText = Entry(CrptoGUI)


LabelforTeam.grid(columnspan = 2)
LabelforPrimeNumber.grid(row = 2, column = 0, sticky = W)
LabelforGenerator.grid(row = 3, column = 0, sticky = W)
LabelforPublicKeyAlice.grid(row =4, column = 0, sticky = W)
LabelforPublicKeyBob.grid(row = 5, column = 0, sticky = W)
LabelforDH.grid(row =6, column = 0, sticky =W)
LabelforAddingPlainText.grid(row = 7, column = 0, sticky = W)
LabelforAddingPlainText.grid(row = 8, column = 0, sticky =W)
LabelforResult.grid(row = 9, column = 0, sticky = W)
LabelforEncryptedText.grid(row = 10, column = 0, sticky = W)

EntryforPrimeNumber.grid(row = 2, column = 1)
EntryforGenerator.grid(row = 3, column = 1)
EntryforPublicKeyAlice.grid(row = 4, column =1)
EntryforPublicKeyBob.grid(row = 5, column = 1)
EntryforAddingPlainText.grid(row = 8, column = 1)


ButtonforDH = Button(CrptoGUI, text = "DH", command = KeyExch)
ButtonforDH.grid(columnspan = 2)
ButtonforEncrpytion = Button(CrptoGUI, text = "Encryption", command = Encrpt)
ButtonforEncrpytion.grid(columnspan = 3)
ButtonforQuit = Button(CrptoGUI, text = "Quit", command = QuittheApplication)
ButtonforQuit.grid(columnspan = 4)

CrptoGUI.mainloop()
