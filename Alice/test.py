from key_generation import generate_alice_key, sift_alice_key
from utils.basis_generation import generate_basis_sequence, split_key_into_blocks


bob_basis = generate_basis_sequence(100)
alice_key = generate_alice_key(100)

sifted_key = sift_alice_key(alice_key, bob_basis)

print("Alice's final key:", sifted_key)