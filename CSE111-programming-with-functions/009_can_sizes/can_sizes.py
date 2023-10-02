from math import pi
def cilinder_volume(radius,height):
  """Compute and return the volume of a cilinder."""
  volume = pi * radius**2 * height
  return volume

def surface_area_cilinder(radius,height):
  """Compute and return the surface area of a cilinder."""
  surface_area = 2 * pi * radius * (radius + height)
  return surface_area

def can_eficiency(radius,height):
  """Compute and return the efficiency of a can."""
  efficiency = cilinder_volume(radius,height) / surface_area_cilinder(radius,height)
  return efficiency

data = [
    ["#1 Picnic", 6.83, 10.16, "$0.28"],
    ["#1 Tall", 7.78, 11.91, "$0.43"],
    ["#2", 8.73, 11.59, "$0.45"],
    ["#2.5", 10.32, 11.91, "$0.61"],
    ["#3 Cylinder", 10.79, 17.78, "$0.86"],
    ["#5", 13.02, 14.29, "$0.83"],
    ["#6Z", 5.40, 8.89, "$0.22"],
    ["#8Z short", 6.83, 7.62, "$0.26"],
    ["#10", 15.72, 17.78, "$1.53"],
    ["#211", 6.83, 12.38, "$0.34"],
    ["#300", 7.62, 11.27, "$0.38"],
    ["#303", 8.10, 11.11, "$0.42"]]

def cost_efficiency():
  for item in data:
    efficiency = can_eficiency(item[1],item[2])
    price = item[3].replace("$","")

    return efficiency/price
   
def main():
  for item in data:
    eficiency = can_eficiency(item[1],item[2])
    price = float(item[3].replace("$",""))
    print(f"{item[0]}: {eficiency/price:.2f}")

main()