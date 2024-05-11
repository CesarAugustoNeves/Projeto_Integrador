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


#Versão 2.0 - Puxar os dados do banco de dados por meio do código inserido pelo usuário, então mostrar os dados
#e então realizar os cálculos e classificar o lucro

import mysql.connector

db = mysql.connector.connect(
    host = "127.0.0.1",
    user = "root",
    password = "codifique")

print(db.is_connected()) #mostra se conectou

cursor = db.cursor()

cursor.execute("describe projeto_integrador_pucc.PRODUTOS")

for i in cursor:
    print(i) #printando o que o sql retornou do execute

passou = False

while passou == False:
    try:
        codigo = int(input("Insira o código do produto: "))
        
    except ValueError:
        print("O Codigo deve ser um número inteiro")
    else:
        passou = True
        



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
print(f"H. Rentabilidade (C - G)             {round(rentabilidade, 2)} {round((rentabilidade/ pv) * 100, 2)}%")


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




    