SELECT * FROM emails
LEFT JOIN personas
ON emails.personas = personas.idificador;s