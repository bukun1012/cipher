def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message:
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index % len(key)].lower()
            key_index += 1

            offset = alphabet.index(key_char)
            index = alphabet.index(char.lower())
            new_index = (index + offset * direction) % len(alphabet)
            # 保持原大小寫
            transformed_char = alphabet[new_index].upper() if char.isupper() else alphabet[new_index]
            final_message += transformed_char
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)

def decrypt(message, key):
    return vigenere(message, key, -1)

# 用戶輸入
text = input("Enter the text to encrypt/decrypt: ")
custom_key = input("Enter the encryption key: ")

if not custom_key.isalpha():
    raise ValueError("Key must contain only alphabetic characters.")

# 執行加密與解密
encrypted_text = encrypt(text, custom_key)
decrypted_text = decrypt(encrypted_text, custom_key)

print(f"\nOriginal text: {text}")
print(f"Encrypted text: {encrypted_text}")
print(f"Decrypted text: {decrypted_text}")
