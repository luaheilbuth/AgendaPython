def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':
        opcao= input('''
        ====================================================================
                                         AGENDA
        MENU:
        
        [1]NOVO CONTATO
        [2]CONSULTAR CONTATOS CADASTRADOS
        [3]BUSCAR CONTATO PELO NOME
        [4]ATUALIZAR CONTATO
        [5]REMOVER CONTATO
        [6]SAIR
        
        =====================================================================
        ESCOLHA UMA DAS OPÇÕES ACIMA: ''')
        if opcao =='1':
            novoContato()
        elif opcao =='2':
            consultaContato()
        elif opcao =='3':
            buscarContatoPeloNome()
        elif opcao =='4':
            atualizarContato()
        elif opcao == '5':
            removerContato()
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

def buscarContatoPeloNome():
    nome = input('Digite o nome a ser procurado: ').upper()
    agenda = open('atividadeAtiva.txt', 'r')
    for contato in agenda:
        if nome in (contato.split(',')[0]).upper():
            print(contato)
    agenda.close()

def atualizarContato():
        nomeDeletado = input('Digite o nome a ser atualizado: ').lower()
        agenda = open('atividadeAtiva.txt', 'r')
        aux = []
        aux2 = []
        for i in agenda:
            aux.append(i)
        for i in range(0, len(aux)):
            if nomeDeletado not in aux[i].lower():
                aux2.append(aux[i])
        agenda = open('atividadeAtiva.txt', 'w')
        for i in aux2:
            agenda.write(i)
        nome = input('Digite o nome atualizado do contato: ')
        telefone = input('Digite o telefone atualizado do contato: ')
        email = input('DIgite o email atualizado do contato: ')
        twitter = input('Digite o twitter atualizado do seu contato: ')
        instagram = input('Digite o instagram atualizado do seu contato: ')
        try:
            agenda = open('atividadeAtiva.txt', 'a')
            dados = f'{nome},{telefone},{email},{twitter},{instagram} \n'
            agenda.write(dados)
            agenda.close()
            print(f'Contato atualizado com sucesso!')
        except:
            print('Erro na gravação do contato')

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

def sair():
    print(f'Até mais!')
    exit()

def main():

    menu()
    
main()