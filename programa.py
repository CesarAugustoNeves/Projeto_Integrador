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




codigo = int(input("Insira o código do produto: "))
nome = str(input("Insira o nome do produto: "))
descricao = str(input("Insira a descrição do produto: "))
cp = float(input("Insira o custo do produto (CP): "))
cf = float(input("Insira o custo fixo (CF) do produto: "))
cv = float(input("Insira o valor de comissão de vendas (CV) do produto: "))
iv = float(input("Insira o custo dos impostos do produto (IV): "))
ml = float(input("Insira o valor de rentabilidade do produto (ML): "))

pv = cp / (1 - (cf + cv + iv + ml) / 100)


print(pv) 
