select * from
cliente;
/*konsulta 1*/
select nombre as izena, apellidos as abizena from cliente 
where nombre IN ('José', 'Luis') 
order by nombre, apellidos;
/*kontsula 2*/
select nombre as izena, telefono as tel from cliente
where floor(DATEDIFF(CURDATE(), fechaNacimiento) / 365.2) BETWEEN 45 and 50;
/*kontsulta 3*/
select nombre, apellidos from cliente where telefono IS NULL;
/*kontsulta 4*/
select stock_seguridad, izena from articulo where stock_seguridad <4;
/*kontsulta 5*/
select izena, descripcion, img from articulo
where precio_unidad < 200;

