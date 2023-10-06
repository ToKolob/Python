def wind_chill(temperature, wind):
  chill_factor = 35.74 + (0.6215 * temperature) - (35.75 * (wind ** 0.16)) + (0.4275 * temperature * (wind ** 0.16))
  return round(chill_factor, 1)

def heat_index(temperature, humidity):
  heat_index = (-42.379 +
    (2.04901523 * temperature) +
    (10.14333127 * humidity) -
    (0.22475541 * temperature * humidity) -
    (0.00683783 * (temperature ** 2)) -
    (0.05481717 * (humidity ** 2)) +
    (0.00122874 * (temperature ** 2) * humidity) +
    (0.00085282 * (temperature * humidity ** 2)) -
    (0.00000199 * (temperature ** 2) * (humidity ** 2)))
  
  return round(heat_index, 1)
