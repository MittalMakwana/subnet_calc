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

    def mask_int_to_bin(self):
        return [int(i, 2) for i in Netmask.mask_bin(self)]

    def wild_mask_int_to_bin(self):
        return [int(i, 2) for i in Netmask.wild_mask_bin(self)]


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

    def network(self):
        IP_bin = Ipaddress.ip_int_to_bin(self)
        MASK_bin = Netmask.mask_bin(self)
        ip_mask = zip(IP_bin, MASK_bin)
        return [int(i, 2) & int(m, 2) for i, m in ip_mask]

    def broadcast(self):
        # networkaddr = Network.network(self)
        networkbin = Ipaddress.ip_int_to_bin(self)
        wildcard = Netmask.wild_mask_bin(self)
        ip_mask = zip(networkbin, wildcard)
        return [int(i, 2) | int(m, 2) for i, m in ip_mask]

    def first_host(self):
        network = Network.network(self)[:-1]
        network.append(Network.network(self)[-1] + 1)
        return network

    def last_host(self):
        network = Network.broadcast(self)[:-1]
        network.append(Network.broadcast(self)[-1] - 1)
        return network


def ip_bin_to_int(IP):
    return [int(i, 2) for i in Ipaddress.ip_int_to_bin(IP)]


if __name__ == "__main__":
    t = Network([10, 0, 0, 1], 17)
    print t.ip
    print t.mask_bin()
    print t.wild_mask_bin()
    print t.network()
    print t.broadcast()
    print t.ip_int_to_bin()
    print t.total_host()
    print t.mask_int_to_bin()
    print t.wild_mask_int_to_bin()
    print t.first_host()
    print t.last_host()
