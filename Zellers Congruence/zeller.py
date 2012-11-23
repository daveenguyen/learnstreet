#Zeller Method project

# We'll be using Zeller's congruence, which is an algorithm devised by Christian Zeller to 
# calculate the day of the week for any Julian or Gregorian calendar date:

# h = ( ( q +( (m+1) * 26 // 10)+ Y +( Y // 4)+ 6 * (Y // 100)+ (Y // 400)) % 7 )

#... all of which translates to this:

#dayOfWeek = (dayOfMonth + ((month + 1) * 26 // 10) + year + (year // 4) +
#   6 * (year/ / 100) + (year // 400)) % 7)

# Note that in this algorithm, January and February are counted as
# months #13 & #14 of the previous year, which will need to factor into your method.

def zeller(q, m, Y):
    # q = day of month (int)
    # m = month of the year (string)
    # Y = year (int)
    days = ("Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
    months = {
        "january":  13,
        "february": 14,
        "march":     3,
        "april":     4,
        "may":       5,
        "june":      6,
        "july":      7,
        "august":    8,
        "september": 9,
        "october":  10,
        "november": 11,
        "december": 12
    }
    m = m.lower()
    if months[m] > 12:
        Y -= 1
    day = ( ( q +( (months[m]+1) * 26 // 10)+ Y +( Y // 4)+ 6 * (Y // 100)+ (Y // 400)) % 7 )
    # This method should return the day of the week as a string
    return days[day]