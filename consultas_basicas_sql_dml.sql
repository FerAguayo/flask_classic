/*Seleccionar todos los registros de una tabla */
SELECT * FROM movements;
/*Seleccionar algunos campos de una tabla base de datos */
SELECT concept,quantity FROM movements;
/*Para insertar nuevos registros en la tabla*/
/*INSERT INTO movements(date,concept,quantity) VALUES("2026-02-12","extra trabajo",100);*/
/*Para actualizar registros de la tabla de base de datos, siempre hay que usar el WHERE sino cambia todos */
/*UPDATE movements SET concept = "Almuerzo", quantity = -50 WHERE id = 2;*/
/*Seleccionar con WHERE*/
/SELECT * FROM movements WHERE quantity<0;
/*Borrar registros, siempre poner el WHERE sino borramos todo*/
/*DELETE FROM movements WHERE id = 2;*/
/*Consultar SELECT con orden aplicado*/
SELECT * FROM movements ORDER BY quantity DESC;