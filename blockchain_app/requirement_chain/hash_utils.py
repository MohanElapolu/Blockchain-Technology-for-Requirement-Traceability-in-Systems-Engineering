#Hash

import hashlib

#Hash the block
def __init__():
    pass

def hash_block(hash_data):
    """ 
    Explanation:
    Arguments:
    Return values: 
    """
    return hashlib.sha256(hash_data.encode()).hexdigest()
def hash_requirement(hash_data):
    """ 
    Explanation:
    Arguments:
    Return values: 
    """
    return str(hash(hash_data))