from basis_generation import generate_basis_sequence, split_key_into_blocks

seq = generate_basis_sequence(100)

seq_split = split_key_into_blocks(seq, 2)

print(seq_split)


