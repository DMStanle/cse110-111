#My exceeding of requirements can be found in lines 48-50.
#I have added code that tells the customer when they can return their items.


import csv
from datetime import datetime, timedelta

def main():
   SERIAL_INDEX = 0

   dictionary = read_dictionary('products.csv', SERIAL_INDEX)
   list = read_request('request.csv')
   aligned = align_portion(dictionary, list)
   print(dictionary)
   print()
   print('Inkom Emporium')
   try:

      for item in aligned:
       print(f'{item[3]}: {item[1]} @ {item[4]}')
   except:
      print('The aligned is empty')

   quantity = sum(int(item[1]) for item in aligned)
   print()
   print(f'You have ordered {quantity} items.')

   sub_total = 0
   tax = 0
   total = 0
   for item in aligned:
      if len(item) > 4:
         sub_total += float(item[1]) * float(item[4])
         tax = sub_total * 0.06
         total = sub_total + tax
   print(f'The subtotal is: ${sub_total:.2f}')
   print(f'The tax is: ${tax:.2f}')
   print(f'The total is: ${total:.2f} ')
   print('Thank you for shopping at the Inkom Emporium.')

   now = datetime.now()
   date_and_time = now.strftime("%A, %B %d, %H:%M:%S %Y")
   print(date_and_time)




   return_date = now + timedelta(days=30)
   return_date2 = return_date.strftime("%m-%d-%Y")
   print(f'Returns acceped until 9:00PM on {return_date2}.')



      

def read_dictionary(products, SERIAL_INDEX):
  
  dictionary = {}
  try:
     
   with open(products, 'rt') as csv_file:
      reader = csv.reader(csv_file)
      next(reader)

      for i in reader:
         if len(i) != 0:
            key = i[SERIAL_INDEX]
            dictionary[key] = i

  except:
      print(f"Error: missing file\n[Errno 2] No such file or directory: '{products}' ")
   

  return dictionary
  
def read_request(request):
    with open(request, 'rt') as csv_file:
       reader = csv.reader(csv_file)
       next(reader)
       return list(reader)

def align_portion(dictionary, list):
   try:
      for item in list:
         values = dictionary[item[0]]
         for value in values:
            item.append(value)
   except:
      print(f"Error: unknown product ID in the request.csv file\n '{item[0]}'")
      

   return list
   



if __name__ == "__main__":
    main()


