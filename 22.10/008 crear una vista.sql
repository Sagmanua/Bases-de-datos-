CREATE VIEW personas_correos AS 

SELECT
emails.direcciones,
personas.nombre,
personas.apellidos
FROM emails
LEFT JOIN personas
ON emails.personas = personas.idificador;

SELECT * FROM personas_correos;