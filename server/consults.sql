//Reporte de ventas por agente
SELECT ag.ID, ag.Nombre, count(1)
	FROM Tipo_Empleado as te
	JOIN Empleado as ag on te.id = em.Tipo
	JOIN Contrato as con on ag.Cedula = con.Agente
	JOIN Tipo_Contrato on con.Tipo = Tipo_Contrato.ID
	WHERE te.Detalle = 'Agente' AND Tipo_Contrato.Detalle = 'Venta'
	GROUP BY ag.ID, ag.Nombre

