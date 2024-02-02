import os
import time
import pyautogui as patg
import rsa 

class OpenVMware:
    click = lambda x,y : patg.doubleClick(x, y)
    write = lambda Txt : patg.write(Txt)
    sleep = lambda sec : time.sleep(sec)
    def __init__(self) -> None:
        pass
    def openvm(self):
        filepath = r"C:\Program Files (x86)\VMware\VMware Horizon View Client\vmware-view.exe"
        os.startfile(filepath)
    def openserver(self):
        X, Y = 555, 333
        patg.doubleClick(X, Y)
    def login(self):
        patg.doubleClick(1015, 590)
        time.sleep(1)
        P = "-510x-460x-190x170x-30x100x-190x170x210x-360x-340x-290x-480x"
        patg.write(decrypt(P))
        time.sleep(0.5)
        patg.doubleClick(1041, 658)
        time.sleep(1)
        patg.doubleClick(555, 333)
        time.sleep(3)
        patg.press("enter")
        time.sleep(1)
        P1 = "1234a@qwer"
        patg.write(P1)
        time.sleep(0.5)
        patg.press("enter")


    def running(self):
        self.openvm()
        time.sleep(2)
        self.openserver()
        time.sleep(2)
        self.login()
def encDec():
    txt = "123"
    publicKey, privateKey = rsa.newkeys(256)
    print(publicKey, privateKey)
    enctxt = rsa.encrypt(txt.encode(), publicKey)
    dectxt = rsa.decrypt(enctxt, privateKey).decode()
    print(enctxt, dectxt)
def encrypt(Text) -> str():
    lst = ""
    for x in Text:
        tmp = ord(x)
        tmp -= 100 
        lst = lst + str(tmp) + "0x"
    return lst
def decrypt(Enc) -> str():
    lst = Enc.split("0x")
    dec = ""
    for x in range(0, len(lst)-1):
        tmp = int(lst[x]) + 100
        dec += chr(tmp)
    return dec
if __name__ == "__main__":
    OpenVMware().running()


    
