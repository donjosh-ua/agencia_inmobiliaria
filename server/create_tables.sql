CREATE TABLE Empleado(
	Cedula      VARCHAR(10) PRIMARY KEY,
	Nombre      TEXT NOT NULL,
	Telefono    TEXT NOT NULL,
	Email       TEXT NOT NULL,
	Direccion   TEXT NOT NULL,
	Tipo        TEXT
);

CREATE TABLE Ciudad(
	ID	    INT,
	Nombre	VARCHAR
)

CREATE TABLE Sector(
	ID	        INT,
	Nombre	    VARCHAR,
	ID_Ciudad	INT REFERENCES Ciudad(ID)
)

CREATE TABLE Cliente(
	Cedula      VARCHAR(10) PRIMARY KEY,
	Nombre      VARCHAR(100),
	Telefono    VARCHAR(15),
	Email       VARCHAR(100),
	Direccion   TEXT
);

CREATE TABLE Clasificacion(
	ID	    INT PRIMARY KEY,
	Nombre	TEXT NOT NULL
);

CREATE TABLE Tipo_Inmueble(
	ID	            INT PRIMARY KEY,
	Clasificacion 	INT REFERENCES Clasificacion(ID),
	Nombre	        TEXT
);

CREATE TABLE Estado_Inmueble(
	ID	    INT PRIMARY KEY,
	Nombre	TEXT
);

CREATE TABLE Caracteristica(
	ID	        INT PRIMARY KEY,
	Descripcion	TEXT,
)

CREATE TABLE Inmueble (
	ID                  INT PRIMARY KEY,
	Tipo	            INT REFERENCES Tipo_Inmueble(ID),
	Estado 	            INT REFERENCES Estado_Inmueble(ID),
	Sector 	            INT REFERENCES Sector(ID),
	Anio_Construccion   SMALLINT NOT NULL,
	Largo_Terreno	    NUMERIC NOT NULL,
	Ancho_Terreno	    NUMERIC NOT NULL,
	Dueño	            VARCHAR(10) REFERENCES Cliente(Cedula)
);

CREATE TABLE Inmueble_Caracteristica(
	ID	            INT PRIMARY KEY,
	Inmueble	    INT REFERENCES Inmueble(ID),
	Caracteristica	INT REFERENCES Caracteristica(ID),
	Valor	        VARCHAR
)

CREATE TABLE Tipo_Contrato(
	ID	    INT PRIMARY KEY,
	Nombre	TEXT
);

CREATE TABLE Contrato (
	ID              INT PRIMARY KEY,
	Inmueble        INT REFERENCES Inmueble(ID),
	Comprador       VARCHAR(10) REFERENCES Clientes(Cedula),
	Agente          VARCHAR(10) REFERENCES Empleado(Cedula),
	Tipo	        INT REFERENCES Tipo_Contrato(ID),
	Fecha_Venta     DATE,
	Precio_Venta    NUMERIC
);