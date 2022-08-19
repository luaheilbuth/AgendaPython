def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':
        opcao= input('''
        ====================================================================
                                         AGENDA
        MENU:
        
        [1]NOVO CONTATO
        [2]CONSULTAR CONTATOS CADASTRADOS
        [3]REMOVER CONTATO
        [4]BUSCAR CONTATO PELO NOME
        [5]SAIR
        
        =====================================================================
        ESCOLHA UMA DAS OPÇÕES ACIMA: ''')
        if opcao =='1':
            novoContato()
        elif opcao =='2':
            consultaContato()
        elif opcao =='3':
            removerContato()
        elif opcao =='4':
            buscarContatoPeloNome()
        else:
            sair()
        voltarMenuPrincipal = input('Deseja voltar ao menu principal? (s;n): ').lower()


def novoContato():
    nome = input('Digite o nome do seu contato: ')
    telefone = input('Digite o telefone do seu contato: ')
    email = input('DIgite o email do contato: ')
    twitter = input('Digite o twitter do seu contato: ')
    instagram = input('Digite o instagram do seu contato: ')
    try:
        agenda = open('atividadeAtiva.txt','a')
        dados = f'{nome},{telefone},{email},{twitter},{instagram} \n'
        agenda.write(dados)
        agenda.close()
        print(f'Contato gravado com sucesso!')
    except:
        print('Erro na gravação do contato')

def consultaContato():
    agenda = open('atividadeAtiva.txt','r')
    for contato in agenda:
        print(contato)
    agenda.close()

def removerContato():
    nomeDeletado = input('Digite o nome a ser deletado: ').lower()
    agenda = open('atividadeAtiva.txt','r')
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0,len(aux)):
        if nomeDeletado not in aux[i].lower():
            aux2.append(aux[i])
    agenda = open('atividadeAtiva.txt','w')
    for i in aux2:
        agenda.write(i)
    print(f'Contato deletado com sucesso!')
    consultaContato()


def buscarContatoPeloNome():
    nome = input('Digite o nome a ser procurado: ').upper()
    agenda = open('atividadeAtiva.txt', 'r')
    for contato in agenda:
        if nome in (contato.split(',')[0]).upper():
            print(contato)
    agenda.close()

def sair():
    print(f'Até mais!')
    exit()

def main():

    menu()
    
main()