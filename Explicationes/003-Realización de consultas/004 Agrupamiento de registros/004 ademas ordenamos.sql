SELECT COUNT(color)
FROM productos; -- resume

SELECT COUNT(color),color
FROM productos
GROUP BY color
ORDER BY COUNT(color) ASC;