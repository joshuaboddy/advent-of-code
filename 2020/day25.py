def transform(pub_key, subject, remainder):
    
    value = 1
    loop_size = 0
    while value != pub_key:
        value = value * subject % remainder
        loop_size += 1

    return loop_size

def rev_transform(pub_key, subject, loop_size, remainder):
    
    value = 1
    counter = 0
    while counter < loop_size:
        value = value * subject % remainder
        counter += 1
        
    encryption_key = value
    
    return encryption_key

door_pub = 18499292

card_pub = 8790390

loop = transform(door_pub,7,20201227)

print(rev_transform( 7, card_pub, loop, 20201227))

