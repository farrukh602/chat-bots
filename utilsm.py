import numpy as np
import matplotlib.pyplot as plt

def convert_units_si_english(value, quantity_type, current_system):
    """
    Convert a value from SI to English system or vice versa.
    
    Parameters:
    value (float): The value to be converted.
    quantity_type (str): The type of quantity (e.g., 'mass', 'length', 'force', 'energy', etc.).
    system (str): The system of the input value ('SI' or 'English').
    
    Returns:
    float: The converted value.
    str: The system of the converted value ('SI' or 'English').
    """
    
    # Conversion factors between SI and English systems
    conversion_factors = {
        'mass': {'SI_to_English': 2.20462, 'English_to_SI': 0.453592,"SI_unit":"kg", "English_unit":"lbm"},  # kg to lbm and vice versa
        'length': {'SI_to_English': 3.28084, 'English_to_SI': 0.3048,"SI_unit":"m", "English_unit":"ft"},  # meter to feet and vice versa
        'time': {'SI_to_English': 1, 'English_to_SI': 1,"SI_unit":"sec", "English_unit":"sec"},  # second to second (same in both systems)
        'force': {'SI_to_English': 0.224809, 'English_to_SI': 4.44822,"SI_unit":"N", "English_unit":"lbm"},  # newton to lbf and vice versa
        'acceleration': {'SI_to_English': 3.28084, 'English_to_SI': 0.3048,"SI_unit":"m/s²", "English_unit":"ft/s²"},  # m/s² to ft/s² and vice versa
        'gravitational_acceleration': {'SI_to_English': 3.28084, 'English_to_SI': 0.3048,"SI_unit":"m/s²", "English_unit":"ft/s²"},  # m/s² to ft/s² and vice versa
        'energy': {'SI_to_English': 0.000947817, 'English_to_SI': 1055.06,"SI_unit":"joule", "English_unit":"Btu"},  # joule to Btu and vice versa
        'work': {'SI_to_English': 0.737562, 'English_to_SI': 1.35582,"SI_unit":"joule", "English_unit":"ft.lbf"},  # joule to ft·lbf and vice versa
        'specific_weight': {'SI_to_English': 0.06243, 'English_to_SI': 16.0185,"SI_unit":"N/m³", "English_unit":"lbf/ft³"},  # N/m³ to lbf/ft³ and vice versa
        'density': {'SI_to_English': 0.06243, 'English_to_SI': 16.0185,"SI_unit":"kg/m³", "English_unit":"lbm/ft³"},  # kg/m³ to lbm/ft³ and vice versa
    }
    
    quantity_type = quantity_type.lower()

    if quantity_type not in conversion_factors:
        raise ValueError(f"Quantity type '{quantity_type}' is not supported.")
    

    current_system = current_system.lower() # to make the system parameter case insensitive

    if current_system == 'si':
        converted_value = value * conversion_factors[quantity_type]['SI_to_English']
        return converted_value, conversion_factors[quantity_type]['English_unit']
    
    elif current_system == 'english':
        converted_value = value * conversion_factors[quantity_type]['English_to_SI']
        return converted_value, conversion_factors[quantity_type]['SI_unit']
    
    else:
        raise ValueError("System must be either 'SI' or 'English'.")
