class Caesar_cipher:
    def __init__(self,txt,language:str="en",mode="lower",task="encrypt"):
        self._txt=txt
        self._mode=mode
        self._language=language
        self._task=task
        self._plaintxt=""
        self._ciphertext=""
        if task=="encrypt":
            self._plaintxt=txt
        else:
            self._ciphertext=txt
    def encrypt(self,k=2,):
        try:
            if self._task=="decrypt":
                return self._ciphertext
            else:
                txt=self._txt
                if self._mode=="lower":
                    tmp="".join([chr((ord(i)-ord('a') + k) % 26 + ord('a')) for i in txt])
                elif self._mode=="upper":
                    tmp="".join([chr((ord(i)-ord('A') + k) % 26 + ord('a')) for i in txt])
        except BaseException:
            tmp="something wrong"
        if self._task=="encrypt":
            self._ciphertext=tmp
        return tmp
    def decrypt(self,k=2,language:str="en"):
        try:
            if self._task=="encrypt":
                return self._plaintxt
            else:
                txt=self._txt
                k=26-k
                if self._mode=="lower":
                    tmp="".join([chr((ord(i)-ord('a') + k) % 26 + ord('a')) for i in txt])
                elif self._mode=="upper":
                    tmp="".join([chr((ord(i)-ord('A') + k) % 26 + ord('a')) for i in txt])
        except BaseException:
            tmp="something wrong"
        if self._task=="decrypt":
            self._plaintxt=tmp
        return tmp
    def check(self):
        if self._task=="encrypt":
            return "Input is the plaintext"
        elif self._task=="decrypt":
            return "Input is the ciphertext"
        if self._plaintxt!="" and self._ciphertext!="" and self._txt!="":
            return"task over"
        else:
            return "task not over"
    def goal(self):
        if self._task=="encrypt":
            return self._ciphertext
        elif self._task=="decrypt":
            return self._plaintxt

































# a=caesar_cipher("iloveapple")
# print(a.encrypt())
# print(caesar_cipher(a.encrypt()).decrypt())
















































































