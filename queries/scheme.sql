-- Tabela de Pacientes
CREATE TABLE Paciente (
    id_paciente INTEGER PRIMARY KEY,
    data_nasc DATE,
    nome VARCHAR(100),
    sexo CHAR(1),
    CPF CHAR(11) UNIQUE,
    telefone VARCHAR(15),
    email VARCHAR(100),
    endereco VARCHAR(200),
    convenio VARCHAR(100)
);

-- Tabela de Funcionários
CREATE TABLE Funcionario (
    id_funcionario INTEGER PRIMARY KEY,
    nome VARCHAR(100),
    data_nasc DATE,
    sexo CHAR(1),
    CPF CHAR(11) UNIQUE,
    telefone VARCHAR(15),
    email VARCHAR(100),
    endereco VARCHAR(200),
    data_admissao DATE,
    salario REAL
);

-- Especializações de Funcionário
CREATE TABLE Medico (
    id_funcionario INTEGER PRIMARY KEY,
    CRM VARCHAR(20) UNIQUE,
    especialidade VARCHAR(100),
    FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
);

CREATE TABLE Tecnico (
    id_funcionario INTEGER PRIMARY KEY,
    especialidade VARCHAR(100),
    FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
);

CREATE TABLE Enfermagem (
    id_funcionario INTEGER PRIMARY KEY,
    COREN VARCHAR(20) UNIQUE,
    FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
);

-- Tabela de Consultas
CREATE TABLE Consulta (
    id_consulta INTEGER PRIMARY KEY,
    data_hora DATETIME,
    valor REAL,
    status_consulta VARCHAR(30),
    status_pagamento VARCHAR(30),
    forma_pagamento VARCHAR(30),
    data_pagamento DATE,
    id_paciente INT,
    id_medico INT,
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente),
    FOREIGN KEY (id_medico) REFERENCES Medico(id_funcionario)
);

-- Tabela de Exames
CREATE TABLE Exame (
    id_exame INTEGER PRIMARY KEY,
    data_solicitacao DATE,
    data_coleta DATE,
    status_exame VARCHAR(30),
    status_pagamento VARCHAR(30),
    forma_pagamento VARCHAR(30),
    data_pagamento DATE,
    id_paciente INT,
    FOREIGN KEY (id_paciente) REFERENCES Paciente(id_paciente)
);

-- Tabela de Tipos de Exame
CREATE TABLE Tipo (
    id_tipo INTEGER PRIMARY KEY,
    nome VARCHAR(50),
    descricao VARCHAR(200),
    preco REAL
);

-- Tabela associativa Exame_Tipo
CREATE TABLE Exame_Tipo (
    id_exame INT,
    id_tipo INT,
    PRIMARY KEY(id_exame, id_tipo),
    FOREIGN KEY(id_exame) REFERENCES Exame(id_exame),
    FOREIGN KEY(id_tipo) REFERENCES Tipo(id_tipo)
);

-- Tabela de Receitas
CREATE TABLE Receita (
    id_receita INTEGER PRIMARY KEY,
    descricao VARCHAR(200),
    data_emissao DATE
);

-- Relacionamento Consulta ↔ Receita
CREATE TABLE Emite (
    id_consulta INT,
    id_receita INT,
    PRIMARY KEY(id_consulta, id_receita),
    FOREIGN KEY(id_consulta) REFERENCES Consulta(id_consulta),
    FOREIGN KEY(id_receita) REFERENCES Receita(id_receita)
);

-- Relacionamento Técnico ↔ Exame
CREATE TABLE Analisa (
    id_tecnico INT,
    id_exame INT,
    data_analise DATE,
    PRIMARY KEY(id_tecnico, id_exame),
    FOREIGN KEY(id_tecnico) REFERENCES Tecnico(id_funcionario),
    FOREIGN KEY(id_exame) REFERENCES Exame(id_exame)
);