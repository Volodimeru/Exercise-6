def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dollars1 = d.replace("$","")
    return float(dollars1)


def percent_to_float(p):
    percent1 = p.replace("%","")
    percent2 = float(percent1) /100
    return (percent2)

main()