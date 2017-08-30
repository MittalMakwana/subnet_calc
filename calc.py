def mask_bin(MASK):
    MASK_bin = ''
    for i in range(32):
        if i < MASK:
            MASK_bin = MASK_bin + "1"
        else:
            MASK_bin = MASK_bin + "0"
    mask = [MASK_bin[i:i+8] for i in range(0, len(MASK_bin), 8)]
    return mask


def wild_mask_bin(MASK):
    MASK_bin = ''
    for i in range(32):
        if i < MASK:
            MASK_bin = MASK_bin + "0"
        else:
            MASK_bin = MASK_bin + "1"
    mask = [MASK_bin[i:i+8] for i in range(0, len(MASK_bin), 8)]
    return mask


def ip_bin(IP):
    ip = ["{0:08b}".format(int(i)) for i in IP]
    return ip


def network(ip, mask):
    IP_bin = ip_bin(ip)
    MASK_bin = mask_bin(mask)
    ip_mask = zip(IP_bin, MASK_bin)
    return [int(i, 2) & int(m, 2) for i, m in ip_mask]


def broadcast(ip, mask):
    networkaddr = network(ip, mask)
    networkbin = ip_bin(networkaddr)
    wildcard = wild_mask_bin(mask)
    ip_mask = zip(networkbin, wildcard)
    return [int(i, 2) + int(m, 2) for i, m in ip_mask]


def ip(IP):
    return [int(i, 2) for i in IP]


def total_host(MASK):
    return (2**(32-MASK)) - 2


def print_result(ip_list, mask):
    net_mask = ip(mask_bin(mask))
    wild_card = ip(wild_mask_bin(mask))
    net = network(ip_list, mask)
    broad = broadcast(ip_list, MASK)
    f_host = net_mask[:-1]
    f_host.append(net_mask[-1]+1)
    l_host = broad[:-1]
    l_host.append(broad[-1]-1)
    host = total_host(mask)
    print "Address: " + str(ip_list)
    print "Net Mask: " + str(net_mask)
    print "Wildcard: " + str(wild_card)
    print "Network Address: " + str(net)
    print "Broadcast Address: " + str(broad)
    print "1st host: " + str(f_host)
    print "Last host: " + str(l_host)
    print "Hosts : " + str(host)


IP = [10, 0, 0, 130]
MASK = 24
print_result(IP, MASK)
