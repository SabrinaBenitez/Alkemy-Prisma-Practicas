-- Listar los nombres de los proveedores cuya ciudad contenga la cadena de texto “Ramos”.
SELECT Nombre
FROM Proveedor
WHERE Ciudad LIKE '%Ramos%'

/* Listar los códigos de los materiales que provea el proveedor 4 y
no los provea el proveedor 5. Se debe resolver de 3 formas*/
  
SELECT CodMat
FROM Provisto_Por
WHERE CodProv = 4 AND CodMat NOT IN (SELECT CodMat
FROM Provisto_Por
WHERE CodProv = 5)

SELECT CodMat
FROM Provisto_por pp
WHERE CodProv = 4 AND NOT EXISTS
(SELECT 1
FROM Provisto_por pp2
WHERE CodProv = 5 and pp.CodMat=pp2.CodMat)

SELECT CodMat
FROM Provisto_por
WHERE CodProv =4
EXCEPT
SELECT CodMat
FROM Provisto_por
WHERE CodProv = 5


/* Listar los materiales, código y descripción, provistos por proveedores 
de la ciudad de Ramos Mejía */

SELECT DISTINCT m.CodMat,m.Descripcion
FROM Material m inner join Provisto_Por pp on
m.CodMat =pp.CodMat inner join Proveedor p on 
p.CodProv = p.CodProv
WHERE P.Ciudad = 'Ramos mejia' 
/*Listar los proveedores y materiales que provee. La lista
resultante debe incluir a aquellos proveedores que no proveen ningún material.*/

SELECT p.CodProv,p.Nombre,m.CodMat,m.Descripcion
FROM Proveedor p left join
Provisto_Por pp on p.CodProv = pp.CodProv left join 
Material m on pp.CodMat=pp.CodMat  

/*Listar los artículos que cuesten más de $30 o que estén
compuestos por el material 2*/

SELECT a.CodArt
FROM Articulo a 
where a.Precio > 30
UNION
SELECT cp.CodArt
FROM Compuesto_Por cp
WHERE cp.CodMat = '2'

-- Listar los artículos de Mayor precio
SELECT CodArt,Descripcion,Precio
FROM Articulo
WHERE Precio = (SELECT max(Precio) FROM Articulo)
-- Listar los proveedores que proveen más de 3 materiales

SELECT pp.CodProv, count(pp.CodProv) as 'Cantidad Materiales'
FROM Provisto_Por pp
GROUP BY pp.CodProv
HAVING count(pp.CodProv)> 3

/* Crear una vista para el caso de los proveedores que proveen
más de 4 materiales. Mostrar la forma de invocar esa vista */

CREATE VIEW proveedor_provee_mas_de_4_Materiales as
SELECT pp.CodProv, count(pp.CodProv) as 'Cantidad Materiales'
FROM Provisto_Por pp
GROUP BY pp.CodProv
HAVING count(pp.CodProv)> 4


SELECT *
FROM proveedor_provee_mas_de_4_Materiales