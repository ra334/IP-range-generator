start_ip = '103.136.43.0.'
end_ip = '103.136.43.255.'
count = 256

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

def generate_range_ip(ip_list, count):
    for i in range(count):
        print(f'{ip_list[0]}.{ip_list[1]}.{ip_list[2]}.{ip_list[3]}')

        if ip_list[0] == 255:
            break

        if ip_list[1] == 255:
            ip_list[0] += 1

        if ip_list[2] == 255:
            ip_list[1] += 1

        if ip_list[3] == 255:
            ip_list[2] += 1

        ip_list[3] += 1

generate_range_ip(start_ip_list, count)
