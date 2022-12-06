raw = open('input.txt').read().strip()

part = 2
packet_size = 4 if part == 1 else 14

i = 0
while True:
    packet = raw[i:i+packet_size]
    if sorted(list(set(packet))) == sorted(list(packet)):
        print(i+packet_size)
        break
    i+=1