import readCSV
import rangeIPGen

csv_reader = readCSV.CSV_Reader('')
csv_data = csv_reader.read()



for [data_1, data_2, data_3] in csv_data:
    ip_gen = rangeIPGen.IP_Generator()
    ip_gen.str_to_arr(data_1 + '.')
    ip_gen.generate_range_ip(int(data_3.replace(',', '')))