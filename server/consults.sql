//Reporte de ventas por agente
SELECT ag.ID, ag.Nombre, count(1)
	FROM Empleado as ag on te.id = em.Tipo
	JOIN Contrato as con on ag.Cedula = con.Agente
	JOIN Tipo_Contrato on con.Tipo = Tipo_Contrato.ID
WHERE Tipo_Contrato.Detalle = 'Compra'
GROUP BY ag.ID, ag.Nombre

//Reporte de inmuebles de un tipo especifico
SELECT Inmueble.ID, Inmueble.Nombre, Clasificacion.Nombre, ei.Nombre, Sector.Nombre,Ciudad.Nombre,Cliente.Nombre
FROM Inmueble
     JOIN Tipo_Inmueble as ti on Inmueble.Tipo = ti.ID
     JOIN Clasificacion on ti.Clasificacion = Clasificacion.ID
     JOIN Estado_Inmueble as ei on Inmueble.Estado = ei.ID
     JOIN Sector on Inmueble.Sector = Sector.ID
     JOIN Ciudad on Sector.ID_Ciudad = Ciudad.ID
     JOIN Cliente on Inmueble.Dueño = Cliente.Cedula
WHERE Tipo_Inmueble = [recuperado de vistas]

//Listado de inmuebles vendidos por sector
SELECT Sector.ID, count(DISTINCT Inmueble.ID)
FROM Contrato
    JOIN Inmueble on Contrato.Inmueble = Inmueble.ID
    JOIN Tipo_Contrato Contrato.Tipo = Tipo_Contrato.ID
    JOIN sector on Inmueble.Sector = Sector.ID
WHERE Tipo_Contrato.Detalle = 'Compra'
GROUP BY Sector.ID

//Reporte de inmuebles disponibles para la venta
SELECT Inmueble.ID, Inmueble.Nombre, Tipo_Inmueble.Nombre, Clasificacion.Nombre, ei.Nombre, Sector.Nombre,Ciudad.Nombre,Cliente.Nombre
FROM Contrato
    JOIN Inmueble on Contrato.Inmueble = Inmueble.id
    JOIN Tipo_Contrato on Contrato.Tipo = Tipo_Contrato.ID
    JOIN Tipo_Inmueble as ti on Inmueble.Tipo = ti.ID
    JOIN Clasificacion on ti.Clasificacion = Clasificacion.ID
    JOIN Estado_Inmueble as ei on Inmueble.Estado = ei.ID
    JOIN Sector on Inmueble.Sector = Sector.ID
    JOIN Ciudad on Sector.ID_Ciudad = Ciudad.ID
    JOIN Cliente on Inmueble.Dueño = Cliente.Cedula
WHERE Tipo_Contrato.Detalle = 'Venta'
    AND Inmueble.ID NOT IN (SELECT Inmueble.ID
                            FROM Contrato JOIN Inmueble on Contrato.Inmueble = Inmueble.id
                                JOIN Tipo_Contrato on Contrato.Tipo = Tipo_Contrato.ID
                            WHERE Tipo_Contrato.Detalle = 'Compra')

//Reporte de ventas realizadas en un rango de fechas
SELECT Inmueble.Nombre as Inmueble, Empleado.Nombre as Agente, Cliente.Nombre as Cliente
FROM Contrato JOIN Inmueble on Contrato.Inmueble = Inmueble.id
    JOIN Tipo_Contrato on Contrato.Tipo = Tipo_Contrato.ID
    JOIN Empleado JOIN Contrato.Agente = Empleado.Cedula
    JOIN Cliente on Contrato.Cliente = Cliente.Cedula
WHERE Tipo_Contrato.Detalle = 'Compra' and [Fecha_Inicio de vista] < Contrato.Fecha_Inicio and [Fecha_Fin de vista] > Contrato.Fecha_Inicio