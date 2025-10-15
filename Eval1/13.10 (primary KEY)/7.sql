INSERT INTO clientes VALUES(
	NULL,
	'12345678a',
	'Bohdan',
	'Sydorenko',
	'info@gmail.com'
);

ERROR 1265 (01000): Data truncated for column 'id' at row 1

INSERT INTO clientes VALUES(
	1,
	'12345678Z',
	'Bohdan',
	'Sydorenko',
	'infogmail.com'
);

