input_date="10/05/2022"
year=int(input_date[-4:])
if (year%4 == 0 and year % 100!=0) or (year%400 == 0):
    output_year =year+1
else:
    output_year=year-1
output_date = input_date[:-4]+str(output_year)
print("output_date:",output_date)


