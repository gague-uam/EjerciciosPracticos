import clases.clases as c

cliente_regular = c.Cliente(1, "Gabriela Guerrero", "83694019", 0)
cliente_vip = c.Cliente(2, "Andrea de la Roca", "82367054", 30)

pedido_regular = [c.Pedido("comida", 100), c.Pedido("bebida", 50)]
pedido_vip = [c.Pedido("comida", 200), c.Pedido("bebida", 100)]

print("Total cliente regular:", cliente_regular.calcular_total(pedido_regular))
print("Total cliente VIP:", cliente_vip.calcular_total(pedido_vip))

