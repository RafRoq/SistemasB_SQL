SELECT
    t.nome AS "Tipo de Exame",
    COUNT(et.id_exame) AS "Quantidade Realizada",
    SUM(t.preco) AS "Valor Total Arrecadado"
FROM
    Tipo t
JOIN
    Exame_Tipo et ON t.id_tipo = et.id_tipo
GROUP BY
    t.id_tipo, t.nome
ORDER BY
    "Valor Total Arrecadado" DESC;
