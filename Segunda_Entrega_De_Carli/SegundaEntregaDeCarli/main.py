from SegundaEntregaDeCarli.funciones import Cliente

cliente1 = Cliente("David", "De Carli", 32, 5, 0)
cliente2 = Cliente("juan", "Perez", 32, 3, 1)
cliente3 = Cliente("Diego", "Rodriguez", 17, 0, 1)


cliente2.tirar()

print(f"Porcentaje de aciertos de {cliente1.nombre}: {cliente1.calcular_aciertos()}%")
print(f"Porcentaje de aciertos de {cliente2.nombre}: {cliente2.calcular_aciertos()}%")