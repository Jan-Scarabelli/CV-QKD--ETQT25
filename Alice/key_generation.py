import numpy as np
import utils.basis_generation as bg

def generate_alice_key(length: int) -> list:
    """
    Generates a random key for Alice using the basis generation utilities.
    
    Args:
        length (int): The length of the key to generate.
        
    Returns:
        list: A list containing the generated key bits.
    """
    return bg.split_key_into_blocks(bg.generate_basis_sequence(2*length),2)

def sift_alice_key(key: list, bob_basis: list) -> list:
    """
    Sifts Alice's key based on Bob's basis measurement.
    
    Args:
        key (list): Alice's key to be sifted.
        bob_basis (list): Bob's basis used for sifting.
        
    Returns:
        list: The sifted key.
    """
    sifted_key = []

    for i in range(len(bob_basis)):
        # If Bob's basis is 0 (measured amplitude), take the first element, otherwise take the seccond bit of each block.
        if bob_basis[i] == 0:
            sifted_key.append(key[i][0])
        else:
            sifted_key.append(key[i][1])
    
    return sifted_key
