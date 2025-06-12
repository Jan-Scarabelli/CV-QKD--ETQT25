import secrets
import numpy as np

def generate_basis_sequence(length: int) -> list:
    """
    Generates a random sequence of bits (0s and 1s) to represent the basis for measurements.
    
    Args:
        length (int): The length of the basis sequence to generate.
        
    Returns:
        list: A list containing the generated basis bits.
    """
    return [secrets.randbelow(2) for _ in range(length)]

def split_key_into_blocks(key: list, block_size: int) -> list:
    """
    Splits a key into blocks of a specified size.
    
    Args:
        key (list): The key to be split.
        block_size (int): The size of each block.
        
    Returns:
        list: A list of blocks, each containing the specified number of bits.
    """
    return [key[i:i + block_size] for i in range(0, len(key), block_size)]