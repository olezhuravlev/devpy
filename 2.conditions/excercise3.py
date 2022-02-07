#!/usr/bin/python3
import Utils

# Name          Boundaries
# Aries         21.03 - 20.04
# Taurus        21.04 - 21.05
# Gemini        22.05 - 21.06
# Cancer        22.06 - 22.07
# Leo           23.07 - 23.08
# Virgo         24.08 - 22.09
# Libra         23.09 - 23.10
# Scorpius      24.10 - 22.11
# Sagittarius   23.11 - 21.12
# Capricorn     22.12 - 20.01
# Aquarius      21.01 - 18.02
# Pisces        19.02 - 20.03


signs = (
    (21, "Aquarius"),  # January
    (19, "Pisces"),  # February
    (21, "Aries"),  # March
    (21, "Taurus"),  # April
    (22, "Gemini"),  # May
    (22, "Cancer"),  # June
    (23, "Leo"),  # July
    (24, "Virgo"),  # August
    (23, "Libra"),  # September
    (24, "Scorp1ius"),  # October
    (23, "Sagittarius"),  # November
    (22, "Capricorn")  # December
)


def get_zodiac_sign(month, day):
    idx = month - 1
    sign = signs[idx]
    sign_day = sign[0]
    if (day >= sign_day):
        return sign[1]
    else:
        return signs[idx - 1][1]


if __name__ == '__main__':
    month = Utils.get_parameter("Enter month: ", result_type=int)
    day = Utils.get_parameter("Enter day: ", result_type=int)
    print(get_zodiac_sign(month, day))
