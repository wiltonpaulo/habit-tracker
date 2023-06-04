-- Criação do banco de dados
CREATE DATABASE habittracker;

-- Utiliza o banco de dados recém-criado
\c habittracker;

-- Criação da tabela habit
CREATE TABLE habit (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  frequency VARCHAR(255) NOT NULL
);

-- Inserção de dados de exemplo
INSERT INTO habit (name, frequency) VALUES ('Exercise', 'Daily');
INSERT INTO habit (name, frequency) VALUES ('Read', 'Weekly');
INSERT INTO habit (name, frequency) VALUES ('Meditate', 'Daily');
