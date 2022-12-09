import csv


class CSV_Reader:
    def __init__(self, filename):
        self.filename = filename

    def reading(self):
        return_arr = []
        with open(self.filename) as f:
            reader = csv.reader(f)

            row = iter(reader)
            next(row, None)

            for row in reader:
                print(f'Start: {row[0]}, End: {row[1]}, Count: {row[2]}')
                return_arr.append(row)

        return return_arr

cve_test = CSV_Reader()

print(cve_test.reading())