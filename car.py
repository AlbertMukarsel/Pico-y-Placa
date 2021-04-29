from restrictions import restrictionDays, restrictionHours

class Car:
    def __init__(self, licensePlate):
        self.licensePlate = licensePlate

    def hasRestriction(self, date, time):
        isDayRestricted = restrictionDays(date, self.licensePlate)
        isHourRestricted = restrictionHours(time)
        if isDayRestricted and isHourRestricted:
            print("You cannot use your car on the {} at {}".format(date, time))
        else:
            print("You can be on the road")

    