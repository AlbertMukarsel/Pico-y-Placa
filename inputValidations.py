import re #RegEx built-in library, imported to validate the license plate number

def checkInput(inputReceived, inputType):
    inputIsCorrect=False
    #region Regular Expressions 
    licensePlateRegEx=re.compile("^[A-Za-z]{2,3}-[0-9]{4}$")
    """
    Ecuadorian license plate numbers could come in the next formats:
        AAA-####
        AA-####
    """ 
    dateRegEx=re.compile("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$")
    """
    Date will be in the format DD/MM/YYYY & DD-MM-YYYY
    """
    timeRegEx=re.compile("^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$")
    """
    Time will be used in the format 00:00 - 23:59
    """
    #endregion
    #region Validations
    if (inputExpected == "License Plate"):
        if licensePlateRegEx.match(inputType):
            inputIsCorrect=True
        else:
            print("Invalid license plate number, please try again")
    elif(inputExpected == "Date"):
        if dateRegEx.match(inputType):
            inputIsCorrect=True
        else:
            print("Invalid date, please try again")
    elif(inputExpected== "Time"):
        if timeRegEx.match(inputType):
            inputIsCorrect=True
        else:
            print("Invalid time, please try again") 
    #endregion
    return inputIsCorrect