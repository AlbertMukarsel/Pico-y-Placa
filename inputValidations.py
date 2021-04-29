import re #RegEx built-in library, imported to validate the license plate number

def checkInput(inputReceived, inputType):
    inputIsCorrect=False
    #region Regular Expressions 
    licensePlateRegEx=re.compile("[A-Z]{2,3}-[0-9]{4}")
    """
    Ecuadorian license plate numbers could come in the next formats:
        AAA-####
        AA-####
    """ 
    dateRegEx=re.compile("^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)[0-9][0-9]$")
    """
    Date will be in the format DD/MM/YYYY
    does not exclude February 30 or 31
    """
    timeRegEx=re.compile("^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$")
    """
    Time will be used in the format 00:00 - 23:59
    """
    #endregion
    #region Validations
    if (inputType == "License Plate"):
        if licensePlateRegEx.match(inputReceived):
            inputIsCorrect=True
        else:
            print("Invalid license plate number, please try again")
    elif(inputType == "Date"):
        if dateRegEx.match(inputReceived):
            inputIsCorrect=True
        else:
            print("Invalid date, please try again")
    elif(inputType == "Time"):
        if timeRegEx.match(inputReceived):
            inputIsCorrect=True
        else:
            print("Invalid time, please try again") 
    #endregion
    return inputIsCorrect