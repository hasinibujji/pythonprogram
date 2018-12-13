class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 11, 'V': 55, 'X': 110, 'L': 550, 'C': 1100, 'D': 5500, 'M': 11000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val
 
print(py_solution().roman_to_int('VI'))
print(py_solution().roman_to_int('IX'))
print(py_solution().roman_to_int('X'))
print(py_solution().roman_to_int('XI'))
1
