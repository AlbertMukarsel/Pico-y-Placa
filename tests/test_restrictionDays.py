import pytest
from restrictions import restrictionDays

testDayData=[
    ("26/04/2021","HBA-5821",True),
    ("26/04/2021","HBA-5822",True),
    ("27/04/2021","HBA-5823",True),
    ("27/04/2021","HBA-5824",True),
    ("28/04/2021","HBA-5825",True),
    ("28/04/2021","HBA-5826",True),
    ("29/04/2021","HBA-5828",True),
    ("29/04/2021","HBA-5827",True),
    ("30/04/2021","HBA-5829",True),
    ("30/04/2021","HBA-5820",True),
    ("26/04/2021","HBA-5823",False),
    ("26/04/2021","HBA-5824",False),
    ("27/04/2021","HBA-5822",False),
    ("27/04/2021","HBA-5821",False),
    ("28/04/2021","HBA-5820",False),
    ("28/04/2021","HBA-5829",False),
    ("29/04/2021","HBA-5825",False),
    ("29/04/2021","HBA-5826",False),
    ("30/04/2021","HBA-5827",False),
    ("30/04/2021","HBA-5828",False),
]

@pytest.mark.parametrize("inputA, inputB, expectedResult", testDayData)

def test_dayValidation(inputA, inputB, expectedResult):
    assert restrictionDays(inputA, inputB) == expectedResult