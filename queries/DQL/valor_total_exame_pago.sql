SELECT
    SUM(t.preco) AS "Valor Total Pago",
    COUNT(e.id_exame) AS "Número de Exames Pagos"
FROM
    Exame e
JOIN
    Exame_Tipo et ON e.id_exame = et.id_exame
JOIN
    Tipo t ON et.id_tipo = t.id_tipo
WHERE
    e.status_pagamento = 'Pago';