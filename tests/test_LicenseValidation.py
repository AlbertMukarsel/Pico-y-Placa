import pytest
from inputValidations import checkInput

testLicenseData =[
    ("HBA-5828","License Plate", True),
    ("hba-5828","License Plate", True),
    ("xz-2020","License Plate", True),
    ("XZ-2020","License Plate", True),
    ("Xz-2020","License Plate", False),
    ("HBA-582","License Plate", False),
    ("A-142","License Plate", False),
    ("HBA-5828","Date", False),
]

@pytest.mark.parametrize("inputA, inputB, expectedResult", testLicenseData)

def test_licenseValidation(inputA, inputB, expectedResult)
    assert checkInput(inputA, inputB) == expectedResult

