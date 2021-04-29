import datetime

def getRestrictionHours(Hours):
    restrictionStartTime=datetime.strptime(Hours[0],"%H:%M").time()
    restrictionEndTime=datetime.strptime(Hours[1],"%H:%M").time()
    return restrictionStartTime, restrictionEndTime