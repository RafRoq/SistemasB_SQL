CREATE VIEW melhor_cliente_f AS SELECT
    p.nome AS "Nome do Paciente",
    COUNT(c.id_consulta) AS "Número de Consultas",
    SUM(c.valor) AS "Total Gasto em Consultas"
FROM
    Paciente p
JOIN
    Consulta c ON p.id_paciente = c.id_paciente
WHERE
    p.sexo = 'F'
GROUP BY
    p.id_paciente, p.nome
HAVING
    COUNT(c.id_consulta) > 0
ORDER BY
    "Total Gasto em Consultas" DESC;