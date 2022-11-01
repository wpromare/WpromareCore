from cypto.classical_cryptography.caesar_cipher import Caesar_cipher,brute_force_for_Caesar
a=Caesar_cipher(txt="jgnnq",task="decrypt")
b=brute_force_for_Caesar(a)
b.process()
print(b.get_result_li())

