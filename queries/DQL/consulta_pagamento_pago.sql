SELECT 
    SUM(c.valor) AS "Valor Total Pago",
    COUNT(c.id_consulta) AS "Número de Consultas Pagamento Pago"
FROM 
    consulta c
WHERE
    c.status_pagamento = 'Pago'