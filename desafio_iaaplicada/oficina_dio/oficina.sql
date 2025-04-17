
CREATE DATABASE IF NOT EXISTS Oficina;
USE Oficina;

-- Tabela Cliente
CREATE TABLE Cliente (
    ID_Cliente INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100),
    Telefone VARCHAR(20),
    Email VARCHAR(100),
    Tipo ENUM('PF', 'PJ'),
    CPF_PJ VARCHAR(20)
);

-- Tabela Veiculo
CREATE TABLE Veiculo (
    ID_Veiculo INT AUTO_INCREMENT PRIMARY KEY,
    Placa VARCHAR(10) UNIQUE,
    Modelo VARCHAR(50),
    Marca VARCHAR(50),
    Ano INT,
    ID_Cliente INT,
    FOREIGN KEY (ID_Cliente) REFERENCES Cliente(ID_Cliente)
);

-- Tabela Equipe
CREATE TABLE Equipe (
    ID_Equipe INT AUTO_INCREMENT PRIMARY KEY,
    Nome_Equipe VARCHAR(100)
);

-- Tabela Mecânico
CREATE TABLE Mecanico (
    ID_Mecanico INT AUTO_INCREMENT PRIMARY KEY,
    Nome VARCHAR(100),
    Especialidade VARCHAR(100)
);

-- Tabela Ordem de Serviço
CREATE TABLE Ordem_Servico (
    ID_OS INT AUTO_INCREMENT PRIMARY KEY,
    Data_Criacao DATE,
    Data_Entrega_Prevista DATE,
    ID_Veiculo INT,
    ID_Equipe INT,
    FOREIGN KEY (ID_Veiculo) REFERENCES Veiculo(ID_Veiculo),
    FOREIGN KEY (ID_Equipe) REFERENCES Equipe(ID_Equipe)
);

-- Tabela Serviço
CREATE TABLE Servico (
    ID_Servico INT AUTO_INCREMENT PRIMARY KEY,
    Descricao VARCHAR(200),
    Valor DECIMAL(10, 2)
);

-- Relacionamento N:N entre Ordem_Servico e Servico
CREATE TABLE Ordem_Servico_Servico (
    ID_OS INT,
    ID_Servico INT,
    PRIMARY KEY (ID_OS, ID_Servico),
    FOREIGN KEY (ID_OS) REFERENCES Ordem_Servico(ID_OS),
    FOREIGN KEY (ID_Servico) REFERENCES Servico(ID_Servico)
);

-- Relacionamento N:N entre Equipe e Mecânico
CREATE TABLE Equipe_Mecanico (
    ID_Equipe INT,
    ID_Mecanico INT,
    PRIMARY KEY (ID_Equipe, ID_Mecanico),
    FOREIGN KEY (ID_Equipe) REFERENCES Equipe(ID_Equipe),
    FOREIGN KEY (ID_Mecanico) REFERENCES Mecanico(ID_Mecanico)
);
