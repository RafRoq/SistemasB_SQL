--CREATE UNIQUE INDEX idx_paciente_cpf ON Paciente(CPF);
--CREATE UNIQUE INDEX idx_funcionario_cpf ON Funcionario(CPF);

--Otimiza pesquisa
CREATE INDEX idx_consulta_paciente ON Consulta(id_paciente);
CREATE INDEX idx_consulta_medico ON Consulta(id_medico);
CREATE INDEX idx_exame_paciente ON Exame(id_paciente);
