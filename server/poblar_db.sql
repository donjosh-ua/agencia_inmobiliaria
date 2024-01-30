INSERT INTO Tipo_Contrato (ID, Nombre)
    VALUES  (1, 'Compra'),
            (2, 'Venta');

INSERT INTO Estado_Inmueble (ID, Nombre)
    VALUES  (1, 'Disponible'),
            (2, 'Vendido'),
            (3, 'Alquilado'),
            (4, 'No disponible');

INSERT INTO Clasificacion (ID, Nombre)
    VALUES  (1, 'Comercial'),
            (2, 'Residencial');

INSERT INTO Tipo_Inmueble (ID, Clasificacion, Nombre)
    VALUES  (1, 1, 'Local'),
            (2, 1, 'Oficina'),
            (3, 1, 'Bodega'),
            (4, 1, 'Terreno'),
            (5, 1, 'Edificio'),
            (6, 2, 'Casa'),
            (7, 2, 'Apartamento'),
            (8, 2, 'Finca'),
            (9, 1, 'Hotel'),
            (10, 1, 'Motel'),
            (11, 1, 'Hostal'),
            (12, 2, 'Cabaña'),
            (13, 2, 'Casa de campo'),
            (14, 2, 'Casa de playa'),
            (15, 2, 'Casa de montaña'),
            (16, 2, 'Casa de ciudad'),
            (17, 2, 'Casa de pueblo');

INSERT INTO Ciudad (ID, Nombre)
    VALUES  (1, 'Cuenca'),
            (2, 'Machala'),
            (3, 'Guayaquil'),
            (4, 'Quito'),
            (5, 'Loja');

INSERT INTO Sector (ID, Nombre, ID_Ciudad)
    VALUES  (1, 'Centro', 1),
            (2, 'Totoracocha', 1),
            (3, 'El Batan', 1),
            (4, 'El Vecino', 1);

INSERT INTO Caracteristica (ID, Descripcion)
    VALUES  (1, 'Piscina'),
            (2, 'Garaje'),
            (3, 'Patio'),
            (4, 'Jardin'),
            (5, 'Cancha'),
            (6, 'Baño'),
            (7, 'Cuarto'),
            (8, 'Oficina');