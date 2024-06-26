CREATE TABLE Empleado(
	Cedula      VARCHAR(10) PRIMARY KEY,
	Nombre      TEXT NOT NULL,
	Telefono    TEXT NOT NULL,
	Email       TEXT NOT NULL,
	Direccion   TEXT NOT NULL
);

CREATE TABLE Ciudad(
	ID	    INT PRIMARY KEY,
	Nombre	VARCHAR
);

CREATE TABLE Sector(
	ID	        INT PRIMARY KEY,
	Nombre	    VARCHAR,
	ID_Ciudad	INT REFERENCES Ciudad(ID)
);

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
	ID	        INT PRIMARY KEY,
	Nombre	    TEXT
);

CREATE TABLE Caracteristica(
	ID	            INT PRIMARY KEY,
	Descripcion	    TEXT
);

CREATE TABLE Inmueble (
	ID                  INT PRIMARY KEY,
	Nombre	            TEXT UNIQUE,
	Direccion           TEXT NOT NULL,
	Sector 	            INT REFERENCES Sector(ID),
	Tipo	            INT REFERENCES Tipo_Inmueble(ID),
	Estado 	            INT REFERENCES Estado_Inmueble(ID),
	Anio_Construccion   SMALLINT NOT NULL,
	Area	            NUMERIC NOT NULL,
	Dueño	            VARCHAR(10) REFERENCES Cliente(Cedula)
);

CREATE TABLE Inmueble_Caracteristica(
	Inmueble	    INT REFERENCES Inmueble(ID),
	Caracteristica	INT REFERENCES Caracteristica(ID),
	Valor	        VARCHAR
);

CREATE TABLE Tipo_Contrato(
	ID	    INT PRIMARY KEY,
	Nombre	TEXT
);

CREATE TABLE Contrato (
	ID              INT PRIMARY KEY,
	Inmueble        INT REFERENCES Inmueble(ID),
	Cliente         VARCHAR(10) REFERENCES Cliente(Cedula),
	Agente          VARCHAR(10) REFERENCES Empleado(Cedula),
	Tipo	        INT REFERENCES Tipo_Contrato(ID),
	Fecha_Inicio    DATE,
	Fecha_Fin       DATE,
	Comision        NUMERIC,
	Precio_Venta    NUMERIC
);