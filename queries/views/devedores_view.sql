CREATE VIEW devedores_consulta AS SELECT
    p.id_paciente AS "ID do Paciente",
    p.nome AS "Nome do Paciente",
    COUNT(c.id_consulta) AS "Número de Pagamento Pendentes",
    SUM(c.valor) AS "Total a Pagar"
FROM
    Paciente p
JOIN
    Consulta c ON p.id_paciente = c.id_paciente
WHERE
    c.status_pagamento = 'Pendente'
GROUP BY 
    p.id_paciente
HAVING
    COUNT(c.id_consulta) > 0
ORDER BY
    "Total a Pagar" DESC;