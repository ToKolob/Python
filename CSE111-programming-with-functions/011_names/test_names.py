from names import make_full_name,  extract_family_name, extract_given_name
import pytest

def test_make_full_name():

  assert make_full_name("Sally", "Brown") == "Brown; Sally"

  assert make_full_name("Lucas", "Nunes") == "Nunes; Lucas"

  assert make_full_name("James", "Creison") == "Creison; James"

pytest.main( ["-v", "--tb=line", "-rN", __file__ ] )

def test_extract_family_name():

  assert extract_family_name("Brown; Sally") == "Brown"

  assert extract_family_name("Nunes; Lucas") == "Nunes"

  assert extract_family_name("Ferguson; Jamescreison") == "Ferguson"

def test_extract_given_name():

  assert extract_given_name("Brown; Sally") == "Sally"

  assert extract_given_name("Nunes; Lucas") == "Lucas"

  assert extract_given_name("Ferguson; Jamescreison") == "Jamescreison"

pytest.main( ["-v", "--tb=line", "-rN", __file__ ] )