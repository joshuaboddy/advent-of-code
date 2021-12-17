import numpy as np

def hex_to_bin(h, b_digits):
    return bin(int(h, 16))[2:].zfill(b_digits)

def bin_to_int(b):
    return int(str(b), 2)

def process_initial_hex(h):
    
    bin_str = str(hex_to_bin(h, 4))
    
    while len(bin_str) % 4 != 0:
        bin_str = '0' + bin_str
    
    return bin_str

def process_literal(b, pos):
    
    literal_str = b[pos+6:]
    
    all_groups = [literal_str[i:i+5] for i in range(0, len(literal_str), 5)]
    index_of_last_group = [g[0] == '0' for g in all_groups].index(True)
    groups = all_groups[0:index_of_last_group+1]
    
    literal_value = bin_to_int(''.join([g[1:] for g in groups]))
 
    pos = pos + 5*index_of_last_group + 11

    
    return literal_value, pos

version_sum = 0

def get_subpackets(bin_str, idx):

    global version_sum

    packet_version = bin_to_int(bin_str[0+idx:3+idx])
    packet_type_id = bin_to_int(bin_str[3+idx:6+idx])
    
    version_sum += packet_version
    scores_in_packet = []

    length_type_id = int(bin_str[idx+6])
    
    if packet_type_id == 4:
        literal_value, pos = process_literal(bin_str, idx)
        scores_in_packet.append(literal_value)
        return literal_value, pos
    
    jumper = 7
    if length_type_id == 0:
        subpackets_length_bits = 15
        subpackets_length = bin_to_int(bin_str[idx+jumper:idx+jumper+subpackets_length_bits])
        
        pos = idx + jumper + subpackets_length_bits

        while pos < subpackets_length + idx + jumper + subpackets_length_bits:
            score, pos = get_subpackets(bin_str, pos)
            scores_in_packet.append(score)
        
        
    elif length_type_id == 1:
        number_of_subpackets_bits = 11
        number_of_subpackets = bin_to_int(bin_str[idx+jumper:idx+jumper+number_of_subpackets_bits])
        
        pos = idx + jumper + number_of_subpackets_bits
        
        for _ in range(number_of_subpackets):
            score, pos = get_subpackets(bin_str, pos)
            scores_in_packet.append(score)
      

    if packet_type_id == 0:
        score = sum(scores_in_packet)
    elif packet_type_id == 1:
        score = np.prod(scores_in_packet)
    elif packet_type_id == 2:
        score = min(scores_in_packet)
    elif packet_type_id == 3:
        score = max(scores_in_packet)
    elif packet_type_id == 4:
        score = scores_in_packet[0]
    elif packet_type_id == 5:
        score = int(scores_in_packet[0] > scores_in_packet[1])
    elif packet_type_id == 6:
        score = int(scores_in_packet[1] > scores_in_packet[0])
    elif packet_type_id == 7:
        score = int(scores_in_packet[0] == scores_in_packet[1])
        
    return score, pos


f = open('input.txt')
raw = f.read()
f.close()

hexa = raw.strip()

print('p2:' + str(get_subpackets(process_initial_hex(hexa), 0)[0]))
print('p1:' + str(version_sum))
