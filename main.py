start_ip = '104.166.148.0.'
end_ip = '104.166.151.255.'
count = 1024

def generate(ip):

    ip_arr = []

    num = ''

    for i in ip:

        if i == '.':
            ip_arr.append(int(num))
            num = ''
        else:
            num += i

    return ip_arr


start_ip_list = generate(start_ip)
end_ip_list = generate(end_ip)

def generate_range_ip(ip_list, end_ip, count):
    for i in range(count):

        if ip_list[0] == 255:
            break

        elif ip_list[1] == 255:
            ip_list[0] += 1
            print(f'{ip_list[0]}.{ip_list[1]}.{ip_list[2]}.{ip_list[3]} - count {i}')
            ip_list[1] = 0

        elif ip_list[2] == 255:
            ip_list[1] += 1
            print(f'{ip_list[0]}.{ip_list[1]}.{ip_list[2]}.{ip_list[3]} - count {i}')
            ip_list[2] = 0

        elif ip_list[3] == 255:
            ip_list[2] += 1
            print(f'{ip_list[0]}.{ip_list[1]}.{ip_list[2]}.{ip_list[3]} - count {i}')
            ip_list[3] = 0

        else:
            print(f'{ip_list[0]}.{ip_list[1]}.{ip_list[2]}.{ip_list[3]} - count {i}')
            ip_list[3] += 1


generate_range_ip(start_ip_list, end_ip_list, count)
