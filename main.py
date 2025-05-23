def main():
    arquivo = open("minhas_notas.txt", "w", encoding="utf-8")
    arquivo.write("Etapa 1:\n")
    arquivo.write("Primeira frase da primeira etapa.\n")
    arquivo.write("Segunda frase da primeira etapa.\n")
    arquivo.close()

    arquivo = open("minhas_notas.txt", "a", encoding="utf-8")
    arquivo.write("Segunda etapa:.\n")
    arquivo.write("Primeira frase da segunda etapa.\n")
    arquivo.close()

    arquivo = open("minhas_notas.txt", "r", encoding="utf-8")
    conteudo = arquivo.read()
    print("Conteúdo do arquivo:\n")
    print(conteudo)
    arquivo.close()


if __name__ == "__main__":
    main()