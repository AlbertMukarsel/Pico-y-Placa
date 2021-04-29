from datetime import datetime
import utilities

def restrictionDays(date, licensePlate):
    """
    Each day is represented by a number, Monday=0...Sunday-6
    during weekdays, according to each day, if a license plate has
    one of those digits as its last one, is subject to the Pico y Placa restrictions
    I.E: on Mondays, a car with its license plate ending on 1 or 2
    is subject to restrictions
    """
    plateNumbersPerDay={
        0:[1,2],
        1:[3,4],
        2:[5,6],
        3:[7,8],
        4:[9,0],
        5:[],
        6:[]}

    day=datetime.strptime(date, '%d/%m/%Y').weekday()
    if day == 5 or day == 6:
        return False
    else: 
        dayRestrictions=plateNumbersPerDay[day] #Gets the plate's last digits that cannot be on the road acording to day 
        lastDigit=int(licensePlate[-1]) #Get the input plate's last digit to check if is allowed or not to be on the road
        if (lastDigit in dayRestrictions):
            return True
    return False

def restrictionHours(time):
    restrictedHours={
    "AM":["7:00","9:30"],
    "PM":["16:00","19:30"]}
    
    hour=datetime.strptime(time, "%H:%M").time()
    AMRestrictionStartTime, AMRestrictionEndTime = utilities.getRestrictionHours(restrictedHours["AM"])
    PMRestrictionStartTime, PMRestrictionEndTime = utilities.getRestrictionHours(restrictedHours["PM"])
    if AMRestrictionStartTime <= hour <= AMRestrictionEndTime:
        return True
    if PMRestrictionStartTime <= hour <= PMRestrictionEndTime:
        return True
    #if the specified time is not part of the restrictions schedule, it returns False
    return False

