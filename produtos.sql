CREATE TABLE PRODUTOS(
codigo int not null auto_increment,
nome varchar(30),
descricao varchar(100),
custo decimal(9,2),
cf decimal(4,2),
cv decimal(4,2),
impostos decimal(10,2),
rentabilidade decimal(4,2),
primary key(codigo))
default charset=utf8mb4;

