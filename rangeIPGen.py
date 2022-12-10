class IP_Generator:
    def __init__(self):
        self.start_ip_list = []

    def str_to_arr(self, ip):

        ip_arr = []

        num = ''

        for i in ip:

            if i == '.':
                ip_arr.append(int(num))
                num = ''
            else:
                num += i

        self.start_ip_list = ip_arr

    def generate_range_ip(self, count, filename='ip.txt'):
        for i in range(count):
            with open(filename, 'a') as f:
                if self.start_ip_list[0] == 255:
                    break

                elif self.start_ip_list[1] == 255:
                    self.start_ip_list[0] += 1
                    f.write(f'{self.start_ip_list[0]}.{self.start_ip_list[1]}.{self.start_ip_list[2]}.{self.start_ip_list[3]}\n')
                    # print(f'{self.start_ip_list[0]}.{self.start_ip_list[1]}.{self.start_ip_list[2]}.{self.start_ip_list[3]} - count {i}')
                    self.start_ip_list[1] = 0

                elif self.start_ip_list[2] == 255:
                    self.start_ip_list[1] += 1
                    f.write(f'{self.start_ip_list[0]}.{self.start_ip_list[1]}.{self.start_ip_list[2]}.{self.start_ip_list[3]}\n')
                    # print(f'{self.start_ip_list[0]}.{self.start_ip_list[1]}.{self.start_ip_list[2]}.{self.start_ip_list[3]} - count {i}')
                    self.start_ip_list[2] = 0

                elif self.start_ip_list[3] == 255:
                    self.start_ip_list[2] += 1
                    f.write(f'{self.start_ip_list[0]}.{self.start_ip_list[1]}.{self.start_ip_list[2]}.{self.start_ip_list[3]}\n')
                    # print(f'{self.start_ip_list[0]}.{self.start_ip_list[1]}.{self.start_ip_list[2]}.{self.start_ip_list[3]} - count {i}')
                    self.start_ip_list[3] = 0

                else:
                    f.write(f'{self.start_ip_list[0]}.{self.start_ip_list[1]}.{self.start_ip_list[2]}.{self.start_ip_list[3]}\n')
                    # print(f'{self.start_ip_list[0]}.{self.start_ip_list[1]}.{self.start_ip_list[2]}.{self.start_ip_list[3]} - count {i}')
                    self.start_ip_list[3] += 1


if __name__ == '__main__':
    ip_gen = IP_Generator()
    ip_gen.str_to_arr('192.168.0.0.')
    ip_gen.generate_range_ip(10)