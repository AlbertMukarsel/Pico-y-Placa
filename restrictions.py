from datetime import datetime
import utilities

def restrictionDays(date, licensePlate):
    plateNumbersPerDay={
        0:[1,2],
        1:[3,4],
        2:[5,6],
        3:[7,8],
        4:[9,0],
        5:[],
        6:[]}

    day=datetime.strptime(date, '%d/%m/%Y').weekday()
    if day == 6 or day == 7:
        return False
    else: 
        dayRestrictions=plateNumbersPerDay[day]
        lastDigit=licensePlate[-1]
        if lastDigit in dayRestrictions:
            return True
        else:
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
    

