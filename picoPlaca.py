from inputValidations import checkInput

validatedLicense = False
validatedDate = False
validatedTime = False

while(not validatedLicense):
    licensePlate = input("Enter you license number plate: ")
    validated=checkInput(licensePlate, "License Plate")

while(not validatedDate):
    date = input("Enter the date you want to check (format DD-MM-YYYY): ")
    validatedDate=checkInput(date, "Date")

while(not validatedTime):
    time = input("Enter the time you want to check (format HH:mm): ")
    validatedTime=checkInput(date,"Time")




