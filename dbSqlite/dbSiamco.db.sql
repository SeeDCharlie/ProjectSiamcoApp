BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `users` (
	`idUser`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`userName`	TEXT NOT NULL,
	`name`	TEXT NOT NULL,
	`lastName`	INTEGER NOT NULL,
	`pass`	TEXT NOT NULL,
	`phone`	NUMERIC
);
INSERT INTO `users` (idUser,userName,name,lastName,pass,phone) VALUES (1,'admuno','carlos','castillo','admuno',16513),
 (2,'admdos','rufino','castillo','admdos',16513536);
CREATE TABLE IF NOT EXISTS `activities` (
	`cod`	TEXT NOT NULL,
	`description`	TEXT NOT NULL,
	`und`	TEXT NOT NULL,
	`value`	NUMERIC NOT NULL,
	PRIMARY KEY(`cod`)
);
COMMIT;
