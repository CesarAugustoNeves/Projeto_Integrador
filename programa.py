# Primeiro vamos fazer o usuário inserir os dados do produto a ser cadastrado. São eles: 
# Código do produto (chave primária pro SQL) - (int)
# Nome do produto - (str)
# Descrição do produto - (str)
# Custo do produto (CP) - (float)
# Custo Fixo/Administrativo (CF) - (float)
# Comissão de Vendas (CV) - (float)
# Impostos (IV) - (float)
# Rentabilidade (ML) - (float)

# Todos esses valores irão para uma fórmula afim de calcular o preço de venda (PV)


#Implementações da Versão 2.0 VVVVV

#Faremos uma Integração do código em Python com um Banco de Dados SQL.




#Versão 2.0 - Puxar os dados do banco de dados por meio do código inserido pelo usuário, então mostrar os dados
#e então realizar os cálculos e classificar o lucro



#Versão 3.0 - Fazer um CRUD para a Inserção, Atualização, Consulta e Eliminação de Dados do banco

import mysql.connector





def menuOpçoes(menu):
    print(f"{menu[0]}\n{menu[1]}\n{menu[2]}\n{menu[3]}\n{menu[4]}\n{menu[5]}\n")




def inserir():
    while True:
        print("Iniciando a função inserir")
        print("Essa função insere dados na tabela Produtos")
        try:

            codigo = int(input("Insira o código do produto: "))
            nome = str(input("Insira o nome do produto: "))
            descricao = str(input("Insira a descrição do produto: "))
            cp = float(input("Insira o custo do produto (CP): "))
            cf = float(input("Insira o custo fixo (CF) do produto: "))
            cv = float(input("Insira o valor de comissão de vendas (CV) do produto: "))
            iv = float(input("Insira o custo dos impostos do produto (IV): "))
            ml = float(input("Insira o valor de rentabilidade do produto (ML): "))
        except ValueError:
            print("Insira os valores corretos, sendo um número inteiro em código, letras em nome e descrição, decimais nos demais")
        else:
            executarDb(f"INSERT INTO Produtos VALUES(('{codigo}'), ('{nome}'), ('{descricao}'), ('{cp}'), ('{cf}'), ('{cv}'), ('{iv}'), ('{ml}'));", False)            


        sair = input("Digite 0 para sair ou qualquer coisa para continuar: ")

        if sair == '0':
            break

def atualizar():
    
    opcoesAtualizar = ["1 - Nome", \
                       "2 - Descrição", \
                       "3 - Custo do Produto (CP)", \
                       "4 - Custo Fixo/Administrativo (CF)", \
                       "5 - Comissão de Vendas (CV)", \
                       "6 - Impostos (IV)", \
                       "7 - Rentabilidade (ML)", \
                       "8 - Sair"]


    while True:
        print("Iniciando a função atualizar")
        print("Essa função atualiza dados de um produto específico da tabela Produtos")
        codigo = qualCodigo()

        if codigo == 0:
            break

        dadosProduto = executarDb(f"SELECT * FROM Produtos WHERE codigo={codigo};")

        dadosAtuais = dadosProduto[0]

        nomeAtual = dadosAtuais[1]
        descAtual = dadosAtuais[2]
        cpAtual = dadosAtuais[3]
        cfAtual = dadosAtuais[4]
        cvAtual = dadosAtuais[5]
        ivAtual = dadosAtuais[6]
        mlAtual = dadosAtuais[7]


        print(f"{opcoesAtualizar[0]}\n{opcoesAtualizar[1]}\n{opcoesAtualizar[2]}\n{opcoesAtualizar[3]}\n{opcoesAtualizar[4]}\n{opcoesAtualizar[5]}\n{opcoesAtualizar[6]}\n{opcoesAtualizar[7]}\n")

        opcaoAtualizar = int(input("Insira a opção desejada: "))

        match opcaoAtualizar:
            case 1:
                print(f"O nome atual é {nomeAtual}")
                novoNome = input("Insira o novo nome ou 0 para cancelar: ")
                if novoNome == nomeAtual:
                    print("O nome permaneceu igual")
                elif novoNome == '0':
                    print("Cancelando atualização")
                else:
                    executarDb(f"UPDATE Produtos SET nome='{novoNome}' WHERE codigo={codigo};", False)
            case 2:
                print(f"A descrição atual é: {descAtual}")
                novaDesc = input("Insira a nova descrição ou 0 para cancelar: ")
                if novaDesc == descAtual:
                    print("A descrição permaneceu igual")
                elif novaDesc == '0':
                    break
                else:
                    executarDb(f"UPDATE Produtos SET descricao='{novaDesc}' WHERE codigo={codigo};", False)    
            case 3:
                print(f"O Custo do Produto atual é: {cpAtual}")
                novoCp = input("Insira o novo custo do produto ou 0 para cancelar: ")
                if novoCp == cpAtual:
                    print("O custo do produto permaneceu igual")
                elif  novoCp == '0':
                    break
                else:
                    executarDb(f"UPDATE Produtos SET cp='{novoCp}' WHERE codigo={codigo};", False)
            case 4:
                print(f"O Custo Fixo/Administrativo atual é: {cfAtual}")
                novoCf = input("Insira o novo custo fixo ou 0 para cancelar: ")
                if novoCf == cfAtual:
                    print("O custo fixo permaneceu igual")
                elif novoCf == '0':
                    break
                else:
                    executarDb(f"UPDATE Produtos SET cf='{novoCf}' WHERE codigo={codigo};", False)
            case 5:
                print(f"A Comissão de Vendas atual é: {cvAtual}")
                novaCv = input("Insira a nova comissão de vendas ou 0 para cancelar: ")
                if novaCv == cvAtual:
                    print("A comissão de vendas permaneceu igual")
                elif novaCv == '0':
                    break
                else:
                    executarDb(f"UPDATE Produtos SET cv='{novaCv}' WHERE codigo={codigo};", False)
            case 6:
                print(f"A taxa de imposto atual é: {ivAtual}")
                novoIv = input("Insira a nova taxa ou 0 para cancelar: ")
                if novoIv == ivAtual:
                    print("A taxa permaneceu igual")
                elif novoIv == '0':
                    break
                else:
                    executarDb(f"UPDATE Produtos SET iv='{novoIv}' WHERE codigo={codigo};", False)
            case 7:
                print(f"A margem de lucro atual é: {mlAtual}")
                novaMl = input("Insira a nova margem de lucro ou 0 para cancelar: ")
                if novaMl == mlAtual:
                    print("A margem permaneceu igual")
                elif novaMl == '0':
                    break
                else:
                    executarDb(f"UPDATE Produtos SET ml='{novaMl}' WHERE codigo={codigo};", False)        
def consultar():
    
    

    while True:
        print("Iniciando a função consultar")
        print("Essa função faz uso do SELECT no banco de dados e retorna um item baseado em seu codigo")

        codigo = qualCodigo()

        if codigo == 0:
            break

        funcao = (f"SELECT * FROM Produtos WHERE codigo = {codigo}")

        dados = executarDb(funcao)

        for item in dados:
            print(f"Codigo = {item[0]}")
            print(f"Nome = {item[1]}")
            print(f"Descrição = {item[2]}")
            print(f"Custo (CP) = {item[3]}")
            print(f"Custo Fixo/Administrativo (CF) = {item[4]}")
            print(f"Comissão de Vendas (CV) = {item[5]}")
            print(f"Impostos (IV) = {item[6]}")
            print(f"Rentabiliadde (ML) = {item[7]}\n")

        

        


def listar():
    print("Iniciando a função Listar\n")
    print("Essa função lista todos os dados na tabela Produtos")
    funcao = ("SELECT * FROM Produtos;")
    dados = executarDb(funcao)

    for item in dados:
        print(f"Codigo = {item[0]}")
        print(f"Nome = {item[1]}")
        print(f"Descrição = {item[2]}")
        print(f"Custo (CP) = {item[3]}")
        print(f"Custo Fixo/Administrativo (CF) = {item[4]}")
        print(f"Comissão de Vendas (CV) = {item[5]}")
        print(f"Impostos (IV) = {item[6]}")
        print(f"Rentabiliadde (ML) = {item[7]}\n")




def excluir():
    while True:
        print("Iniciando a função excluir")
        print("Essa função exclui um produto da tabela Produtos")

        codigo = qualCodigo()

        if codigo == 0:
            break

        dados = executarDb(f"SELECT * FROM Produtos WHERE codigo={codigo};")

        dadosProduto = dados[0]

        print(f"Tem certeza que deseja excluir o produto {dadosProduto[1]}, de código {dadosProduto[0]}?\n")
        confirma = input("Digite S, s ou N, n para excluir: ").upper()
        if confirma == 'S':
            executarDb(f"DELETE FROM Produtos WHERE codigo={codigo};", False)
        elif confirma == 'N':
            print("Exclusão de dados cancelada!")
        else:
            print("Nenhuma opção inválida foi selecionada!\n")




def qualCodigo():

    passou = False

    while passou == False:
        try:
            codigo = int(input("Insira o código do produto ou 0 para sair: "))
        
        except ValueError:
            print("O Codigo deve ser um número inteiro")
        else:
            passou = True
    return codigo


passou = False

"""
while passou == False:
    try:

        codigo = int(input("Insira o código do produto: "))
        nome = str(input("Insira o nome do produto: "))
        descricao = str(input("Insira a descrição do produto: "))
        cp = float(input("Insira o custo do produto (CP): "))
        cf = float(input("Insira o custo fixo (CF) do produto: "))
        cv = float(input("Insira o valor de comissão de vendas (CV) do produto: "))
        iv = float(input("Insira o custo dos impostos do produto (IV): "))
        ml = float(input("Insira o valor de rentabilidade do produto (ML): "))
    except ValueError:
        print("Insira os valores corretos, sendo um número inteiro em código, strings em nome e descrição, floatpoint nos demais")
    else:
        passou = True
        
pv = cp / (1 - (cf + cv + iv + ml) / 100)


print(pv) 

"""


def executarDb(comando, usaFetch=True):
    
    db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "codifique",
    database = "projeto_integrador_pucc")

    

    cursor = db.cursor()

    cursor.execute(comando)

    print("Função executada!\n")

    if usaFetch == True:
        dados = cursor.fetchall()
        return dados
    else:
        commit = input("Deseja aplicar as alterações? S, s ou N, n: ").upper()
        if commit == 'S':
            db.commit()
            print("Alterações aplicadas!")
        elif commit == 'N':
            db.rollback()
            print("Alterações descartadas!")
        else:
            print("Insira uma opção válida!\n")
            

    db.close()
    

    

def calcularLucro(dados):
    
    erro = True

    while erro == True:
        try:
            cp = dados[3]
            cf = dados[4]
            cv = dados[5]
            iv = dados[6]
            ml = dados[7]
        except IndexError: #Esse erro acontece quando tentamos passar a lista inteira (dados) para essa função ao invés da tupla que está dentro dela (dados[0])
            print("Erro ao passar valores da tabela para as variáveis")  
            break
        else:  
            erro = False
    
    
            pv = cp / (1 - (cf + cv + iv + ml) / 100)

            receita = pv - cp

            outrosCustos = (cf / 100 * pv) + (cv / 100 * pv) + (iv / 100 * pv)

            rentabilidade = receita - outrosCustos

            lucro = rentabilidade / 100

            print(f"Descrição                            Valor    %")
            print(f"A. Preço de Venda                    {round(pv, 2)}   {round((pv / pv) * 100, 2)}%")
            print(f"B. Custo de Aquisição (fornecedor)   {round(cp, 2)}   {round((cp/ pv) * 100, 2)}%")
            print(f"C. Receita Bruta (A-B)               {round(receita, 2)}   {round((receita / pv) * 100, 2)}%")
            print(f"D. Custo Fixo/Administrativo         {round(cf / 100 * pv, 2)}   {round(cf, 2)}%")
            print(f"E. Comissão de Vendas                {round(cv/ 100 * pv, 2)}   {round(cv, 2)}%")
            print(f"F. Impostos                          {round(iv/ 100 * pv, 2)}   {round(iv, 2)}%")
            print(f"G. Outros custos (D+E+F)             {round(outrosCustos, 2)} {round((outrosCustos / pv) * 100, 2)}%")
            print(f"H. Rentabilidade (C - G)             {round(rentabilidade, 2)} {round((rentabilidade/ pv) * 100, 2)}%\n\n")


        if lucro < 0:
            print("O seu lucro é menor do que 0, logo você está em PREJUÍZO!")
        elif lucro == 0:
            print("O seu lucro é de 0%, logo você está em EQUILÍBRIO")
        elif lucro > 0 and lucro < 10 / 100:
            print("O seu lucro está entre 0 e 10%, logo ele é BAIXO")
        elif lucro > 10/100 and lucro < 20/100:
            print("O seu lucro está entre 10% e 20%, logo ele é MÉDIO")
        elif lucro > 20 / 100:
            print("O seu lucro é maior que 20%, logo ele é ALTO")




# Definições acima ^^^


menu = ["1 - Inserir Dados", \
        "2 - Atualizar Dados", \
        "3 - Consultar Dados", \
        "4 - Listar Dados", \
        "5 - Excluir Dados", \
        "6 - Sair do Programa"]

opcao = 999

while opcao != 6:
    menuOpçoes(menu)
    opcao = int(input("Insira a opção desejada: "))
    if opcao == 1:
        inserir()
    elif opcao ==2:
        atualizar()
    elif opcao ==3:
        consultar()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        excluir()
    elif opcao == 6:
        pass
    else:
        print("Opção não encontrada! Por Favor digite novamente! \n")
