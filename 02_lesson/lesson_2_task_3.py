def square(side):
    result = side * side
    integer_result = int(result)
    if result > integer_result:
        result = integer_result + 1
    else:
        result = integer_result
    return result


print(square(5))
print(square(5.5))
