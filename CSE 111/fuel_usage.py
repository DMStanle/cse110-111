def main():
  
  

  # Get an odometer value in U.S. miles from the user.
  # Get another odometer value in U.S. miles from the user.
  # Get a fuel amount in U.S. gallons from the user.
  # Call the miles_per_gallon function and store
  # the result in a variable named mpg.
  # Call the lp100k_from_mpg function to convert the
  # miles per gallon to liters per 100 kilometers and
  # store the result in a variable named lp100k.
  # Display the results for the user to see.


  pass

def miles_per_gallon(start_miles, end_miles, amount_gallons):
 
 mpg2 = end_miles - start_miles
 mpg = mpg2 / amount_gallons


 return mpg



start_miles = float(input('What is the starting odometer in miles: '))
end_miles = float(input('What is the end odometer in miles: '))
amount_gallons = float(input('What is the amount of gas in gallons: '))
mpg = miles_per_gallon(start_miles, end_miles, amount_gallons)

def lp100k_from_mpg(mpg):
  lp100k = 235.215 / mpg
  
  
  """Convert miles per gallon to liters per 100
  kilometers and return the converted value.
  Parameter mpg: A value in miles per gallon
  Return: The converted value in liters per 100km.
  """
  return lp100k

lp100k = lp100k_from_mpg(mpg)
print(f'Your gas mileage is {mpg:.2f} per gallon. ')
print(f'In liters per 100k it is {lp100k:.2f} liters per 100k. ')
# Call the main function so that
# this program will start executing.




main()