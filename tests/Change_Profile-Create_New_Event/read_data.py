import csv

class Read:
    def read(self, filepath):
        with open(filepath, 'r') as datafile:
            datasheet = csv.reader(datafile)
            values = []
            for row in datasheet:
                values.append(row)
            values.pop(0)
        return values