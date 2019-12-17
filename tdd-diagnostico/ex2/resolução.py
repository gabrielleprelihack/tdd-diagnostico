def trocar_vogais(palavra_frase):
    for c in range(0, len(palavra_frase)):
        if palavra_frase[c] in 'a':
             palavra_frase = palavra_frase.replace('a', '*')
        elif palavra_frase[c] in 'e':
            palavra_frase = palavra_frase.replace('e', '&')
        elif palavra_frase[c] in 'i':
            palavra_frase = palavra_frase.replace('i', '#')
        elif palavra_frase[c] in 'o':
            palavra_frase = palavra_frase.replace('o', '!')
        elif palavra_frase[c] in 'u':
            palavra_frase = palavra_frase.replace('u', '@')

    return palavra_frase


print(trocar_vogais('luar'))