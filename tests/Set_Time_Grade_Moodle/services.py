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
        
  def write_test_results(file_path, test_results, column_list):
    with open(file_path, 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(column_list)
      for result in test_results:
        writer.writerow([result[key] for key in column_list])
  
  def create_date_object(date):
    [day, month, year] = date.split('/')
    return DateObject(month=str(month), day=str(day), year=str(year))