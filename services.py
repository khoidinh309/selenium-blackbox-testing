import csv
from date import DateObject

class TestService:
  def read_csv_data(file_path, column_list):
    with open(file_path, 'r') as file:
      reader = csv.DictReader(file)
      result = []
      
      for row in reader:
        row_object = {}
        for column in column_list:
          row_object[column] = row[column]
        result.append(row_object)
        
      return result
        
  def write_test_results(file_path, test_results):
    with open(file_path, 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(['Id', 'Test_Result'])
      for result in test_results:
        writer.writerow([result['Id'], result['Passed']])
  
  def create_date_object(date):
    [day, month, year] = date.split('/')
    return DateObject(month=str(month), day=str(day), year=str(year))