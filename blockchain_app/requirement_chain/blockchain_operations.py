##Blockchain utilities file...

#Importing all the required modules
import json
import pickle
import requests
from collections import OrderedDict
import hashlib
import numpy as np
from datetime import datetime
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
import Crypto.Random
import binascii

#Importing all the required homemade modules
from requirement_chain.wallet import Wallet
from requirement_chain.file_operations import *
from requirement_chain.hash_utils import *
from threading import Lock

#from file_operations import read_data, save_data, load_data
#import print_func

#Getting last block of the RequirementChain
def get_requirement_chain():
    """ 
    Explanation: Gives the most recent requirement_chain
    Arguments: 
    Return values: 
    """
    #print(10)
    #print(local_host)
    return load_data()


#It collects the data obtained from the excel sheet
#It converts the data into a suitable format of block
def get_artifact_data(requirement_data, wallet):
    """ 
    Explanation:
    Arguments:
    Return values: 
    """
    artifact_data = OrderedDict()
    for i in range(len(requirement_data[:,0])):
        requirement_address       = hash_block(requirement_data[i,0])
        prev_requirement_address  = hash_block(requirement_data[i,1])
        trans_id                  = hash_block(requirement_data[i,0] + requirement_data[i,1])
        signature                 = wallet.sign_transaction(requirement_address, 
                                                       prev_requirement_address, 
                                                       requirement_data[i,2])
        data                      = [requirement_data[i,0], requirement_address, 
                                    prev_requirement_address, requirement_data[i,2], 
                                    wallet.public_key, signature]
        artifact_data[trans_id]   = data
        #artifact_data.append
    return artifact_data

#Adding block to the requirement chain
#It will check all the necessary conditions before adding a block
def add_block(RequirementChain, block):
    """ 
    Explanation:
    Arguments:
    Return values: 
    """
    ###Checking for hashes match
    #lock = Lock()
    #with lock:
    if len(RequirementChain)>0:
        hashes_match    = block["previous_hash"] == RequirementChain[-1]["hash"]
        #if not proof_is_valid or not hashes_match:
        if not hashes_match:
            message = "hashes not matching"
            return message, False
        #print("I am here")
        ###Checking for all the data field
        required_fields =  ["index", "previous_hash", "hash", 
                            "Time_Stamp", "name", "artifact_trace", 
                            "authors", "proof", "artifact_data"]
        verify_required_fields =  all(key in list(block.keys()) for key in required_fields)
        #print("required_fields: {}".format(not verify_required_fields))
        if not verify_required_fields:
                message = "some required fields missing"
                return message, False

        verify_artifact_trace_bool = verify_artifact_trace(RequirementChain, 
                                                            block["artifact_trace"])
        if not verify_artifact_trace_bool:
            message = "please recheck all the parent artifact ids"
            return message, False
        
        verify_artifact_data_trace_bool = verify_artifact_data_trace(RequirementChain, 
                                                            block["artifact_data"])
        if not verify_artifact_data_trace_bool:
            message = "please recheck all the parent objects"
            return message, False
        
        #verify_duplicate_object_bool = verify_duplicate_object(RequirementChain, 
        #                                                   block["artifact_data"])
        #if not verify_duplicate_object_bool:
        #    message = "Please recheck all the objects, some of the objects already exist"
        #    return message, False

        #print("I am here")
        ###Checking for valid proof
        no_of_zeros = 3
        length_chain  =  len(RequirementChain) + 1
        hash_data  = str(length_chain) + str(RequirementChain[-1]['previous_hash']) + str(block["Time_Stamp"])
        hash_data  = hash_data + str(block["name"])
        hash_data  = hash_data + json.dumps(block["artifact_trace"], 
                                            sort_keys = True)
        hash_data  = hash_data + str(block["authors"])
        hash_data  = hash_data + json.dumps(block["artifact_data"], 
                                            sort_keys = True)
        proof      = proof_of_work(hash_data, no_of_zeros)
        proof_is_valid  =  valid_proof(hash_data, proof, no_of_zeros)
        #print("Proof is valid: {}".format(not proof_is_valid))
        if not proof_is_valid:
            message = "proof is invalid"
            return message, False

        ###Signature verification
        #print("I am here")
        verify_sign = []
        for key1, artifact_data in block["artifact_data"].items():
            #print(artifact_data)
            #print(key1)
            #print(RSA.importKey(binascii.unhexlify(artifact_data[4])))
            verify_sign.append(verify_transaction(artifact_data, key1))
        #print("Verify signature: {}".format(not all(verify_sign)))
        if not all(verify_sign):
            message = "transactions are not verified"
            return message, False
        
    RequirementChain.append(block) 
    message = "good"
    return message, True

def verify_artifact_trace(RequirementChain, artifact_trace):
    counter = 0
    for i in range(len(artifact_trace)):
        for j in range(len(RequirementChain)):
            if artifact_trace[i][0] == RequirementChain[j]['hash']:
                counter = counter+1
    print("Counter: ".format(counter))
    #print("length of artifact_trace:".format(len(artifact_trace)))
    if counter == len(artifact_trace):
        return True
    return False

def verify_artifact_data_trace(RequirementChain, artifact_data):
    counter = 0
    Requirements_check=[]
    for j in range(len(RequirementChain)):
        for k in range(len(RequirementChain[j]['artifact_data'])):
            Requirements_check.append(list(RequirementChain[j]['artifact_data'].values())[k][1])
    for i in range(len(artifact_data)):
        if list(artifact_data.values())[i][2] in Requirements_check:
            counter = counter+1
    #print("Counter: ".format(counter))
    #print("length of artifact_trace:".format(len(artifact_trace)))
    if counter == len(artifact_data):
        return True
    return False

def verify_transaction(artifact_data, key1):
    data1      = artifact_data[1]
    data2      = artifact_data[2]
    #data3     = hash_block(artifact_data[2])
    data3      = artifact_data[3]
    public_key = artifact_data[4]
    signature  = artifact_data[5]
    #print(data1)
    #print(public_key)
    PK        = RSA.importKey(binascii.unhexlify(public_key))
    verifier  = PKCS1_v1_5.new(PK)
    h         = SHA256.new((str(data1) + str(data2) + str(data3)).encode("utf8"))
    return verifier.verify(h, binascii.unhexlify(signature))
#Create block class 
#Contains block data in "artifact"
#Contains previous block address in "previous_block_hash"
#Contain current block address in "block_hash"

def verify_duplicate_object(RequirementChain, artifact_data):
    counter = 0
    Requirements_check=[]
    for j in range(len(RequirementChain)):
        for k in range(len(RequirementChain[j]['artifact_data'])):
            Requirements_check.append(list(RequirementChain[j]['artifact_data'].values())[k][1])
    for i in range(len(artifact_data)):
        if list(artifact_data.values())[i][1] in Requirements_check:
            return False
    #print("Counter: ".format(counter))
    #print("length of artifact_trace:".format(len(artifact_trace)))
    #if counter == len(artifact_data):
    #    return True
    return True

class RequirementBlock:
    """ 
    Explanation:
    Arguments:
    Return values: 
    """
    def __init__(self, previous_block_hash, artifact):
        self.previous_block_hash = previous_block_hash        
        self.block_data          = artifact
        self.hash_data           = "" .join(artifact) + "; " + previous_block_hash
        self.block_hash          = hashlib.sha256(self.hash_data.encode()).hexdigest()
        #self.block_metadata      = [previous_block_hash, self.block_hash]

#Verify the chain
def verify_chain(RequirementChain):
    """ 
    Explanation:
    Arguments:
    Return values: 
    """
    is_valid = True
    for i in range(len(RequirementChain)-1):
        prev_block = RequirementChain[i]
        cur_block  = RequirementChain[i+1]
        if cur_block["previous_hash"] != prev_block["hash"]:
            is_valid = False
            return is_valid, i
    return is_valid, i

##Send block to all peer nodes
def send_block(block, peer_nodes):
    #lock2 = Lock()
    #with lock2:
    response_false_counter = 0
    for node in peer_nodes:
        url = "http://{}/broadcast_block".format(node)
        #print(url)
        response = requests.post(url, json={"block": block})
        #print(response.status_code)
        #print(response.message)
        print("Node {}: \n status code {}\n message {} ".format(node, response.status_code, response.text))
        if response.status_code >= 400 and response.status_code<=599:
            #print("Block declined, needs resolving")
            response_false_counter = response_false_counter + 1
    if response_false_counter == 0:
        #print("I am here")
        return True
    else: 
        return False

#Add requirement artifact
def add_requirement_artifact(name, depends_on, authors, artifact_data):
    """ Append a new value as well as the last blockchain value to the blockchain
    Arguments:
        :creater: The creater of the coins
        :approver: The approver of the coins
        :no_of_requirements: The no_of_requirements in the artifact
    """ 
    requirement_artifact = OrderedDict([("authors", list(authors)),
                                        ("artifact_trace", depends_on.tolist()),
                                        ("name",list(name)),
                                        ("artifact_data",artifact_data)])
    return requirement_artifact

#Valid proof
def valid_proof(hash_data, proof, no_of_zeros):
    """ 
    Explanation:
    Arguments:
    Return values: 
    """
    guess = (str(proof) + hash_data).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[0:no_of_zeros]=="0"*no_of_zeros

#Proof of work
def proof_of_work(hash_data, no_of_zeros):
    """ 
    Explanation:
    Arguments:
    Return values: 
    """
    proof      = 0
    while not valid_proof(hash_data, proof, no_of_zeros):
        proof += 1
    return proof

#Doing the time stamp
def time_stamp():
    ## getting the current time
    dt = datetime.now()
    ##getting the time stamp
    ts = datetime.timestamp(dt)
    return ts

#Mine the block
def mine_block(RequirementChain, open_requirements, peer_nodes, length_Chain):
    """ 
    Explanation:
    Arguments:
    Return values: 
    """
    #print("I am here")
    if len(RequirementChain) == 0:
        previous_hash = 'dummy'
    else: 
        previous_hash = RequirementChain[-1]["hash"]
    #print("I am after that")
    no_of_zeros = 3
    ts         = time_stamp()
    hash_data  = str(length_Chain) + str(previous_hash) + str(ts)
    hash_data  = hash_data + str(open_requirements["name"]) 
    hash_data  = hash_data + json.dumps(open_requirements["artifact_trace"], 
                                            sort_keys = True)
    hash_data  = hash_data + str(open_requirements["authors"])
    hash_data  = hash_data + json.dumps(open_requirements["artifact_data"], 
                                        sort_keys = True)
    proof      = proof_of_work(hash_data, no_of_zeros)
    hash_data  = str(proof) + hash_data  
    block = {
        "index": length_Chain, 
        "previous_hash": previous_hash,
        "hash": hash_block(hash_data),
        "Time_Stamp": ts,
        "name": open_requirements["name"],
        "artifact_trace": open_requirements["artifact_trace"],
        "authors": open_requirements["authors"],
        "proof": proof,
        "artifact_data":open_requirements["artifact_data"],
    }
    succeed = False
    if len(RequirementChain)>0:
        #print("I am here")
        succeed_trace = verify_artifact_trace(RequirementChain, block["artifact_trace"])
        message = "please recheck all the parent artifact ids"
        if succeed_trace:
            succeed_trace = verify_artifact_data_trace(RequirementChain, block["artifact_data"])
            #print(succeed_trace)
            message = "please recheck all the parent objects"
            #if succeed_trace:
            #    succeed_trace == verify_duplicate_object(RequirementChain, block["artifact_data"])
            #    message = "please recheck all the objects, there is some duplicates"
    else :
        succeed_trace = True
        message = "success"
    if succeed_trace:
        succeed = send_block(block, peer_nodes)
    if succeed:
        message = "Nodes accepted the block" 
    else: 
        message = "Some of the nodes Rejected the block" 
    #succeed = send_block(block, peer_nodes)
    return block, succeed, message