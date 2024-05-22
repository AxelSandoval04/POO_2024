# Crear un programa que calcule y obtenga el total a pagar por un producto determinado. Se deberá de solicitar el nombre
# o descripccion del producto, codigo, cantidad del producto, precio unitario.
# El total a pagar incluye el IVA y el descuento.
# si se compran de 1 a 5 productos se otorga el 10% de descuento si se compran de 6 a 10 se apllica el 15% de descuento
# y si se compran mas de 10 se aplica el 20& de descuento
producto=int(input("Ingrese el precio del producto que desea comprar "))
cantidad=int(input("Cuantas unidades comprará: "))
if cantidad<=5:
    descuento=(producto*10) /100
    print("el descuento es de:",descuento)
elif cantidad<=10:
    descuento=(producto*15) /100
    print("el descuento es de:",descuento)
elif cantidad<=20:
    descuento=(producto*20) /100
    print("el descuento es de:",descuento)
precio=producto*cantidad
Iva=precio*.16
total=Iva+precio-descuento
print("El iva es",Iva," y el descuento es de", descuento,"asi que el total a pagar es ",total)



