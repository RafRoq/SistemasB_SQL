SELECT
    p.nome AS "Nome do Paciente",
    c.id_consulta AS "ID da Consulta",
    COUNT(c.id_consulta) AS "Número de Consultas Pendentes",
    SUM(c.valor) AS "Total a Pagar"
FROM
    Paciente p
    Consultas c ON p.id_paciente = c.id_paciente
WHERE
    c.status_pagamento = 'Pendente'
HAVING
    COUNT(c.id_consulta) > 0
ORDER BY
    "Total a Pagar" ASC;