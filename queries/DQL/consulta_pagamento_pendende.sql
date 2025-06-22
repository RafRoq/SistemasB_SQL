SELECT 
    SUM(c.valor) AS "Valor Total Pendente",
    COUNT(c.id_consulta) AS "Número de Consultas Pagamento Pendentes"
FROM 
    consulta c
WHERE
    c.status_pagamento = 'Pendente'