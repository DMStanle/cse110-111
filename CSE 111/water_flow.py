#My exceeding of requirements can be found in lines 2-4 with constants defined and used thoughout the program.
earth_acceleration_of_gravity = 9.8066500
water_density = 998.2
water_dynamic_viscosity = 0.0010016

def water_column_height(tower_height, tank_height):
    height = 3 * tank_height
    height2 = height / 4
    height3 = tower_height + height2
    return height3

def pressure_gain_from_water_height(height):
    pressure = water_density * earth_acceleration_of_gravity
    pressure2 = pressure * height
    pressure3 = pressure2 / 1000
    return pressure3

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    lost_pressure = fluid_velocity**2
    lost_pressure2 = -friction_factor * pipe_length * water_density
    lost_pressure3 = lost_pressure * lost_pressure2
    lost_pressure4 = 2000 * pipe_diameter
    lost_pressure5 = lost_pressure3 / lost_pressure4
    return lost_pressure5

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    flp = fluid_velocity**2
    flp2 = -0.04 * water_density * flp * quantity_fittings
    flp3 = flp2 / 2000
    return flp3

def reynolds_number(hydraulic_diameter, fluid_velocity):
    rn = water_density * hydraulic_diameter * fluid_velocity / water_dynamic_viscosity
    return rn

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    plpr = 50 / reynolds_number
    plpr2 = plpr + 0.1
    plpr3 = larger_diameter / smaller_diameter
    plpr4 = plpr3**4 - 1
    plpr5 = plpr2 * plpr4

    plpr6 = fluid_velocity**2
    plpr7 = -plpr5 * water_density * plpr6
    plpr8 = plpr7 / 2000

    return plpr8

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
    pressure = pressure_gain_from_water_height(water_height)
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
    print(f"Pressure at house: {pressure:.1f} kilopascals")
if __name__ == "__main__":
    main()