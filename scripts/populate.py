# FEITO PELO GEMINI PRO

import sqlite3
import random
from faker import Faker
from datetime import timedelta

# Inicializa o Faker para gerar dados em português do Brasil
fake = Faker('pt_BR')

def conectar_banco():
    """Cria a conexão com o banco de dados SQLite."""
    try:
        conn = sqlite3.connect('database.db')
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None

def criar_tabelas(cursor):
    """Executa o script SQL para criar as tabelas no banco de dados."""
    schema = """
    -- Tabela de Pacientes
    CREATE TABLE IF NOT EXISTS Paciente (
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
    CREATE TABLE IF NOT EXISTS Funcionario (
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
    CREATE TABLE IF NOT EXISTS Medico (
        id_funcionario INTEGER PRIMARY KEY,
        CRM VARCHAR(20) UNIQUE,
        especialidade VARCHAR(100),
        FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
    );

    CREATE TABLE IF NOT EXISTS Tecnico (
        id_funcionario INTEGER PRIMARY KEY,
        especialidade VARCHAR(100),
        FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
    );

    CREATE TABLE IF NOT EXISTS Enfermagem (
        id_funcionario INTEGER PRIMARY KEY,
        COREN VARCHAR(20) UNIQUE,
        FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
    );

    -- Tabela de Consultas
    CREATE TABLE IF NOT EXISTS Consulta (
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
    CREATE TABLE IF NOT EXISTS Exame (
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
    CREATE TABLE IF NOT EXISTS Tipo (
        id_tipo INTEGER PRIMARY KEY,
        nome VARCHAR(50),
        descricao VARCHAR(200),
        preco REAL
    );

    -- Tabela associativa Exame_Tipo
    CREATE TABLE IF NOT EXISTS Exame_Tipo (
        id_exame INT,
        id_tipo INT,
        PRIMARY KEY(id_exame, id_tipo),
        FOREIGN KEY(id_exame) REFERENCES Exame(id_exame),
        FOREIGN KEY(id_tipo) REFERENCES Tipo(id_tipo)
    );

    -- Tabela de Receitas
    CREATE TABLE IF NOT EXISTS Receita (
        id_receita INTEGER PRIMARY KEY,
        descricao VARCHAR(200),
        data_emissao DATE
    );

    -- Relacionamento Consulta ↔ Receita
    CREATE TABLE IF NOT EXISTS Emite (
        id_consulta INT,
        id_receita INT,
        PRIMARY KEY(id_consulta, id_receita),
        FOREIGN KEY(id_consulta) REFERENCES Consulta(id_consulta),
        FOREIGN KEY(id_receita) REFERENCES Receita(id_receita)
    );

    -- Relacionamento Técnico ↔ Exame
    CREATE TABLE IF NOT EXISTS Analisa (
        id_tecnico INT,
        id_exame INT,
        data_analise DATE,
        PRIMARY KEY(id_tecnico, id_exame),
        FOREIGN KEY(id_tecnico) REFERENCES Tecnico(id_funcionario),
        FOREIGN KEY(id_exame) REFERENCES Exame(id_exame)
    );
    """
    cursor.executescript(schema)
    print("Tabelas criadas com sucesso (se não existiam).")

def popular_paciente(cursor, quantidade):
    """Popula a tabela Paciente com dados aleatórios."""
    convenios = ['Unimed', 'Bradesco Saúde', 'Amil', 'SulAmérica', 'NotreDame Intermédica', 'Hapvida', 'Particular']
    for _ in range(quantidade):
        nome = fake.name()
        sexo = random.choice(['M', 'F'])
        data_nasc = fake.date_of_birth(minimum_age=0, maximum_age=90)
        cpf = fake.cpf().replace('.','').replace('-','')
        telefone = fake.phone_number()
        email = f"{nome.split(' ')[0].lower()}.{fake.last_name().lower()}@example.com"
        endereco = fake.address()
        convenio = random.choice(convenios)
        cursor.execute("""
            INSERT INTO Paciente (data_nasc, nome, sexo, CPF, telefone, email, endereco, convenio)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (data_nasc, nome, sexo, cpf, telefone, email, endereco, convenio))
    print(f"{quantidade} pacientes inseridos.")

def popular_funcionario_e_especializacoes(cursor, qtd_total, qtd_medicos, qtd_tecnicos, qtd_enfermagem):
    """Popula as tabelas Funcionario, Medico, Tecnico e Enfermagem."""
    if qtd_total < (qtd_medicos + qtd_tecnicos + qtd_enfermagem):
        raise ValueError("A quantidade total de funcionários é menor que a soma das especializações.")

    ids_funcionarios = []
    # Listas de especialidades
    especialidades_medicas = ['Cardiologia', 'Dermatologia', 'Ortopedia', 'Pediatria', 'Ginecologia', 'Neurologia', 'Urologia']
    especialidades_tecnicas = ['Radiologia', 'Análises Clínicas', 'Enfermagem do Trabalho', 'Hemoterapia']

    for i in range(qtd_total):
        nome = fake.name()
        sexo = random.choice(['M', 'F'])
        data_nasc = fake.date_of_birth(minimum_age=20, maximum_age=65)
        cpf = fake.cpf().replace('.','').replace('-','')
        telefone = fake.phone_number()
        email = f"{nome.split(' ')[0].lower()}.{fake.last_name().lower()}@work-example.com"
        endereco = fake.address()
        data_admissao = fake.date_between(start_date='-15y', end_date='today')
        salario = round(random.uniform(2500.0, 25000.0), 2)

        cursor.execute("""
            INSERT INTO Funcionario (nome, data_nasc, sexo, CPF, telefone, email, endereco, data_admissao, salario)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nome, data_nasc, sexo, cpf, telefone, email, endereco, data_admissao, salario))
        ids_funcionarios.append(cursor.lastrowid)

    print(f"{qtd_total} funcionários inseridos.")
    
    # Garante que não haverá sobreposição de funcionários nas especializações
    random.shuffle(ids_funcionarios)
    
    # Popula Medico
    for i in range(qtd_medicos):
        id_func = ids_funcionarios.pop(0)
        crm = f"CRM/SP {random.randint(100000, 999999)}"
        especialidade = random.choice(especialidades_medicas)
        cursor.execute("INSERT INTO Medico (id_funcionario, CRM, especialidade) VALUES (?, ?, ?)", (id_func, crm, especialidade))
    print(f"{qtd_medicos} médicos inseridos.")

    # Popula Tecnico
    for i in range(qtd_tecnicos):
        id_func = ids_funcionarios.pop(0)
        especialidade = random.choice(especialidades_tecnicas)
        cursor.execute("INSERT INTO Tecnico (id_funcionario, especialidade) VALUES (?, ?)", (id_func, especialidade))
    print(f"{qtd_tecnicos} técnicos inseridos.")

    # Popula Enfermagem
    for i in range(qtd_enfermagem):
        id_func = ids_funcionarios.pop(0)
        coren = f"COREN-SP {random.randint(100000, 999999)}-ENF"
        cursor.execute("INSERT INTO Enfermagem (id_funcionario, COREN) VALUES (?, ?)", (id_func, coren))
    print(f"{qtd_enfermagem} enfermeiros(as) inseridos.")

def popular_tipo_exame(cursor):
    """Insere tipos de exame pré-definidos."""
    tipos = [
        ('Hemograma Completo', 'Análise das células sanguíneas.', 80.50),
        ('Colesterol Total e Frações', 'Mede os níveis de colesterol no sangue.', 65.00),
        ('Glicemia de Jejum', 'Mede o nível de açúcar no sangue.', 45.75),
        ('Raio-X do Tórax', 'Imagem diagnóstica do tórax.', 120.00),
        ('Ultrassonografia Abdominal', 'Imagem dos órgãos abdominais.', 250.00),
        ('Eletrocardiograma (ECG)', 'Avalia a atividade elétrica do coração.', 150.00)
    ]
    cursor.executemany("INSERT INTO Tipo (nome, descricao, preco) VALUES (?, ?, ?)", tipos)
    print(f"{len(tipos)} tipos de exame inseridos.")

def popular_consulta_e_relacionados(cursor, quantidade, ids_pacientes, ids_medicos):
    """Popula as tabelas Consulta, Receita e Emite."""
    status_pag = ['Pago', 'Pendente', 'Cancelado']
    status_cons = ['Realizada', 'Agendada', 'Cancelada']
    forma_pag = ['Cartão de Crédito', 'Débito', 'Dinheiro', 'Pix', 'Convênio']
    medicamentos = ['Dipirona 500mg', 'Paracetamol 750mg', 'Amoxicilina 500mg', 'Ibuprofeno 600mg', 'Omeprazol 20mg']

    for _ in range(quantidade):
        id_paciente = random.choice(ids_pacientes)
        id_medico = random.choice(ids_medicos)
        data_hora = fake.date_time_between(start_date='-2y', end_date='+30d')
        valor = round(random.uniform(100.0, 500.0), 2)
        status_consulta = random.choice(status_cons)
        if status_consulta == 'Cancelada':
            status_pagamento = 'Cancelado'
        else:
            status_pagamento = random.choice(status_pag[:-1])
        forma = random.choice(forma_pag)
        data_pagamento = None
        if status_pagamento == 'Pago':
            data_pagamento = fake.date_between(start_date=data_hora.date(), end_date=data_hora.date() + timedelta(days=5))

        cursor.execute("""
            INSERT INTO Consulta (data_hora, valor, status_consulta, status_pagamento, forma_pagamento, data_pagamento, id_paciente, id_medico)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (data_hora, valor, status_consulta, status_pagamento, forma, data_pagamento, id_paciente, id_medico))
        
        id_consulta = cursor.lastrowid

        # Chance de 50% de gerar uma receita para a consulta
        if status_consulta == 'Realizada' and random.choice([True, False]):
            desc_receita = f"Tomar {random.choice(medicamentos)} de {random.randint(6,12)} em {random.randint(6,12)} horas por {random.randint(3,10)} dias."
            data_emissao_receita = data_hora.date()
            cursor.execute("INSERT INTO Receita (descricao, data_emissao) VALUES (?, ?)", (desc_receita, data_emissao_receita))
            id_receita = cursor.lastrowid
            cursor.execute("INSERT INTO Emite (id_consulta, id_receita) VALUES (?, ?)", (id_consulta, id_receita))

    print(f"{quantidade} consultas inseridas (com possíveis receitas associadas).")

def popular_exame_e_relacionados(cursor, quantidade, ids_pacientes, ids_tecnicos, ids_tipos):
    """Popula as tabelas Exame, Exame_Tipo e Analisa."""
    status_ex = ['Aguardando Coleta', 'Em Análise', 'Concluído', 'Cancelado']
    status_pag = ['Pago', 'Pendente', 'Cancelado']
    forma_pag = ['Cartão de Crédito', 'Débito', 'Dinheiro', 'Pix', 'Convênio']

    for _ in range(quantidade):
        id_paciente = random.choice(ids_pacientes)
        data_solicitacao = fake.date_between(start_date='-2y', end_date='today')
        data_coleta = None
        status_exame = random.choice(status_ex)
        
        if status_exame != 'Aguardando Coleta':
             data_coleta = fake.date_between(start_date=data_solicitacao, end_date=data_solicitacao + timedelta(days=10))

        if status_exame == 'Cancelado':
            status_pagamento = 'Cancelado'
        else:
            status_pagamento = random.choice(status_pag[:-1])
        forma = random.choice(forma_pag)
        data_pagamento = None
        if status_pagamento == 'Pago':
            data_pagamento = fake.date_between(start_date=data_solicitacao, end_date=data_solicitacao + timedelta(days=5))

        cursor.execute("""
            INSERT INTO Exame (data_solicitacao, data_coleta, status_exame, status_pagamento, forma_pagamento, data_pagamento, id_paciente)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (data_solicitacao, data_coleta, status_exame, status_pagamento, forma, data_pagamento, id_paciente))
        id_exame = cursor.lastrowid

        # Associa 1 ou 2 tipos de exame ao exame criado
        tipos_para_exame = random.sample(ids_tipos, k=random.randint(1, 2))
        for id_tipo in tipos_para_exame:
            cursor.execute("INSERT INTO Exame_Tipo (id_exame, id_tipo) VALUES (?, ?)", (id_exame, id_tipo))

        # Se o exame está em análise ou concluído, um técnico o analisou
        if status_exame in ['Em Análise', 'Concluído'] and data_coleta:
            id_tecnico = random.choice(ids_tecnicos)
            data_analise = fake.date_between(start_date=data_coleta, end_date=data_coleta + timedelta(days=7))
            cursor.execute("INSERT INTO Analisa (id_tecnico, id_exame, data_analise) VALUES (?, ?, ?)", (id_tecnico, id_exame, data_analise))

    print(f"{quantidade} exames inseridos (com tipos e análises associados).")


def main():
    """Função principal para executar todo o processo de população."""
    
    # --- CONTROLE DE QUANTIDADE ---
    # Altere estes valores para definir quantos registros gerar
    QTD_PACIENTES = 100
    QTD_TOTAL_FUNCIONARIOS = 30
    QTD_MEDICOS = 10
    QTD_TECNICOS = 8
    QTD_ENFERMAGEM = 7
    QTD_CONSULTAS = 200
    QTD_EXAMES = 150
    # -----------------------------

    conn = conectar_banco()
    if conn:
        cursor = conn.cursor()
        
        # Habilita o uso de chaves estrangeiras
        cursor.execute("PRAGMA foreign_keys = ON;")
        
        # 1. Cria a estrutura de tabelas
        criar_tabelas(cursor)
        
        # 2. Popula as tabelas sem dependências externas fortes
        popular_paciente(cursor, QTD_PACIENTES)
        
        # 3. Popula funcionários e suas especializações
        popular_funcionario_e_especializacoes(cursor, QTD_TOTAL_FUNCIONARIOS, QTD_MEDICOS, QTD_TECNICOS, QTD_ENFERMAGEM)
        
        # 4. Popula tipos de exames
        popular_tipo_exame(cursor)

        # 5. Obtém os IDs gerados para usar como chaves estrangeiras
        ids_pacientes = [row[0] for row in cursor.execute("SELECT id_paciente FROM Paciente").fetchall()]
        ids_medicos = [row[0] for row in cursor.execute("SELECT id_funcionario FROM Medico").fetchall()]
        ids_tecnicos = [row[0] for row in cursor.execute("SELECT id_funcionario FROM Tecnico").fetchall()]
        ids_tipos_exame = [row[0] for row in cursor.execute("SELECT id_tipo FROM Tipo").fetchall()]

        # Validação para garantir que temos IDs para continuar
        if not all([ids_pacientes, ids_medicos, ids_tecnicos, ids_tipos_exame]):
            print("\nERRO: Não foi possível obter os IDs necessários das tabelas base. Abortando população de tabelas dependentes.")
            conn.close()
            return
            
        # 6. Popula as tabelas com dependências
        popular_consulta_e_relacionados(cursor, QTD_CONSULTAS, ids_pacientes, ids_medicos)
        popular_exame_e_relacionados(cursor, QTD_EXAMES, ids_pacientes, ids_tecnicos, ids_tipos_exame)

        # Salva (commit) as mudanças e fecha a conexão
        conn.commit()
        conn.close()
        print("\nProcesso de população concluído com sucesso!")

if __name__ == '__main__':
    main()
