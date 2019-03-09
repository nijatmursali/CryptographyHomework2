# CryptographyHomework2
This is to implement BlockChainingMode for AES and DH

This is the application that's created by Nijat Mursali(ADA BCS 2019)

This application is created by using Tkinter GUI.

If we talk about the program itself, it has 2 parts: first one is about implementing the DH key exchange

and the second part is about implementing AES with CBC Mode.

I added AES library by using the pycrypto(you can install simply by typing "pip install pycrypto"
(however Linux and Mac has the libraries installed))

#DH key exchange

I used GUI with this so the input will be added by the user by using .get() from input. After getting input the calculations for Bob and Alice starts.



#AES with CBC Mode



In Encrpt method I simply call the result that we got from DH method and encrypt with IV

(I took IV randomly, however key is from KeyExchange method and user inputs the plaintext.)



And finally CrptoGUI is for implementing Tkinter for GUI.

