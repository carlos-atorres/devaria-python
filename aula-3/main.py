from classes.Ave import Ave
from classes.Mamifero import Mamifero
from classes.Reptil import Reptil

if __name__ == '__main__':

    lista_animais = [
        Mamifero('Leão', 4, False, False),
        Reptil('Serpente', 4, True, 0),
        Ave('Gavião', 500, True, False),
        Peixe('Tubarão', 2, True, True)
    ]
    nome_animal = input("Digite o nome do Animal: ")

    animal_encontrado = list(filter(lambda a_: a.nome == nome_animal, lista_animais))

if len(animal_encontrado) == 0:
    print('Animal não encontrado')
else:

    if(isinstance(animal_encontrado[0], Mamifero)):
        print(f'Animal {animal_encontrado[0].nome} encontrado do tipo Mamifero')
