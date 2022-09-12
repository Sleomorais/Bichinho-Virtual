#Importando Bibliotecas
from os import rename
from time import sleep

#ANIMAL VIRTUAL
#Classe Construtora
class Pou():
    # Definindo Atributos
    def __init__(self, nome):
        self.nome = nome
        self.energia = 100
        self.sede = 0
        self.fome = 0
        self.saude = 100
        self.xp = 0
        self.humor = 100
        self.idade = 0
        self.vida = True
    #Implementando Metodos
    def sono(self):
        if self.energia < 20 or self.saude < 30:
            print("Quer descansar um pouco? S/N")
            dormir=input("Dormir?").upper()
            if dormir == "S":
                print("ZZzzZZ")
                sleep(5.0)
                self.energia = 100
                self.saude +=10
            elif dormir == "N":
                print("Continuando jogo")
            else:
                print("Dado Invalido")

        if self.energia <= 5 or self.saude <= 10:
            print("Desmaiou")
            sleep(0.5)
            print("Recuperando...")
            sleep(10.0)
            self.energia = 100
            self.saude += 10
            self.humor -= 15
        
        
        if self.humor > 100:
            self.humor = 100
        if self.energia > 100:
            self.energia = 100
        if self.saude > 100:
            self.saude = 100

    def brincar(self):
        opcoes = ["Futebol","Ouvir_Musica","Ciclismo","Pescar","Dançar"]
        brincadeira = input("Quer brincar? S/N\n").upper()
        if brincadeira == "S":
            print("0 ==",opcoes[0] , "\n1 ==",opcoes[1],"\n2 ==",opcoes[2],"\n3 ==",opcoes[3], "\n4 ==:", opcoes[4])
            escolher = int(input("Escolhar uma opção de 0 a 4 \n"))
            if escolher == 0:
                print("Futebol")
                print("                           __________    ")
                print("  __                       |   __   | \  ")
                print("-(°°)- °                   | \(°°)/ |  \ ")
                sleep(1)
                print("                           __________    ")
                print("  __     °                 |   __   | \  ")
                print("-(°°)-                     | -(°°)- |  \ ")
                sleep(1)
                print("                  °        __________    ")
                print("  __                       |    __  | \  ")
                print("-(°°)-                     |  /(°°)\|  \ ")
                sleep(1)
                print("                           __________    ")
                print("  __                       |°  __   | \  ")
                print("-(°°)-                     | \(°°)\ |  \ ")
                sleep(1)
                print("           --GOAL--        __________    ")
                print("  __                       |   ___  | \  ")
                print("\(--)/                     | -(;-;)-| °\ ")

                self.energia -=30
                self.xp += 2.0
                self.humor += 30
                self.sede += 30
                self.fome += 30

                print("Energia: {}\n XP: +{}\n Humor: +{}\n Sede: +{}\n Fome: +{}".format(self.energia, self.xp, self.humor, self.sede, self.fome))
                sleep(2.2)
            elif escolher == 1:
                musica= ["Triste", "Animada"]
                print("Escolha:\n 0 == {}\n 1 == {}\n".format(musica[0],musica[1]))
                musica_escolhida = input("Quer escutar uma musica Triste ou uma Animada?\n")
                print("Ouvindo Musica...")
                print("                 ♩♪ ")
                print("        _____ ♩♪    ")
                print("       /    /       ")
                print("      / ♫♬ /        ")
                print("     /____/         ")
                sleep(1)
                print("             ♩♪     ")
                print("        _____   ♩♪  ")
                print("       /    /  ♩♪   ")
                print("      / ♫♬ /        ")
                print("     /____/         ")
                sleep(1)
                print("                 ♩♪ ")
                print("      ♩♪ _____ ♩♪    ")
                print("       /    /       ")
                print("      / ♫♬ /        ")
                print("     /____/         ")
                if musica_escolhida == 0:
                    self.humor -=20
                    self.xp += 5
                elif musica_escolhida == 0:
                    self.humor +=20
                    self.energia +=5

                self.sede += 5
                self.fome += 5

                print("Energia: {}\n XP: +{}\n Humor: +{}\n Sede: +{}\n Fome: +{}".format(self.energia, self.xp, self.humor, self.sede, self.fome))
                sleep(2.2)

            elif escolher == 2:
                print("Ciclismo") 
                print("              :..    __..__      ")
                print("               |       |         ")
                print("           ____/--------\____    ")
                print("    __    | ./ |        | \. |   ")
                print("  -(°°)-  |____|        |____|   \n\n")
                sleep(1)
                print("      __     :..    __..__      ")
                print("    -(^^)-    |       |         ")
                print("   /      ____/--------\____    ")
                print("    /    | ./ |        | \. |   ")
                print("         |____|        |____|   \n\n")
                sleep(1)
                print("              __               ")
                print("            -(°°)-             ")
                print("             :..    __..__     ")
                print("      __      |       |        ")
                print("    _     ____/--------\____   ")
                print("  ___    | ./ |        | \. |  ")
                print("    -    |____|        |____|  \n\n")
                sleep(1)
                print("               __               ")
                print("             \(^^)/             ")
                print("              :..    __..__     ")
                print("      ___      |       |        ")
                print("    __     ____/--------\____   ")
                print("  _       |  /.|        | .\ |  ")
                print("    --    |____|        |____|  \n\n")
                sleep(1)
                print("              __               ")
                print("            \(^^)/             ")
                print("             :..    __..__     ")
                print("      __      |       |        ")
                print("    _     ____/--------\____   ")
                print("  ___    | ./ |        | \. |  ")
                print("    -    |____|        |____|  \n\n")

                self.energia -=30
                self.xp += 2
                self.humor += 30
                self.sede += 30
                self.fome += 30

                print("Energia: {}\n XP: +{}\n Humor: +{}\n Sede: +{}\n Fome: +{}".format(self.energia, self.xp, self.humor, self.sede, self.fome))
                sleep(2.2)
            elif escolher == 3:
                print("Pescar")
                print("       ___     /| ")
                print("      |°_°|   / | ")
                print("     /----/  /  | ")
                print("    |____/  /   ° \n\n")
                sleep(1.2)
                print("       ___ <3  /| ")
                print("      |^_^|   / | ")
                print("     /----/  /  | ")
                print("    |____/  /   C<\n\n")
                sleep(2.0)
                print("       ___     /| ")
                print("      |°_°|   / | ")
                print("     /----/  /  | ")
                print("    |____/  /   ° ")

                self.energia -=30
                self.xp += 2
                self.humor += 30
                self.sede += 30
                self.fome += 30

                print("Energia: {}\n XP: +{}\n Humor: +{}\n Sede: +{}\n Fome: +{}".format(self.energia, self.xp, self.humor, self.sede, self.fome))
                sleep(2.2)

                                        
            elif escolher == 4:
                print("Dançar")
                print("               _______         ")
                print("              /       \        ")  
                print("             |  ^   ^  |       ")
                print("        -----|     O   |-----  ")
                print("             |         |       ")
                print("              \_______/        ")
                print("              /       \        ")
                print("             /         \       ")
                print("            /           \      ")
                sleep(1)
                print("               _______         ")
                print("              /       \        ")
                print("             |  ^   ^  |    |  ")
                print("        _____|     O   |____|  ")
                print("       |     |         |       ")
                print("       |      \_______/        ")
                print("              /       \        ")
                print("             /         \       ")
                print("            /           \      ")
                sleep(1)
                print("               _______         ")
                print("         __   /       \        ")
                print("        |    |  -   -  |       ") 
                print("        |____|     __- |____   ")
                print("             |         |  __|  ")
                print("              \_______/        ")
                print("              /       \        ")
                print("             /         \       ")
                print("            /           \      ")

                self.energia -=30
                self.xp += 2
                self.humor += 30
                self.sede += 30
                self.fome += 30

                print("Energia: {}\n XP: +{}\n Humor: +{}\n Sede: +{}\n Fome: +{}".format(self.energia, self.xp, self.humor, self.sede, self.fome))
                sleep(2.2)

            else:
                print("Digite uma opção válida")

        if self.humor > 100:
            self.humor = 100
        if self.energia > 100:
            self.energia = 100
        if self.saude > 100:
            self.saude = 100
            
    def crescer(self):
        if self.xp >= 100:
            self.idade += 1
            self.xp = 0

        if self.idade <= 12:
            print("       ___   ")
            print("      |°_°|  ")
            print("     /----/  ")
            print("    |____/   ")
        elif self.idade > 10 and self.idade <= 16:
            print("       __|__   ")
            print("      /     \  ")
            print("     | O  O  | ")
            print("     /   __/ | ")
            print("     \______/  ")
        elif self.idade > 16 and self.idade <= 20:
            print("      _______     ")
            print("  ___|_______|___ ")
            print("   /          \   ")
            print("  |  O      O  |  ")
            print(" /              \ ")
            print("|                |")
            print("|        ___/    |")
            print("\________________/")
        elif self.idade > 20:
            print("    __________    ")
            print("   /          \   ")
            print("  |  (O)---(O) |  ")
            print(" /    -     -   \ ")
            print("|                |")
            print("|        ___/    |")
            print("\________________/")
        

    def hidratar(self):
        if self.sede > 80:
            sede = input("Tô com sede? me dá água?S/N").upper()
            if sede == "S":
                self.sede = 0
            elif sede == "N":
                self.saude -=5
                print("Queria agua...")

    def medicar(self):
        if self.saude < 10:
            print("To me sentindo mal, pode me dar um remedio?")
            remedio = input("S/N").upper()
            if remedio == "S":
                self.saude = 100
            elif remedio == "N":
                self.saude -=50
                print("Você não deu remedio ao {}".format(self.nome))
    
    def alimentar(self):
        if self.fome > 80:
            print("To com fome, pode me dar comida?")
            comida = input("S/N").upper()
            if comida == "S":
                self.fome = 0
            elif comida == "N":
                self.saude -=5
                print("Você não deu comida ao {}".format(self.nome))
    def morrer(self):  
        if self.saude == 0 or self.fome >= 100 or self.sede >= 100 or self.idade == 25:
            print("Voce morreu")
            sleep(2)
            print("                     ______          ")
            print("                  __/      \__       ")
            print("                 /           /       ")
            print("        |       /   X     X /        ")
            print("        |______/           /_____    ")
            print("              /        º  /      |   ")
            print("             / \ ________/      |    ")
            print("            /            |           ")
            print("          /_____        |            ")
            print("               |       |             ")
            print("                     __|             ")
            sleep(3)
            print("    ___________   ")
            print("   /           \  ")
            print("  |             | ")
            print("  |  R . I . P  | ")
            print(f" | {self.nome} | ")
            print("  |             | ")
            sleep(4) 
            renascer = input("Deseja começar a jogar novamente?S/N").upper()
            if renascer == "S":
                print("Bem vindo de volta")
                self.energia = 100
                self.sede = 0
                self.fome = 0
                self.saude = 100
                self.xp = 0
                self.humor = 100
                self.idade = 0
                self.vida = False
            elif renascer == "N":
                print("Obrigado Por Jogar")
                self.energia = 100
                self.sede = 0
                self.fome = 0
                self.saude = 100
                self.xp = 0
                self.humor = 100
                self.idade = 0
                self.vida = False
    def jogar(self):
        while self.vida == True:
            self.morrer()
            self.crescer()
            print(f"Fome: {self.fome}, Sede : {self.sede}, Humor: {self.humor}, XP: {self.xp}, Energia: {self.energia}, Saude: {self.saude} ")
            print(f"\n 0 == brincar\n 1 == alimentar \n 2 == Dar Agua\n 3 == medicar \n 4 == A Mimir\n")
            escolha = int(input("Escolha uma Opção"))

            if escolha == 0:
                self.brincar()
            elif escolha == 1:
                self.alimentar()
            elif escolha == 2:
                self.hidratar()
            elif escolha == 3:
                self.medicar()
            elif escolha == 4: 
                self.sono()
            self.sono()  
if __name__ == '__main__':
    pou = Pou("Jubileu")
    print(pou.nome)
    pou.jogar()
