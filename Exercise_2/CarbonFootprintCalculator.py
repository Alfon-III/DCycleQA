class CarbonFootprintCalculator:
    def __init__(self, energy_consumption, transportation, waste):
        self.energy_consumption = energy_consumption
        self.transportation = transportation
        self.waste = waste

    def calculate_energy_footprint(self):
        return self.energy_consumption * 0.233
    
    def calculate_transportation_footprint(self):
        return self.transportation * 0.21
    
    def calculate_waste_footprint(self):
        return self.waste * 0.05

    def total_carbon_footprint(self):
        return (
            self.calculate_energy_footprint() +
            self.calculate_transportation_footprint() +
            self.calculate_waste_footprint()
        )
    

def get_user_carbon_footprint(user_data):
    calculator = CarbonFootprintCalculator(
        user_data['energy_consumption'],
        user_data['transportation'],
        user_data['waste']
    )
    return {
        'energy_footprint': calculator.calculate_energy_footprint(),
        'transportation_footprint': calculator.calculate_transportation_footprint(),
        'waste_footprint': calculator.calculate_waste_footprint(),
        'total_footprint': calculator.total_carbon_footprint()
    }


def get_comparison_with_average(user_footprint, average_footprint):
    return {
    'energy_difference': user_footprint['energy_footprint'] - average_footprint['energy_footprint'],
    'transportation_difference': user_footprint['transportation_footprint'] - average_footprint['transportation_footprint'],
    'waste_difference': user_footprint['waste_footprint'] - average_footprint['waste_footprint'],
    'total_difference': user_footprint['total_footprint'] - average_footprint['total_footprint']
    }