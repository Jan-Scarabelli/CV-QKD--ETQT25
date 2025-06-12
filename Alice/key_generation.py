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

def shift_alice_key(key: list, bob_basis: list) -> list:
    """
    Shifts Alice's key based on Bob's basis measurement.
    
    Args:
        key (list): Alice's key to be shifted.
        bob_basis (list): Bob's basis used for shifting.
        
    Returns:
        list: The shifted key.
    """
    shifted_key = []
    key_splitted = bg.split_key_into_blocks(key, 2)

    for i in range(len(bob_basis)):
        # If Bob's basis is 0 (measured amplitude), take the first element, otherwise take the seccond bit of each block.
        if bob_basis[i] == 0:
            shifted_key.append(key_splitted[i][0])
        else:
            shifted_key.append(key_splitted[i][1])
    
    return shifted_key
