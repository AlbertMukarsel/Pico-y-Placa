import pytest
from inputValidations import checkInput

testDateData=[
    ("11-11-1987","Date",False),
    ("11/11/1987","Date",True),
    ("11/11/2022","Date",True),
    ("05/01/2020","Date",True),
    ("05/12/2000","Date",True),
    ("11/11/1200","Date",False),
    ("11-11/1987","Date",False),
    ("11/11-1987","Time",False),
    ("1/11/1987","Date",False),
    ("30-15-1987","Date",False),
    ("30/02/2020","Date", False)
]

@pytest.mark.parametrize("inputA, inputB, expectedResult", testDateData)

def test_dateValidation(inputA, inputB, expectedResult):
    assert checkInput(inputA, inputB) == expectedResult
