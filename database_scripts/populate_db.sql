-- Inserindo dados na tabela usuario
INSERT INTO usuario (login, senha, cpf) VALUES
  ('admin', '123456', '111.222.333-44'),
  ('user1', 'senha123', '555.666.777-88');

-- Inserindo dados na tabela cliente
INSERT INTO cliente (nome, cpf, telefone) VALUES
  ('João Silva', '999.888.777-66', '11999998888'),
  ('Maria Souza', '888.777.666-55', '11988887777');

-- Inserindo dados na tabela forma_pagamento
INSERT INTO forma_pagamento (nome) VALUES
  ('Cartão de Crédito'),
  ('Boleto'),
  ('Pix');

-- Inserindo dados na tabela categoria
INSERT INTO categoria (nome) VALUES
  ('Eletrônicos'),
  ('Papelaria');

-- Inserindo dados na tabela produto
INSERT INTO produto (nome, preco, categoria_id, quantidade, unidade_medida) VALUES
  ('Notebook', 3500.00, 1, 10, 'unidade'),
  ('Caderno', 25.50, 2, 50, 'unidade');
