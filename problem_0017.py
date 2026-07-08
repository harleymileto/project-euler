one, hundred, aand, thousand = 3, 7, 3, 8

units = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
teens = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
tens = 6 + 6 + 5 + 5 + 5 + 7 + 6 + 6

# 1-99:
to_ninety_nine = units + teens + 10*tens + 8*units

# 1-999:
to_nine_nine_nine = to_ninety_nine + (units + hundred*9) + (units)*99 + (hundred + aand)*891 + to_ninety_nine*9

print(to_nine_nine_nine + one + thousand)