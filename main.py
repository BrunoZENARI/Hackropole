def vigenere(c, cle):
    indice_cle = 0
    msg_code = ""

    for i in range(0, len(c)):
        if 'A' <= c[i] <= 'Z':
            msg_code += chr((((ord(c[i]) - ord('A')) +(ord(cle[indice_cle]) - ord('A'))) % 26) + ord('A'))
            indice_cle = (indice_cle + 1) % len(cle)
        else:
            msg_code += c[i]
    return msg_code


def decode_vigenere(c, cle):
    indice_cle = 0
    msg_code = ""

    for i in range(0, len(c)):
        if 'A' <= c[i] <= 'Z':
            msg_code += chr((((ord(c[i]) - ord('A')) - (ord(cle[indice_cle]) - ord('A'))) % 26) + ord('A'))
            indice_cle = (indice_cle + 1) % len(cle)
        else:
            msg_code += c[i]
    return msg_code


print(decode_vigenere('Gqfltwj emgj clgfv  Aqltj rjqhjsksg ekxuaqs ua xtwk n feuguvwb gkwp xwj ujts f npxkqvjgw nw tjuwcz ugwygjtfkf qz uw efezg sqk gspwonu  Jgsfwb aqmu f Pspygk nj  cntnn hqzt dg igtwy fw xtvjg rkkunqf'.upper(), 'FCSC'))