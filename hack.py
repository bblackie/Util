import operator

'''
cvpbPGS" is an example of a message encoded with the ROT13 cipher, a simple substitution cipher used in cryptography. ROT13 stands for "rotate by 13 places" and shifts each letter of the plaintext alphabet by 13 places. This cipher is unique because it is its own inverse; applying ROT13 to the ciphertext will return the original plaintext.

For example, if you encode "HELLO" using ROT13, it becomes "URYYB." Decoding "URYYB" using ROT13 brings you back to "HELLO"​ (GitHub)​​ (GitHub)​​ (Boxentriq)​​ (dCode)​.

The text "cvpbPGS" can be decoded as "picoCTF" using ROT13. This method is often used in online puzzles and Capture the Flag (CTF) competitions to hide hints or solutions from plain sight​ (GitHub)​​ (ciphereditor)​.

'''

ROT_CIPHER = 13
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z']


encode_msg = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}"


test_msg = "hello"


def rot(msg, rot_cipher, encrypt):

    rotated = ""


    for c in msg:
        
        rot_index = (alphabet.index(c) + rot_cipher) % 26
        
        rotated += alphabet[rot_index]
    
    return rotated


encrypted = rot("cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_uJdSftmh}", 13, False)
#encrypted = rot("hello", 13, True)
print(encrypted)

decrypted = rot(encrypted, -13, True)

print(decrypted)

    
