USE projeto_integrador_pucc;

CREATE table PRODUTOS(
codigo int not null auto_increment,
nome varchar(50),
descricao varchar(100),
cp decimal(10,2),
cf decimal(10,2),
cv decimal(10,2),
iv decimal(10,2),
ml decimal(10,2),
PRIMARY KEY (codigo))
default charset=utf8mb4;

INSERT INTO PRODUTOS
VALUES(
'1', 'Mesa', 'Mesa de escritório feita de madeira', '75.00', '11.25',
'3.75', '9.00', '15.00'); 





INSERT INTO PRODUTOS
VALUES
('2', 'Porta', 'Porta de ferro', '50.00', '17.00', '6.00', '20.00', '30.00');



