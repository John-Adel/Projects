def encrypt(text, num):
    num %= 26
    encrypted_msg = []
    for i in range(len(text)):
        if num < 0:
            if 65 <= ord(text[i]) <= 90:
                encrypted_char = ord(text[i]) + num
                if encrypted_char < 65:
                    encrypted_char = 91 + (65 - encrypted_char)
                    encrypted_msg.append(chr(encrypted_char))
                else:
                    encrypted_msg.append(chr(encrypted_char))
            elif 97 <= ord(text[i]) <= 122:
                encrypted_char = ord(text[i]) + num
                if encrypted_char < 97:
                    encrypted_char = 123 + (97 - encrypted_char)
                    encrypted_msg.append(chr(encrypted_char))
                else:
                    encrypted_msg.append(chr(encrypted_char))
            else:
                encrypted_msg.append(text[i])
        elif num > 0:
            if 65 <= ord(text[i]) <= 90:
                encrypted_char = ord(text[i]) + num
                if encrypted_char > 90:
                    encrypted_char = 64 + (encrypted_char - 90)
                    encrypted_msg.append(chr(encrypted_char))
                else:
                    encrypted_msg.append(chr(encrypted_char))
            elif 97 <= ord(text[i]) <= 122:
                encrypted_char = ord(text[i]) + num
                if encrypted_char > 122:
                    encrypted_char = 96 + (encrypted_char - 122)
                    encrypted_msg.append(chr(encrypted_char))
                else:
                    encrypted_msg.append(chr(encrypted_char))
            else:
                encrypted_msg.append(text[i])
        else:
            return text
    return "".join(encrypted_msg)

print(f"Hello shifted by 5: {encrypt("Hello", 5)}\nOnce upon shifted by 5: {encrypt("Once upon", 5)}")