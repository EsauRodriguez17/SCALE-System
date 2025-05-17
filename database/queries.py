# Productos
GET_ALL_PRODUCTOS_WITH_STOCK = """
SELECT 
    p.id_producto, 
    p.nombre, 
    p.descripcion, 
    p.precio_base,               
    COALESCE(SUM(vp.stock), 0) AS stock_total, 
    pr.nombre AS proveedor,      
    c.nombre AS categoria        
FROM productos p
LEFT JOIN categorias c ON p.id_categoria = c.id_categoria
LEFT JOIN proveedores pr ON p.id_proveedor = pr.id_proveedor
LEFT JOIN variantes_producto vp ON p.id_producto = vp.id_producto
GROUP BY p.id_producto
ORDER BY p.id_producto ASC;
"""