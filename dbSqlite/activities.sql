BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS `activities` (
	`cod`	TEXT NOT NULL,
	`description`	TEXT NOT NULL,
	`und`	TEXT NOT NULL,
	`value`	NUMERIC NOT NULL,
	PRIMARY KEY(`cod`)
);
COMMIT;
