from weather import wind_chill, heat_index
import pytest
from pytest import approx

def test_wind_chill():
  assert wind_chill(temperature=0, wind=3) == approx(-6.9)

  assert wind_chill(temperature=-5, wind=5) == approx(-16.4)

  assert wind_chill(temperature=-10, wind=3) == approx(-18.2)

def test_heat_index():  
  assert heat_index(temperature=80, humidity=80) == approx(84.2)
  assert heat_index(temperature=85, humidity=80) == approx(96.8)
  assert heat_index(temperature=96, humidity=70) == approx(126.4)


pytest.main(["-v", "--tb=no", ".\CSE111-programming-with-functions\009_weather\test_weather.py"])