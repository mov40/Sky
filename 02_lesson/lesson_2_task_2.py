def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


test_year = 2024
result = is_year_leap(test_year)
print(f"год {test_year}: {result}")
