import portscanner

targets_ip = input('[+] * Enter Target to scan For Vulnerable Open Ports: ')
port_number = int(input('[+] * Enter Amount of Ports you want to scan (500 - first 500 ports): '))
vul_file = input('[+] * Enter Path To The File With Vulnerable Softwares: ')
print('\n')

target = portscanner.Portscan(targets_ip, port_number)
target.scan()

with open(vul_file, 'r') as file:
    count = 0
    for banner in target.banners:
        file.seek(0)
        for line in file.readlines():
            if line.strip() in banner:
                print('[!!] VULNERABLE BANNER: "'+ banner +'" ON PORT : ' + str(target.open_ports[count]))
        count += 1