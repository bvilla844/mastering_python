# match - case statements : an alternative to using many elif statements
# execute some code if a values matches a case

def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return print (f"{day} is not a valid day")

def is_weekend(day):
    match day:
        case "Saturday" | "Sunday":
            return True
        case "Monday" | "Tuesday" | "Wednesday":
            return False
        case _:
            return print (f"{day} is not a valid day")

print(is_weekend("Saturday"))