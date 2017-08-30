class Netmask(object):
    '''
    A netmask is a 32-bit mask used to divide an IP address into subnets and
    specify the network's available hosts
    '''
    def __init__(self, mask):
        self.mask = mask

    def mask_bin(self):
        MASK_bin = ''
        for i in range(32):
            if i < self.mask:
                MASK_bin = MASK_bin + "1"
            else:
                MASK_bin = MASK_bin + "0"
        bin_mask = [MASK_bin[i:i+8] for i in range(0, len(MASK_bin), 8)]
        return bin_mask

    def wild_mask_bin(self):
        MASK_bin = ''
        for i in range(32):
            if i < self.mask:
                MASK_bin = MASK_bin + "0"
            else:
                MASK_bin = MASK_bin + "1"
        bin_mask = [MASK_bin[i:i+8] for i in range(0, len(MASK_bin), 8)]
        return bin_mask

    def total_host(self):
        return (2**(32-self.mask)) - 2


class Ipaddress(object):
    '''
    Defining an IP address
    '''
    def __init__(self, ip):
        self.ip = ip

    def ip_int_to_bin(self):
        ip_bin = ["{0:08b}".format(int(i)) for i in self.ip]
        return ip_bin


class Network(Ipaddress, Netmask):
    '''
    Define a network
    '''
    def __init__(self, ip, mask):
        Netmask.__init__(self, mask)
        Ipaddress.__init__(self, ip)
    


def broadcast(ip, mask):
    networkaddr = network(ip, mask)
    networkbin = ip_bin(networkaddr)
    wildcard = wild_mask_bin(mask)
    ip_mask = zip(networkbin, wildcard)
    return [int(i, 2) + int(m, 2) for i, m in ip_mask]


def ip_bin_to_int(self):
    return [int(i, 2) for i in self.ip]


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


# ip = Ipaddress([10, 0, 0, 130])
# MASK = 24

t = Network([10, 0, 0, 130], 23)
# v = Netmask(23)
# print ip.ip_int_to_bin()
# print v.wild_mask_bin()
# print v.mask_bin()
# print v.total_host()
print t.wild_mask_bin()
print t.total_host()
# print_result(IP, MASK)
