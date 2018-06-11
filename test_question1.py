from question1 import base36_to_base10

def test_alpha_numeric_check():
	assert "error" in base36_to_base10("@as2")
def test_emty_string_check():
	assert "error" in base36_to_base10("")
def test_success_result():
	result = base36_to_base10("614z1")
	assert "data" in result
	assert result['data'] == 10130797
	result = base36_to_base10("ixqye")
	assert "data" in result
	assert result['data'] == 31807670