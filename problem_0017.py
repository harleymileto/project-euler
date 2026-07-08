# one (3) two (3) three (5) four (4) five (4) six (3) seven (5) eight (5) nine (4)
# ten (3) eleven (6) twelve (6) thirteen (8) fourteen (8) fifteen (7) sixteen (7) seventeen (9) eighteen (8) nineteen (8)
# ty (2) twen (4) thir (4) four (4) fif (3) six (3) seven (5) eigh (4) nine (4)
# hundred (7) and (3)
one, two, three, four, five, six, seven, eight, nine = 3, 3, 5, 4, 4, 3, 5, 5, 4
ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen = 3, 6, 6, 8, 8, 7, 7, 9, 8, 8
twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety = 6, 6, 5, 5, 5, 7, 6, 6
hundred, aand, thousand = 7, 3, 8

units = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4
teens = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8
tens = 6 + 6 + 5 + 5 + 5 + 7 + 6 + 6

# 1-99:
to_ninety_nine = units + teens + 10*tens + 8*units

# 1-999:
to_nine_nine_nine = to_ninety_nine + (units + hundred*9) + (units)*99 + (hundred + aand)*891 + to_ninety_nine*9

print(to_ninety_nine)
print(to_nine_nine_nine + one + thousand)