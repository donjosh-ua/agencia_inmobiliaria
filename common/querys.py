def vendidos_por_temporada(fecha_inicio, fecha_fin):
    return f"SELECT Inmueble.Nombre as Inmueble, Empleado.Nombre as Agente, Cliente.Nombre as Cliente"\
           f" FROM Contrato JOIN Inmueble on Contrato.Inmueble = Inmueble.id"\
           f" JOIN Tipo_Contrato on Contrato.Tipo = Tipo_Contrato.ID"\
           f" JOIN Empleado on Contrato.Agente = Empleado.Cedula"\
           f" JOIN Cliente on Contrato.Cliente = Cliente.Cedula"\
           f" WHERE Tipo_Contrato.Nombre = 'Compra' "\
           f" and '{fecha_inicio}' < Contrato.Fecha_Inicio "\
           f" and '{fecha_fin}' > Contrato.Fecha_Fin"


def inmuebles_para_venta():
    return f"SELECT Inmueble.ID, Inmueble.Nombre, ti.Nombre, Clasificacion.Nombre, ei.Nombre, Sector.Nombre,Ciudad.Nombre,Cliente.Nombre"\
           f" FROM Contrato"\
           f" JOIN Inmueble on Contrato.Inmueble = Inmueble.id"\
           f" JOIN Tipo_Contrato on Contrato.Tipo = Tipo_Contrato.ID"\
           f" JOIN Tipo_Inmueble as ti on Inmueble.Tipo = ti.ID"\
           f" JOIN Clasificacion on ti.Clasificacion = Clasificacion.ID"\
           f" JOIN Estado_Inmueble as ei on Inmueble.Estado = ei.ID"\
           f" JOIN Sector on Inmueble.Sector = Sector.ID"\
           f" JOIN Ciudad on Sector.ID_Ciudad = Ciudad.ID"\
           f" JOIN Cliente on Inmueble.Dueño = Cliente.Cedula"\
           f" WHERE ti.Nombre = 'Venta'"\
           f" AND Inmueble.ID NOT IN (SELECT Inmueble.ID"\
           f" FROM Contrato JOIN Inmueble on Contrato.Inmueble = Inmueble.id"\
           f" JOIN Tipo_Contrato on Contrato.Tipo = Tipo_Contrato.ID"\
           f" WHERE Tipo_Contrato.Nombre = 'Compra')"


def inmuebles_vendidos_x_sector():
    return f"SELECT Sector.ID, Sector.Nombre, count(DISTINCT Inmueble.ID)"\
           f" FROM Contrato"\
           f" JOIN Inmueble on Contrato.Inmueble = Inmueble.ID"\
           f" JOIN Tipo_Contrato on Contrato.Tipo = Tipo_Contrato.ID"\
           f" JOIN sector on Inmueble.Sector = Sector.ID"\
           f" WHERE Tipo_Contrato.Nombre = 'Compra'"\
           f" GROUP BY Sector.ID"


def inmuebles_tipo_especifico(tipo):
    return f"SELECT Inmueble.ID, Inmueble.Nombre, Clasificacion.Nombre, ei.Nombre, Sector.Nombre, Ciudad.Nombre, Cliente.Nombre"\
           f" FROM Inmueble"\
           f" JOIN Tipo_Inmueble as ti on Inmueble.Tipo = ti.ID"\
           f" JOIN Clasificacion on ti.Clasificacion = Clasificacion.ID"\
           f" JOIN Estado_Inmueble as ei on Inmueble.Estado = ei.ID"\
           f" JOIN Sector on Inmueble.Sector = Sector.ID"\
           f" JOIN Ciudad on Sector.ID_Ciudad = Ciudad.ID"\
           f" JOIN Cliente on Inmueble.Dueño = Cliente.Cedula"\
           f" WHERE ti.Nombre = '{tipo}'"


def ventas_x_agente():
    return f"SELECT ag.Cedula, ag.Nombre, count(1)"\
           f" FROM Empleado as ag"\
           f" JOIN Contrato as con on ag.Cedula = con.Agente"\
           f" JOIN Tipo_Contrato on con.Tipo = Tipo_Contrato.ID"\
           f" WHERE Tipo_Contrato.Nombre = 'Compra'"\
           f" GROUP BY ag.Cedula, ag.Nombre"
