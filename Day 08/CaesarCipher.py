def encrypted(i):
    return chr(ord(i)+4)
def encrypt(word):
    new_word = ""
    for i in range(0,len(word)-1) :
        new_word += encrypted(word[i]) 
    return new_word

def decrypt(word):
    for i in word:
        i = decrypted(i)
    return word

print(encrypt("adarsh"))
