import random


class Netmask(object):
    '''
    A netmask is a 32-bit mask used to divide an IP address into subnets and
    specify the network's available hosts
    '''
    def __init__(self, mask):
        self.mask = mask
        if mask < 0 or mask > 32:
            raise ValueError

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
        if len(ip) != 4 or len([i for i in ip if i > 256]) != 0:
            raise ValueError

    def ip_int_to_bin(self):
        ip_bin = ["{0:08b}".format(int(i)) for i in self.ip]
        return ip_bin

    def ip_private(self):
        if ((self.ip[0] == 10) or
           (self.ip[0] == 127) or
           (self.ip[0] == 172 and (16 <= self.ip[1] <= 31)) or
           (self.ip[0] == 192 and self.ip[1] == 168)):
            return True
        else:
            return False

    def ip_class(self):
        if 0 <= self.ip[0] <= 127:
            return "A"
        elif 127 <= self.ip[0] <= 191:
            return "B"
        elif 192 <= self.ip[0] <= 223:
            return "C"
        elif 224 <= self.ip[0] <= 239:
            return "D"
        else:
            return "E"

    def ip_loopback(self):
        if self.ip[0] == 127:
            return True
        else:
            return False


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

    def is_network_addr(self):
        if Network.network(self) == self.ip:
            return True
        else:
            return False

    def is_broadcast_addr(self):
        if Network.broadcast(self) == self.ip:
            return True
        else:
            return False

    def get_all_host(self):
        host_list = []
        for i in range(Netmask.total_host(self)):
            temp = bin(int("".join(Ipaddress.ip_int_to_bin(self)),
                       2) + i)[2:].zfill(32)
            temp2 = [temp[j:j+8] for j in range(0, len(temp), 8)]
            temp3 = [int(k, 2) for k in temp2]
            host_list.append(".".join(str(x) for x in temp3))
        return host_list

    def gen_random_host(self, *count):
        host = []
        if len(count) == 0:
            count += (1,)
        if count[0] > Network.total_host(self) or count[0] is int:
            raise ValueError
        for i in range(count[0]):
            random_host = random.randint(0, Netmask.total_host(self))
            temp = bin(int("".join(Ipaddress.ip_int_to_bin(self)), 2) +
                       random_host)[2:].zfill(32)
            temp2 = [temp[j:j+8] for j in range(0, len(temp), 8)]
            temp3 = [int(k, 2) for k in temp2]
            host.append(".".join(str(x) for x in temp3))
        return host


if __name__ == "__main__":
    t = Network([10, 0, 0, 1], 24)
    print t.get_all_host()
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
    print t.is_network_addr()
    print t.is_broadcast_addr()
    print t.gen_random_host(45)
