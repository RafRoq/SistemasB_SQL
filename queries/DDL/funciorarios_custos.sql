SELECT
    'Medico' AS "Categoria",
    COUNT(f.id_funcionario) AS "Número de Funcionários",
    SUM(f.salario) AS "Total Gasto com Salários"
FROM
    Medico m
JOIN
    Funcionario f ON m.id_funcionario = f.id_funcionario

UNION

SELECT
    'Tecnico' AS "Categoria",
    COUNT(f.id_funcionario),
    SUM(f.salario)
FROM
    Tecnico t
JOIN
    Funcionario f ON t.id_funcionario = f.id_funcionario

UNION

SELECT
    'Enfermagem' AS "Categoria",
    COUNT(f.id_funcionario),
    SUM(f.salario)
FROM
    Enfermagem e
JOIN
    Funcionario f ON e.id_funcionario = f.id_funcionario

ORDER BY
    "Total Gasto com Salários" DESC;
