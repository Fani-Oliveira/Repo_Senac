CREATE DATABASE PROJETO;

USE PROJETO;

CREATE TABLE produtos (
Id_Produto INT,
Nome_Produto VARCHAR (100),
Categoria VARCHAR (100),
Preco DECIMAL (10,2),
Marca VARCHAR (100);

CREATE TABLE vendas (
ID_Venda INT,
ID_cliente INT,
ID_Produto INT,
Data DATE,
Quantidade VARCHAR (100),
Canal VARCHAR (20),
Valor_Total DECIMAL (10,2);

CREATE TABLE clientes(
ID_Cliente INT,
