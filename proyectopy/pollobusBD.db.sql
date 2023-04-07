BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "alumno" (
	"id_alumno"	INTEGER,
	"apellidoP"	TEXT,
	"apellidoM"	TEXT,
	"carrera"	TEXT,
	"matricula"	TEXT,
	"ruta"	TEXT,
	"turno"	TEXT,
	"tipoViaje"	TEXT,
	"nombre"	TEXT,
	PRIMARY KEY("id_alumno" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "operador" (
	"id_operador"	INTEGER,
	"apellidoP"	TEXT,
	"apellidoM"	TEXT,
	"NumEmpleado"	INTEGER,
	"licencia"	TEXT,
	"vigencia"	TEXT,
	"nombre"	TEXT,
	PRIMARY KEY("id_operador" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "autobus" (
	"id_autobus"	INTEGER,
	"modelo"	TEXT,
	"matricula"	TEXT,
	"NumAsientos"	INTEGER,
	"capacidadTanque"	TEXT,
	"marca"	TEXT,
	PRIMARY KEY("id_autobus" AUTOINCREMENT)
);
INSERT INTO "alumno" VALUES (1,'ed','es','zu','sis','1200','43','ves','1');
INSERT INTO "operador" VALUES (1,'es','zu',1234,'a','2134','ed');
INSERT INTO "autobus" VALUES (1,'2017','s123',4,'1000','huyn');
COMMIT;
