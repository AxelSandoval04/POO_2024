nombre_producto = input("Ingrese el nombre o descripción del producto: ")
codigo_producto = input("Ingrese el código del producto: ")
cantidad = int(input("Ingrese la cantidad del producto: "))
precio_unitario = float(input("Ingrese el precio unitario del producto: "))
    
    # Definir el porcentaje de IVA
IVA = 0.16
    
    # Calcular el descuento basado en la cantidad
if 1 <= cantidad <= 5:
        descuento = 0.10
elif 6 <= cantidad <= 10:
        descuento = 0.15
elif cantidad > 10:
        descuento = 0.20
else:
        descuento = 0

    # Calcular el precio total sin IVA y sin descuento
subtotal = cantidad * precio_unitario
    
    # Calcular el descuento
monto_descuento = subtotal * descuento
subtotal_con_descuento = subtotal - monto_descuento
    
    # Calcular el IVA sobre el subtotal con descuento
monto_iva = subtotal_con_descuento * IVA
    
    # Calcular el total a pagar
total_a_pagar = subtotal_con_descuento + monto_iva
    
    # Mostrar los resultados

print("\nDetalles del producto:")
print(f"Nombre/Descripción: {nombre_producto}")
print(f"Código: {codigo_producto}")
print(f"Cantidad: {cantidad}")
print(f"Precio unitario: ${precio_unitario:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Descuento aplicado: {descuento*100}%")
print(f"Monto de descuento: ${monto_descuento:.2f}")
print(f"Subtotal con descuento: ${subtotal_con_descuento:.2f}")
print(f"IVA (16%): ${monto_iva:.2f}")
print(f"Total a pagar: ${total_a_pagar:.2f}")