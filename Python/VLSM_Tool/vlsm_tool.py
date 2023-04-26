#netwerk_address = str(input("Given IP address (eg. 192.168.0.0/16): "))
#hosts = str(input("Required hosts seperated by forward slashes (eg. 100/50/20/10...): "))
netwerk_address = "192.168.0.0/16"
hosts = "20/50/20/10"


splitted = netwerk_address.split("/")
netwerk_address, CIDR = splitted[0], int(splitted[1])


def numberToBinary(num):
    binaryString = []
    currentnum = num
    while currentnum != 0:
        if currentnum % 2 == 0:
            currentnum = currentnum / 2
            binaryString.insert(0, "0")
        else:
            currentnum = (currentnum - 1) / 2
            binaryString.insert(0, "1")
    return "".join(binaryString)

def binaryToNumber(binaryString):
    pass


netwerk_address = netwerk_address.split(".")
binary_address = []
for n in netwerk_address:
    n_in_binary = numberToBinary(int(n))
    binary_address.append("0" * (8 - len(n_in_binary)) + n_in_binary)

binary_address = "".join(binary_address)
netwerk_part, host_part = binary_address[0:CIDR], binary_address[CIDR - 1:31]

hosts = hosts.split("/")
hosts_bit_amounts = []
for h in hosts:
    n = 1
    while (2 ** n) < int(h) + 2:
        n += 1
    hosts_bit_amounts.append(n)

print(hosts_bit_amounts)
hosts_bit_amounts = hosts_bit_amounts.sort()


subnet_addresses = []
for h in hosts_bit_amounts:
    current_address = binary_address
    current_cidr = CIDR

    

