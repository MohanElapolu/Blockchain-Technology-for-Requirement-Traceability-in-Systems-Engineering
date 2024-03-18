# Genesis block creation..

#Importing all the required modules
import json
import pickle
from collections import OrderedDict
import hashlib
import os

#Importing all the required homemade modules
from requirement_chain.file_operations import *
from requirement_chain.blockchain_operations import *
from requirement_chain.user_inputs import *
from requirement_chain.hash_utils import hash_block
#import print_func 


def genesis(wallet, peer_nodes):
    #genesis_hash_data = "Need an autonomous racing car"
    path1 = os.path.abspath(os.path.dirname(__file__))
    path2 = "/requirement_artifacts2/artifact_1.xlsx"
    path  =  path1 + path2
    name, depends_on, authors, requirement_data = read_file_pd(path)

    artifact_data = get_artifact_data(requirement_data, wallet)    
    artifact = add_requirement_artifact(name, depends_on, authors, artifact_data)
    genesis_block, succed, message  = mine_block([], artifact, peer_nodes, 0)

    return genesis_block