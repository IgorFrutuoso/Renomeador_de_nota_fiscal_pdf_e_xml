import re
import os
import shutil

print('Renomeador de arquivos by Frutuoso')

pasta = r'C:\Users\User\Downloads\notas'                    #local da pasta onde estâo os aquivos
numero_inicial = int(input('Digite o numero inicial: '))    #Número da primeira nota
numero_final = int(input('Digite o numero final: '))        #Número da ultima nota


def loop_arquivos(root, dirs, files):
    cont = 1
    numero = numero_inicial
    for file in files:
        if cont <= 2:
            cont += 1
            nome, extensão = os.path.splitext(file)
            novo_nome = f'{numero} {nome}{extensão}'
            pasta_antiga = os.path.join(root, file)
            pasta_nova = os.path.join(root, novo_nome)
            print(novo_nome)
            shutil.move(pasta_antiga, pasta_nova)
        else:
            cont = 2
            numero += 1
            nome, extensão = os.path.splitext(file)
            novo_nome = f'{numero} {nome}{extensão}'
            pasta_antiga = os.path.join(root, file)
            pasta_nova = os.path.join(root, novo_nome)
            print(novo_nome)
            shutil.move(pasta_antiga, pasta_nova)


def loop_principal():
    for root, dirs, files in os.walk(pasta):
        loop_arquivos(root, dirs, files)


if __name__ == '__main__':
    loop_principal()
