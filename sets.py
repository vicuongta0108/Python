# Create an empty set
s = set()

# Add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3) # no duplicates in set
print(f'Set: {s}')
print(f'The set has {len(s)} elements\n')
# Remove element from set
s.remove(2)
print(f'New set: {s}')

# Get length of sequence
print(f'The new set has {len(s)} elements')