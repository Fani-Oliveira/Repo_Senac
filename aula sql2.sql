CREATE TABLE cliente (
id INT PRIMARY KEY,
nome VARCHAR(100)) ;

CREATE TABLE produto (
Id INT PRIMARY KEY, 
Produto VARCHAR (100), 
Categoria VARCHAR (100),
Valor_Unitário DECIMAL (10,2));

CREATE TABLE pedido (id INT PRIMARY KEY,
cliente_id INT, FOREIGN KEY (cliente_id) REFERENCES
clientes(id), 
produto_id INT, FOREIGN KEY (produto_id) REFERENCES
produto(id));

INSERT INTO cliente (id, nome)
VALUES 
(31, 'Aline'),
(32, 'Bruno'),
(33, 'Caio'),
(34, 'Manuela'),
(35, 'Nicole');

INSERT INTO cliente (id, nome)
VALUES 
(36, 'Vitor');

INSERT INTO produto (Id, Produto, Categoria, Valor_Unitário)
VALUES
(51, 'SmartPhone', 'Eletrônicos', 4999.00),
(52, 'Máquina de Lavar', 'Eletrodomésticos', 2599.00),
(53, 'Sofá', 'Móveis', 1349.00),
(54, 'Cama Box Queen', 'Móveis', 1699.90),
(55, 'Geladeira', 'Eletrodomésticos', 2378.90),
(56, 'SmartPhone', 'Eletrônicos', 8799.00),
(57, 'Guarda Roupa', 'Móveis', 849.00),
(58, 'Fogão', 'Eletrodomésticos', 849.00),
(59, 'SmartPhone', 'Eletrônicos', 3699.00),
(60, 'AirFryer', 'Eletroportáteis', 249.50);

INSERT INTO pedido (id, cliente_id, produto_id)
VALUES
(11, 33, 52),
(12, 31, 54),
(13, 33, 57),
(14, 35, 58),
(15, 32, 59),
(16, 31, 53),
(17, 34, 51),
(18, 36, 60),
(19, 32, 55),
(20, 35, 56);

SELECT * FROM cliente;

SELECT * FROM pedido;


SELECT cliente.nome, pedido.id AS id_pedido
FROM cliente
LEFT JOIN pedido ON cliente.id = pedido.cliente_id;

SELECT cliente.nome, pedido.id AS id_pedido
FROM cliente
JOIN pedido ON cliente.id = pedido.cliente_id;

DROP TABLE pedido;
DROP TABLE produto;

SELECT cliente.nome, pedido.id AS id_pedido
FROM cliente
<<<<<<< HEAD
LEFT JOIN pedido ON cliente.id = pedido.cliente_id

=======
LEFT JOIN pedido ON cliente.id = pedido.cliente_id
>>>>>>> 95bf32b928d3c4cd02511cd346c088ad26c11ca7
