import re
import os
import shutil

print('Renomeador de arquivos by Frutuoso')

pasta = r'C:\Users\User\Downloads\notas'
numero_inicial = int(input('Digite o numero inicial: '))
numero_final = int(input('Digite o numero final: '))

def renomear_arquivo(file):
    while numero_inicial <= numero_final:
        
        return 


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

#for numero in enumerate(lista_notas, 1):
#    os.rename('a.txt', 'b.kml')


#p.rename("{} {}".format(numero_inicial,numero_da_nota))
