#!/usr/bin/python3
from Crypto.Cipher import AES
from tkinter import *
import tkinter
from Crypto import Random

"""FIRST PART | DIFFIE - Hellman KEY EXCHANGE"""

"""
#input variables

primenum = int(input('Enter prime number:'))
#print(primenum)
generator = int(input('Enter generator:'))
#print(generator)



# secret keys of persons
secretkeyofAlice = int(input("Enter Alice's secret key:"))
secretkeyofBob = int(input("Enter Bob's secret key:"))
"""
#demo
primenum = 17
generator = 3
secretkeyofAlice = 15
secretkeyofBob = 13


#function for Diffie-Hellman
#PublicKeyExchange

publicKeyofAlice = (generator ** secretkeyofAlice) % primenum
print("Public Key of Alice",publicKeyofAlice)
publicKeyofBob = (generator ** secretkeyofBob) % primenum
print("Public Key of Bob",publicKeyofBob)

#sharedkeys

SecretKeyofAlice = (publicKeyofBob ** secretkeyofAlice) % primenum
SecretKeyofBob = (publicKeyofAlice ** secretkeyofBob) % primenum

print("Secret Key of Alice", SecretKeyofAlice)
print("Secret Key of Bob", SecretKeyofBob)

print("\n")
if SecretKeyofBob == SecretKeyofAlice:
    print("Common secure key is:",SecretKeyofBob)


""" SECOND PART - CIPHER BLOCK CHAINING MODE OVER AES ALGORITHM"""

#AES IMPLEMENTATION

keyinAES = secretkeyofBob
print("\n")
plaintext = input("Enter plain text for encryption:")

print("\n")
#print("Your plaintext is:", plaintext)



def QuittheApplication():
        CrptoGUI.destroy()
        return

def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(plaintext, keyinAES, key_size = 192):
    message = pad(plaintext)
    IV = Random.new().read(AES.block_size)
    cipher = AES.new(keyinAES, AES.MODE_CBC, IV)
    return IV + cipher.encrypt(plaintext)


CrptoGUI = tkinter.Tk()
CrptoGUI.title("Homework 2 by Nijat Mursali")
CrptoGUI.minsize(width=300, height= 300)
CrptoGUI.maxsize(width=400, height=400)
CrptoGUI.configure(background = 'red')



LabelforTeam = Label(CrptoGUI, text = 'This is the project of Team 6(I think)', relief = 'raise')
LabelforBoshluq = Label(CrptoGUI, text = '\n', relief = 'raise')
LabelforPrimeNumber = Label(CrptoGUI, text = 'Enter the prime number:')
LabelforGenerator = Label(CrptoGUI, text = '   Enter the generator:     ', padx = 2, pady = 2)
LabelforPublicKeyAlice  = Label(CrptoGUI, text = 'Enter Public Key of Alice:')
LabelforPublicKeyBob  = Label(CrptoGUI, text = 'Enter Public Key of Bob: ', padx = 2, pady = 2)

EntryforPrimeNumber = Entry(CrptoGUI)
EntryforGenerator = Entry(CrptoGUI)
EntryforPublicKeyAlice = Entry(CrptoGUI)
EntryforPublicKeyBob = Entry(CrptoGUI)

LabelforTeam.grid(columnspan = 2)
LabelforPrimeNumber.grid(row = 2, column = 0, sticky = W)
LabelforGenerator.grid(row = 3, column = 0, sticky = W)
LabelforPublicKeyAlice.grid(row =4, column = 0, sticky = W)
LabelforPublicKeyBob.grid(row = 5, column = 0, sticky = W)

EntryforPrimeNumber.grid(row = 2, column = 1)
EntryforGenerator.grid(row = 3, column = 1)
EntryforPublicKeyAlice.grid(row = 4, column =1)
EntryforPublicKeyBob.grid(row = 5, column = 1)

ButtonforEncrpytion = Button(CrptoGUI, text = "Encrpyt", command = encrypt)
ButtonforEncrpytion.grid(columnspan = 2)
ButtonforQuit = Button(CrptoGUI, text = "Quit", command = QuittheApplication)
ButtonforQuit.grid(columnspan = 3)

CrptoGUI.mainloop()
