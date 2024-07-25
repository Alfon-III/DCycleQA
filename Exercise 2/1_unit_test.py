from CarbonFootprintCalculator import CarbonFootprintCalculator

cfc = CarbonFootprintCalculator(
    energy_consumption=100,
    transportation=20,
    waste=30
)

cfc.total_carbon_footprint()


# Falta de Parámetro
cfc = CarbonFootprintCalculator(
    energy_consumption=100,
    transportation=20,
)

# Valores negativos (sería posible si por ejemplo tuviera una placa solar, y la energía le saliera negativa pues genera más de la que consume)

cfc = CarbonFootprintCalculator(
    energy_consumption=-5,
    transportation=10,
)
