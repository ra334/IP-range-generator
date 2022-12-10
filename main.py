import readCSV

csv_reader = readCSV.CSV_Reader('Russian Federation_IPv4.csv')
csv_data = csv_reader.read()



for [data_1, data_2, data_3] in csv_data:
    print(f'data_1: {data_1}, data_2: {data_2}, data_3: {data_3}')