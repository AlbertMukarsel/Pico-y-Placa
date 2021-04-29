import pytest
from restrictions import restrictionHours

testHourData=[
    ("9:29",True),
    ("7:00",True),
    ("9:30",True),
    ("7:01",True),
    ("6:59",False),
    ("9:31",False),
    ("13:00",False),
    ("16:00",True),
    ("19:30",True),
    ("16:01",True),
    ("19:29",True),
    ("19:31",False),
    ("15:59",False),
    ("14:00",False)
]

@pytest.mark.parametrize("inputA, expectedResult", testHourData)

def test_dateValidation(inputA, expectedResult):
    assert restrictionHours(inputA) == expectedResult