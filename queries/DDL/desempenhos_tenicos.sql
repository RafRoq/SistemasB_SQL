SELECT
    f.nome AS "Nome do Técnico",
    COUNT(a.id_exame) AS "Número de Exames Analisados"
FROM
    Funcionario f
JOIN
    Tecnico t ON f.id_funcionario = t.id_funcionario
JOIN
    Analisa a ON t.id_funcionario = a.id_tecnico
GROUP BY
    f.id_funcionario, f.nome
ORDER BY
    "Número de Exames Analisados" DESC;