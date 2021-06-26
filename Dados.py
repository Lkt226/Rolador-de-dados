## Imports
from random import randint

## Variaveis
TipoDado = 6
ultimoroll = 1


## Defs
def Roll(qnt):
    x = 0
    while (x<qnt):
        d6 = randint(1,TipoDado)
        print(d6)
        x = x+1
    print("")

def VerificarRolagens():
    while True:     
        dadosAux = input("você quer rolar quantos dados? ")
        
        if (dadosAux.isdecimal()):
            dados = int(dadosAux)
            if (dados <= 0):
                print("\nvocê deve rolar no minimo 1 dado \n")
                continue
        
            else:
                print("Rolando dados ...")
                Roll(dados)
                global ultimoroll
                ultimoroll = dados
                break 
        else:
            print("\nvocê deve digitar somente numeros \n")
            continue
        
def Codigos():
    while True:
        comando = input("digite um comando: ")

        Listacomandos = ["help", "roll", "change", "reroll"]

        if (comando in Listacomandos):

            if(comando == "help"):
                print("")
                print("roll: Para rolar os dados")
                print("reroll: Repete a ultima rolagem")
                print("change: Para mudar o tipo do dado")
                print("")
    
            elif(comando == "roll"):
                VerificarRolagens()

            elif(comando == "reroll"):
                Roll(ultimoroll)

            elif(comando == "change"):
                global TipoDado
                TipoDado = int(input("Escolha quantas faces tem seu dado: "))
                print("\nvocê esta rolando dados d"+str(TipoDado),"\n")
        else:
            print("O comando que você digitou não existe")

##Comandos
# help: Permite ver os outros comandos
# roll: Para rolar os dados
# reroll: Repete a ultima rolagem
# change: Para mudar o tipo do dado

## Tela
print("Olá, você quer rolar dados?")
print("você esta rolando dados d"+str(TipoDado),"\n")
print("digite "+"help"+" para ver os comandos \n")

Codigos()
