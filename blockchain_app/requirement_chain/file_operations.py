##File operations...

#Importing all the required modules
import json
#import pickle
from collections import OrderedDict
#import hashlib
#import print_func 
import pandas as pd
import numpy as np
import os

#Importing all the inhouse modules
from requirement_chain.hash_utils import hash_block

#Reading data from the artifact
def read_data(path):
    """ 
    Explanation:
    Arguments:
    Return values: 
    """
    with open(path, mode = "r") as d_f:
        artifact = d_f.readlines()
    #try:
    #except IOError:
    #    print("File not found!")
    return artifact

def read_file_pd(path):
    #parent_requirement= input("Enter the name of parent requrirement")
    artifact_data      = pd.read_excel(path)
    #artifact          = artifact_data.values
    authors            = artifact_data.iloc[:,0].dropna().values
    name               = artifact_data.iloc[:,1].dropna().values
    depends_on         = artifact_data.iloc[:,2:4].dropna().values
    #relation_type     = artifact_data.iloc[:,3].dropna().values
    #depends_on        = [[related_to[i], relation_type[i]] for i in range(len(related_to))]
    requirements_list  = artifact_data.iloc[:,4:7].dropna(subset=["Object"]).values
    #artifact_depends_on = artifact_data.iloc[:,6].dropna(subset=["Artifact Depends on"]).values
    #for i in range(len(artifact[:,2])):
    #    if ~np.isnan(artifact[i,2]):
    #        artifact_data.append((artifact[i,2],artifact[i,3],artifact[i,4]))
    #artifact_name = np.array(artifact_name)
    #authors       = np.array(authors)
    #artifact_data = np.array(artifact_data)
    return name[:], depends_on[:], authors[:], requirements_list[:,:]

#Saving data from the requirement chain
def save_data(RequirementChain, peer_nodes):
    """ 
    Explanation:
    Arguments:
    Return values:
    """
    path = "RequirementChain" + ".txt"
    with open(path, mode="w") as d_f:
        d_f.write(json.dumps(RequirementChain))
        d_f.write("\n")
        d_f.write(json.dumps(list(peer_nodes)))
        #for i in range(len(RequirementChain)):
        #    d_f.write(json.dumps(RequirementChain[i]))
        #    d_f.write("\n")
        #d_f.write(json.dump(open_requirements))
        #save_data = {
        #    "chain" : RequirementChain
        #}
        #d_f.write(pickle.dumps(save_data))
    #return artifact

#Loading data from the requirement chain
def load_data():
    """ 
    Explanation:
    Arguments:
    Return values:
    """
    path = "RequirementChain"+".txt"

    if os.path.isfile(path):
        with open(path, mode="r") as d_f:
            #file_content = pickle.loads(d_f.read())
            #RequirementChain = file_content["chain"]
            file_content = d_f.readlines()
            RequirementChain = json.loads(file_content[0])
            #open_requirements = file_content[1]
            #print(file_content)
            if len(file_content)==2:
                peer_nodes = set(json.loads(file_content[1]))
            else:
                peer_nodes = set()
    else:
        RequirementChain = []
        peer_nodes  = set()
    return RequirementChain, peer_nodes