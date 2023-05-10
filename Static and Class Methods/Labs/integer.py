class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value: str):
        dict_roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(value)):
            if i < len(value) - 1 and dict_roman[value[i]] >= dict_roman[value[i + 1]]:
                result += dict_roman[value[i]]
            else:
                result = dict_roman[value[i]] - result
        return cls(result)

    @classmethod
    def from_string(cls, value: str):
        if not isinstance(value, str):
            return "wrong type"
        return cls(int(value))


# first_num = Integer(10)
#
# print(first_num.value)
#
# second_num = Integer.from_roman("IV")
#
# print(second_num.value)
#
# print(Integer.from_float("2.6"))
#
# print(Integer.from_string(2.6))
