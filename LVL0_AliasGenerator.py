def Alias_gen(name):
    nome = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', 'D': 'Data', 'E': 'Enhanced', 'F': 'Foxtrot', 'G': 'Gooner', 'H': 'Hover', 'I': 'Indigo', 'J': 'Jarvi', 'K': 'Kanvas', 'L': 'Leviathan',
            'M': 'Manhattan', 'N': 'Network', 'P': 'Professor', 'Q': 'Queue', 'R': 'Reseveur', 'S': 'Saint', 'T': 'Tone', 'U': 'Underline', 'V': 'Vendetta', 'X': 'Xentrix', 'Z': 'Zen'}
    sobrenome = {'A': 'Alpha2', 'B': 'Beta2', 'C': 'Cache2', 'D': 'Data2', 'E': 'Enhanced2', 'F': 'Foxtrot2', 'G': 'Gooner2', 'H': 'Hover2', 'I': 'Indigo2', 'J': 'Jarvi2', 'K': 'Kanvas2', 'L': 'Leviathan2',
                 'M': 'Manhattan2', 'N': 'Network2', 'P': 'Professor2', 'Q': 'Queue2', 'R': 'Reseveur2', 'S': 'Saint2', 'T': 'Tone2', 'U': 'Underline2', 'V': 'Vendetta2', 'X': 'Xentrix2', 'Z': 'Zen2'}
    NovoNome = []

    for c, nomeDigitado in enumerate(name):
        for letra2, firstName in nome.items():
            if nomeDigitado[0] == letra2:
                if c == 0:
                    NovoNome.append(firstName)
                    print(f'o nome {nomeDigitado} corresponde a {firstName}')
        for letra3, LastName in sobrenome.items():
            if nomeDigitado[0] == letra3:
                if c == 1:
                    NovoNome.append(LastName)
                    print(f'o nome {nomeDigitado} corresponde a {LastName}')
        print(f'nome digitado: {nomeDigitado}')
    #print(f'o novo nome é: {" ".join(NovoNome)}')
    return f'o novo nome é: {" ".join(NovoNome)}'


nome0 = str(input('digite o nome e sobrenome: ').title()).split()
print(nome0)
print(Alias_gen(nome0))

# Existe outra forma de fazer, como esta na imagem salva. No caso os dicionarios 'FIRST_NAME' E 'SURNAME' são acessados de outra forma, pelas suas chaves, logo FIRST_NAME[nomedigitado.upper()[0]] retorna o valor contido no dicionario naquela key.
