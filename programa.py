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

<<<<<<< HEAD
=======
#Implementações da Versão 2.0 VVVVV

#Faremos uma Integração do código em Python com um Banco de Dados SQL.

passou = False
>>>>>>> @{-1}

#Versão 2.0 - Puxar os dados do banco de dados por meio do código inserido pelo usuário, então mostrar os dados
#e então realizar os cálculos e classificar o lucro

import mysql.connector

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "codifique",
    database = "projeto_integrador_pucc")

while db.is_connected == False: 
    print("Erro na conexão com banco de dados, tente corrigir os dados!")
    break

cursor = db.cursor()



def qualCodigo():

    passou = False

    while passou == False:
        try:
            codigo = int(input("Insira o código do produto: "))
        
        except ValueError:
            print("O Codigo deve ser um número inteiro")
        else:
            passou = True
    return codigo


def executarDb(comando, usaFetch=True):
    print(f"Executando: {comando}\n\n")

    cursor.execute(comando)

    print("Função executada!\n")

    if usaFetch == True:
        dadosSelect = cursor.fetchall()
        return dadosSelect
    
    
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


codigo = qualCodigo()

dados = executarDb(f"SELECT * FROM PRODUTOS WHERE CODIGO = {codigo}", True) #Executando o comando no DB e depois usando fetchall()

#Retorna uma lista com uma tupla dentro, sendo cada item da tupla um dado da tabela.



calcularLucro(dados[0]) #Se passar a lista inteira dará erro, usar dados[i] para passar a tupla dentro da lista



    