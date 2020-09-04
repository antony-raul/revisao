"""
Uma empresa de viagens pretende automatizar a venda de passagens. Para isso você deve armazenar todos os ônibus 
em cada Ônibus os seus Passageiro. Cada Ônibus possui, placa, origem, destino, hora 
além da sua lista de Passageiro. Cada Passageiro possui apenas o CPF.
O programa deve:
1-Adicionar Ônibus ok
2-Remover Ônibus
3-Vender Passagem ok
4-Devolver Passagem
5-Imprimir
Observações:
- Não deve existir mais de um Ônibus com a mesma placa;
- Não deve existir mais de um Passageiro com o mesmo CPF em um mesmo Ônibus.
- Todas as informações devem ser persistentes, ou seja, quando fechar o programa tudo deve ser salvo e
  quando abrir o programa todas as informações devem ser carregadas.
"""



onibus = []



def criaOnibus(placa,origem,destino,hora,listPassageiros):
    return{
        'placa': placa,
        'origem': origem,
        'destino': destino,
        'hora': hora,
        'listPassageiros': listPassageiros
        

    }
def criaPassageiro(nome,cpf):
    return{
        'nome': nome,
        'cpf': cpf,
        
    }


def adicionarOnibus():
    placa = input('Digite a placa do onibus: ')
    origem = input('Digite a origem do onibus: ')
    destino = input('Digite a destino do onibus: ')
    hora = input('Digite a hora da chegada: ')
    listPassageiros =[]
    

    bus = criaOnibus(placa, origem, destino, hora,listPassageiros)
    onibus.append(bus)

def adicionarPassageiro():
    nome = input('Digite nome do passageiro: ')
    cpf = input('Digite o cpf do passageiro: ')
    placaBus = input('Digite a placa do onibus que vai viajar: ')
    

    passa =criaPassageiro(nome, cpf)
    for o in onibus:
        if placaBus == o['placa']:
            print(o)
            o['listPassageiros'].append(passa)

        
while True:
    op= int(input("1-Adicionar Ônibus\n2-Remover Ônibus\n3-Vender Passagem\n4-Devolver Passagem\n5-Imprimir\n"))
    if op == 1:
        adicionarOnibus()
        print("onibus adicionado")
    if op == 2:
        '''chmar função'''
        print("onibus removido")
    if op == 3:
        adicionarPassageiro()
        print("passagem vendida")
    if op == 4:
        '''chmar função'''
        print("passagem devolvida")
    if op == 5:
        print(onibus)



