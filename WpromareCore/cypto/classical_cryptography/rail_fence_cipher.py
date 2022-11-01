class Rail_fence_cipher:
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
    def set_txt(self,txt):
        self._txt=txt
        if self._task=="encrypt":
            self._plaintxt=txt
        else:
            self._ciphertext=txt
    def get_txt(self):
        return self._txt
    def set_task(self,task):
        self._task=task
    def get_task(self):
        return self._task
    def encrypt(self,k=2,):
        try:
            if self._task=="decrypt":
                return self._ciphertext
            else:
                txt=self._txt
                tmp=""
                for i in range(int(k)):
                    for j in range(int(txt.__len__() / k + 0.5)):
                        try:
                            tmp += txt[j * k+ i]
                        except:
                            pass
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
class brute_force_for_Caesar:
    def __init__(self,Ccipher:Rail_fence_cipher):
        self._Ccipher=Ccipher
        self._result=""
        self._result_li=[]
    def process(self):
        res_li=[]
        if self._Ccipher.get_task()=="decrypt":
            txt="the brute force will start\n"
            for i in range(1,27):
                res_li.append([i,self._Ccipher.decrypt(i)])
                txt+="k="+str(i)+", result="+self._Ccipher.decrypt(i)+"\n"
            self._result=txt
            self._result_li=res_li
    def get_result_print(self):
        return self._result
    def get_result_li(self):
        return self._result_li


def fence_Passwd_encode():
    string = input('请输入需要加密的明文：')
    num = int(input('请输入栅栏数(密钥)：'))
    res = ''
    for i in range(int(num)):
        # 遍历循环输出结果
        for j in range(int(string.__len__() / num + 0.5)):
            # print(j)
            try:
                res += string[j * num + i]
            except:
                pass
    print(res)


if (__name__ == '__main__'):
    fence_Passwd_encode()

































# a=caesar_cipher("iloveapple")
# print(a.encrypt())
# print(caesar_cipher(a.encrypt()).decrypt())
















































































