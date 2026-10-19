nome = "joana"
print(f"Olá {nome.title()}, gostaria de aprender um pouco de Python hoje?\n")

print(nome.lower())
print(nome.upper())
print(nome.title())

print("Segundo Rosa Luxemburgo: 'Quem não se movimenta não sente as correntes \
      que o prendem.'")

print("Ex. 2.6")
famous_person = "rosa luxemburgo"
message = f"Segungo {famous_person.title()}: 'Quem não se movimenta não sente \
    as correntes que o prendem.'"
print(message)

print("Ex. 2.7")
nome = "\t\t\t Guilherme \n \t\t\t Malaquias \n \t\t\t Ferreira \t\t\t"
print(nome)
print(nome.lstrip())
print(nome.rstrip())
print(nome.strip())

print("Ex. 2.8")
filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))