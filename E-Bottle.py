
import thermoelectric_module_library as thermoelectric  
import temperature_sensor_library as temperature_sensor  
cooling_pin = 2  
heating_pin = 3 
temperature_sensor_pin = 4  
thermoelectric.setup_cooling_module(cooling_pin)
thermoelectric.setup_heating_module(heating_pin)
temperature_sensor.setup_sensor(temperature_sensor_pin)
desired_temperature = 40

while True:
   
    current_temperature = temperature_sensor.read_temperature(temperature_sensor_pin)

   
    if current_temperature > desired_temperature:
        thermoelectric.turn_on_cooling(cooling_pin)
        thermoelectric.turn_off_heating(heating_pin)
    elif current_temperature < desired_temperature:
        thermoelectric.turn_off_cooling(cooling_pin)
        thermoelectric.turn_on_heating(heating_pin)
    else:
        thermoelectric.turn_off_cooling(cooling_pin)
        thermoelectric.turn_off_heating(heating_pin)
delay(1000)  
