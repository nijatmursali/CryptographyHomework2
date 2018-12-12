"""

This is the application that's created by Nijat Mursali(ADA BCS 2019)
This application is created by using Tkinter GUI.
If we talk about the program itself, it has 2 parts: first one is about implementing the DH key exchange
and the second part is about implementing AES with CBC Mode.
I added AES library by using the pycrypto(you can install simply by typing "pip install pycrypto"
                                         (however Linux and Mac has the libraries installed))

#DH key exchange
I used GUI with this so the input will be added by the user by using .get() from input.
                         After getting input the calculations for Bob and Alice starts.

#AES with CBC Mode

In Encrpt method I simply call the result that we got from DH method and encrypt with IV
(I took IV randomly, however key is from KeyExchange method and user inputs the plaintext.)

And finally CrptoGUI is for implementing Tkinter for GUI.

"""


#!/usr/bin/python3
from Crypto.Cipher import AES
from tkinter import *
import tkinter
from Crypto import Random

result=[]
def KeyExchange():
    for res in result:
        res.destroy()
    try:
        InputPrimeNumber=int(EntryforPrimeNumber.get()) #input for prime number
        InputGenerator=int(EntryforGenerator.get()) #input for generator
        InputPublicKeyofAlice=int(EntryforPublicKeyAlice.get()) #input for key of Alice
        InputPublicKeyofBob=int(EntryforPublicKeyBob.get()) #input for key of Bob
        #InputforPlainText = int(EntryforAddingPlainText.get())
        output1=''
        output2=''

    except:
        LabelforResult = Label(CrptoGUI, text ='Enter an positive integer!' ) #if there's no integer included, this text will pop up
        LabelforResult.grid(row = 15, sticky = W) #on 15th row


    #Function for DH
    Alice = (InputGenerator ** InputPublicKeyofAlice) % InputPrimeNumber
    Bob = (InputGenerator ** InputPublicKeyofBob) % InputPrimeNumber

    FinalAnswerforAlice = (Bob ** InputPublicKeyofAlice) % InputPrimeNumber
    FinalAnswerforBob = (Alice ** InputPublicKeyofBob) % InputPrimeNumber

    LabelforDH = Label(CrptoGUI, text = FinalAnswerforAlice)
    LabelforDH.grid(row = 6, column = 1,  sticky = W )
    result.append(LabelforDH)
    return FinalAnswerforAlice

def KeyExch():
    #global plaintext
    #global firstfirst
    KeyExchange()


def QuittheApplication():
        CrptoGUI.destroy()
        return

res = []
def Encrpt():
    InputforPlainText = EntryforAddingPlainText.get()
    for re in res:
        re.destroy()

    #AES = KEY, MODE, IV
    get_bin = lambda x, n: format(x, 'b').zfill(n)

    IV = Random.new().read(16) #IV will be random value with 16 bytes
    keyfromDH =get_bin(KeyExchange(),16).encode("utf8") #key comes from DH(KeyExch that I created above)
    f=((len(InputforPlainText)+15)//16)*16
    plaintextfromuser = InputforPlainText.rjust(f, '0').encode("utf8") #should be encoded because I'm using windows..
    ciphertext = AES.new(keyfromDH, AES.MODE_CBC, IV) #encrpytion
    encrpytedmessage = IV + ciphertext.encrypt(plaintextfromuser)

    LabelforEncryptedText = Label(CrptoGUI, text = encrpytedmessage)
    LabelforEncryptedText.grid(row = 10, column = 1,  sticky = W )
    res.append(LabelforEncryptedText)

#End of Functions


#Python GUI

#Menu
CrptoGUI = tkinter.Tk()
CrptoGUI.title("Homework 2 by Nijat Mursali")
CrptoGUI.minsize(width=350, height= 300)
CrptoGUI.maxsize(width=350, height=300)
CrptoGUI.configure(background = 'grey')

#Labels
LabelforTeam = Label(CrptoGUI, text = 'This is the project of Team 5.', relief = 'raise')
LabelforBoshluq = Label(CrptoGUI, text = '\n', relief = 'raise')
LabelforPrimeNumber = Label(CrptoGUI, text = 'Enter the prime number:')
LabelforGenerator = Label(CrptoGUI, text = '   Enter the generator:     ', padx = 2, pady = 2)
LabelforPublicKeyAlice  = Label(CrptoGUI, text = 'Enter Public Key of Alice:')
LabelforPublicKeyBob  = Label(CrptoGUI, text = 'Enter Public Key of Bob: ', padx = 2, pady = 2)
LabelforAddingPlainText  = Label(CrptoGUI, text = 'Enter the Plain Text: ', padx = 2, pady = 2)
LabelforDH = Label(CrptoGUI, text = 'Result of the DH')
LabelforEncryptedText = Label(CrptoGUI, text = 'Result of the Encryption:')

EntryforPrimeNumber = Entry(CrptoGUI)
EntryforGenerator = Entry(CrptoGUI)
EntryforPublicKeyAlice = Entry(CrptoGUI)
EntryforPublicKeyBob = Entry(CrptoGUI)
EntryforAddingPlainText = Entry(CrptoGUI)


LabelforTeam.grid(columnspan = 2)
LabelforPrimeNumber.grid(row = 2, column = 0, sticky = NSEW)
LabelforGenerator.grid(row = 3, column = 0, sticky = NSEW)
LabelforPublicKeyAlice.grid(row =4, column = 0, sticky = NSEW)
LabelforPublicKeyBob.grid(row = 5, column = 0, sticky = NSEW)
LabelforDH.grid(row =6, column = 0, sticky =NSEW)
LabelforAddingPlainText.grid(row = 7, column = 0, sticky = NSEW)
LabelforAddingPlainText.grid(row = 8, column = 0, sticky =NSEW)
#LabelforResult.grid(row = 9, column = 0, sticky = W)
LabelforEncryptedText.grid(row = 10, column = 0, sticky = NSEW)

EntryforPrimeNumber.grid(row = 2, column = 1)
EntryforGenerator.grid(row = 3, column = 1)
EntryforPublicKeyAlice.grid(row = 4, column =1)
EntryforPublicKeyBob.grid(row = 5, column = 1)
EntryforAddingPlainText.grid(row = 8, column = 1)


ButtonforDH = Button(CrptoGUI, text = "Diffie-Hellman Key Exchange", command = KeyExch)
ButtonforDH.grid(columnspan = 2)
ButtonforEncrpytion = Button(CrptoGUI, text = "Encryption", command = Encrpt)
ButtonforEncrpytion.grid(columnspan = 3)
ButtonforQuit = Button(CrptoGUI, text = "Quit", command = QuittheApplication)
ButtonforQuit.grid(columnspan = 4)



CrptoGUI.mainloop()
