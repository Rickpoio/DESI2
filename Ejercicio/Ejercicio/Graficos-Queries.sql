#Cada una de estas consultas se usa para generar los graficos o KPI en metabase
#para crearse en metabase deben ejecutarse individualmente como nuevas preguntas 

#Consultas para generacion de KPI
#KPI de ingresos totales 
SELECT SUM(subtotal) AS `Ingresos Totales` 
FROM vista_analisis_ventas;

#KPI de ganacia bruta 
SELECT SUM(ganancia) AS `Ganancia Bruta` 
FROM vista_analisis_ventas;

#KPI de total de transacciones 
SELECT COUNT(DISTINCT venta_id) AS `Total Transacciones` 
FROM vista_analisis_ventas;

#KPI de ticket promedio 
SELECT SUM(subtotal) / COUNT(DISTINCT venta_id) AS `Ticket Promedio` 
FROM vista_analisis_ventas;

#Consultas para generacion de Graficos
#Grafico de evolucion temporal 
SELECT 
    DATE(fecha) AS fecha,
    SUM(subtotal) AS `Ventas Totales`,
    SUM(ganancia) AS `Ganancia Bruta`
FROM vista_analisis_ventas
GROUP BY DATE(fecha)
ORDER BY fecha ASC;

#grafico de categorias mas rentables 
SELECT 
    categoria,
    SUM(ganancia) AS ganancia_total,
    SUM(subtotal) AS ventas_totales
FROM vista_analisis_ventas
GROUP BY categoria
ORDER BY ganancia_total DESC;

#grafico de metodos de pago 
SELECT 
    metodo_pago,
    SUM(subtotal) AS total_facturado
FROM vista_analisis_ventas
GROUP BY metodo_pago;

#Grafico de desempeño de vendedores 
SELECT 
    COALESCE(vendedor, 'Sin Asignar') AS Vendedor,
    COUNT(DISTINCT venta_id) AS `Cant Ventas`,
    SUM(subtotal) AS `Total Facturado`,
    SUM(ganancia) AS `Ganancia Generada`
FROM vista_analisis_ventas
GROUP BY vendedor
ORDER BY `Total Facturado` DESC;
