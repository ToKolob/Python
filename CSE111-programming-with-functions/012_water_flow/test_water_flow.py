from pytest import approx
import pytest
from water_flow import water_column_height, presure_gain_from_water_height, pressure_loss_from_pipe

def test_water_column_height():
  # inputs: tower_height, tank_height
  # outputs: water column height
  assert water_column_height(0, 0) == approx(0)
  assert water_column_height(0, 10) == approx(7.5)
  assert water_column_height(25, 0) == approx(25)
  assert water_column_height(48.3, 12.8) == approx(57.9)

def test_presure_gain_from_water_height():
  # Test that the presure gain from water height is correct, within 0.001 of tolerance
  # inputs: height
  # outputs: presure gain
  assert presure_gain_from_water_height(0) == approx(0, abs=0.001)
  assert presure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
  assert presure_gain_from_water_height(50) == approx(489.450, abs=0.001)

def test_pressure_loss_from_pipe():
  # Test that the pressure loss from pipe is correct, within 0.001 of tolerance
  # inputs: pipe_diameter, pipe_length, friction_factor, fluid_velocity
  # outputs: pressure loss

  test_data = [
    (0.048692, 0, 0.018, 1.75, 0, 0.001),
    (0.048692, 200, 0, 1.75, 0, 0.001),
    (0.048692, 200, 0.018, 0, 0, 0.001),
    (0.048692, 200, 0.018, 1.75, -113.008, 0.001),
    (0.048692, 200, 0.018, 1.65, -100.462, 0.001),
    (0.28687, 1000, 0.013, 1.65, -61.576, 0.001),
    (0.28687, 1800.75, 0.013, 1.65, -110.884, 0.001),
  ]
  #[0]Pipe diameter, [1]pipe length, [2]friction factor, [3]fluid velocity, [4]expected pressure loss, [5]tolerance
  for line in test_data:
    assert pressure_loss_from_pipe(line[0], line[1], line[2], line[3]) == approx(line[4], abs=0.001)


pytest.main( ["-v", "--tb=line", "-rN", __file__] )

