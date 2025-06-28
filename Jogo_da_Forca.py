import random

def lista():
    lista_palavras=["python", "banana", "computador", "programa", "desafio", "amizade"]

    palavra_secreta=random.choice(lista_palavras)
    return palavra_secreta

letras_tentadas=[]
palavra_secreta = lista()
letras_descobertas = ["_"]*len(palavra_secreta)
tentativas_erradas=0
limite_tentativas = 6

def forca_desenho(erros):
    forca=["""             ------
             |    |
                  |
                  |
                  |
                  |
            --------
            """,
        """
         ------
         |    |
         O    |
              |
              |
              |
        --------
        """,
        """
         ------
         |    |
         O    |
         |    |
              |
              |
        --------
        """,
        """
         ------
         |    |
         O    |
        /|    |
              |
              |
        --------
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
              |
              |
        --------
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
        /     |
              |
        --------
        """,
        """
         ------
         |    |
         O    |
        /|\\   |
        / \\   |
              |
        --------
        """]
    print(forca[erros])




while True:
    forca_desenho(tentativas_erradas)
    print("Palavra:"," ".join(letras_descobertas))
    print("Letras já tentadas:", ", ".join(letras_tentadas))
    letra=input("Digite uma letra: ").lower()

    if len(letra)!=1 or not letra.isalpha():
        print("\033[31mPor favor, digite apenas UMA letra.\033[m")
        continue

    if letra in letras_descobertas:
         print("\033[31Você já tentou essa letra! Tente outra.\033[m")
         continue
    letras_tentadas.append(letra)
    if letra in palavra_secreta:
        for i in range (len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                letras_descobertas[i] = letra
    else:
        tentativas_erradas+=1
        print(f"\033[31mLetra não está na palavra! Erros: {tentativas_erradas}/{limite_tentativas}\033[m")

    if "_" not in letras_descobertas:
        print(f"\033[32m\nParabéns! Você venceu! A palavra era:{palavra_secreta}\033[m" )
        break

    if tentativas_erradas >= limite_tentativas:
        print(f"\033[31m\nVocê perdeu! A palavra era:{palavra_secreta}\033[m" )
        break

