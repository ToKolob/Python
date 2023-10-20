#constants
earth_acceleration_of_gravity = 9.80665
water_density = 998.2
water_dynamic_viscosity = 0.0010016

def water_column_height(tower_height, tank_height):
  return tower_height + (3*tank_height/4) 

def presure_gain_from_water_height(height):
  return (water_density*earth_acceleration_of_gravity*height)/1000

def pressure_loss_from_pipe(pipe_diameter,pipe_length, friction_factor, fluid_velocity):
  return (-friction_factor*pipe_length*water_density*(fluid_velocity**2))/(pipe_diameter*2000)

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
  """
  P is the lost pressure in kilopascals
  ρ is the density of water (water_density kilogram / meter3)
  v is the velocity of the water flowing through the pipe in meters / second
  n is the quantity of fittings
  """
  return -0.04 * water_density * (fluid_velocity**2) * quantity_fittings / 2000

def reynolds_number(hydraulic_diameter, fluid_velocity): 
  """
  R is the Reynolds number
  ρ is the density of water (water_density kilogram / meter3)
  d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter.
  v is the velocity of the water flowing through the pipe in meters / second
  μ is the dynamic viscosity of water (water_dynamic_viscosity Pascal seconds)
  """  

  return water_density * hydraulic_diameter * fluid_velocity / water_dynamic_viscosity 

def pressure_loss_from_pipe_reduction(larger_diameter,
  fluid_velocity, reynolds_number, smaller_diameter):

  k = (0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)

  return -k * water_density * (fluid_velocity ** 2) / 2000

def kpa_to_psi(kpa):
  return kpa * 0.145038


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = presure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    print(f"Pressure at house: {pressure:.1f} kilopascals or {kpa_to_psi(pressure):.1f} psi")


if __name__ == "__main__":
    main()

