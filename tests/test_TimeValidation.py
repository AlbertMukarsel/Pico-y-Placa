import pytest
from inputValidations import checkInput

testTimeData=[
    ("00:00","Time",True),
    ("23:59","Time",True),
    ("24:00","Time",False),
    ("30:60","Time",False),
    ("01:30","Time",True),
    ("15:30","Time",True),
    ("12:01","Time",True),
    ("12:60","Time",False),   
]

@pytest.mark.parametrize("inputA, inputB, expectedResult", testTimeData)

def test_timeValidation(inputA, inputB, expectedResult)
    assert checkInput(inputA, inputB) == expectedResult    