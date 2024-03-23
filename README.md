# Blockchain application for Requirement Traceability

## Setup the application
1. Prerequisites: conda and python should be installed. Conda version 23.11.2 and up, Python version 3.11.2 and up, should work. 

3. Create and activate the virtual conda environment:
  - Windows (open anaconda prompt terminal)
```
$ conda create --name bc-env
$ conda activate bc-env
```
3. Download the blockchain_app directory. Open the anaconda prompt terminal in this directory.
4. Activate the conda virtual environment _bc-env_.
5. Install all the dependencies in the virtual environment
```
$ pip install -r dependencies.txt
```
4. Run the local node and web app:
```
$ python run.py
```
5. Your app is up and running, copy the address and paste it onto any web browser. This will direct you to homepage of the web application.

## Ngrok (optional)
1. To broadcast the app running in the local network, you can use ngrok. Register and follow the instructions to download the ngrok. For instance, your app is running on local network https://localhost:5000, the below command can be used in the ngrok terminal that allows local network accessible to everyone..
```
ngrok http 5000
```
2. The ngrok will provide you the address that can be accessed by your peers.
   
## Web-app User Interface
### Home page
1. Figure 1 shows the home page of the user interface. User can start using the web application by clicking the start button. <br>
   
![](/assets_main/web_app_welcome.png) <br>
*Figure 1: Home page of the web application* <br>
<br> 

### Login page
1. An existing user will enter the credentials in the login page which is shown in Figure 2. <br>
   
![](/assets_main/web_app_login.png) <br>
*Figure 2: Login Page of the web application* <br>
<br> 

3. New user will click on the Register button to create username and password. Figure 3 shows the web application page where user can create the account. <br>
   
![](/assets_main/web_app_create_account.png) <br>
*Figure 3: Create account page of the web application.* <br>
<br> 

### Create wallet
1. For a new user once the account is created, he will be directed to the page as shown in Figure 4 for entering his wallet (public key and private key) details. <br>

![](/assets_main/web_app_create_wallet.png) <br>
*Figure 4: Wallet page of the web application.* <br>
<br> 

3. If user doesn’t have the public key and private key, he can click on Create Wallet and a new public key and private key is created for the user. He can check the details of the wallet by clicking on My wallet on the top task bar of the web application as shown in Figure 4.

### Add peers of the network
1. Before proceeding to upload the artifact, we should create a network. The _URL_ of the peers can be added using _network page_ of the web app as shown in Figure 5. Just provide the link in the field and click add. To make a local network global you can use _Ngrok_, some information is given in the _Ngrok_ section of this writeup. Similarly, all the peers should add your _URL_ as well, in this way we can create a node network.

![](/assets_main/web_app_network.png) <br>
*Figure 5: Network page of the web application.* <br>
<br> 

### Upload artifact
1. To upload the artifact (excel file), user will be using the page as shown in Figure 6. The user will provide the link of the artifact in the field _Enter Path to requirement artifact_ and uploads the artifact by clicking Add Requirement Block. If the upload is successful, the newly created block will be shown, if not the error in uploading the artifact is shown. <br>
   
![](/assets_main/web_app_upload_artifact.png) <br>
*Figure 6: The page to upload the artifact.* <br>
<br> 

## First Artifact (genesis block)
1. Use the template as shown in Figure 7 and fill all the necessary requirement traceability information. The sample template _artifact_template.xlsx_ is given in the home directory of the repository. <br>
   
![](/experiment/assets/art_template.png) <br>
*Figure 7: Template to fill the necessary requirements traceability information* <br>
<br> 

3. Artifact Creators will be the stake holders involved in creating the artifact. <br>
   _Ex. Stake holder 1, Stake holder 2, Stake holder 3, Stake holder 4, Stake holder 5, Stake holder 6._
4. Artifact Name is the name of the artifact. Please use the below names to have consistency throughout the process. <br>
  _Ex: Mission Requirements, System Requirements, Vehicle Requirements, Subsystem Requirements, Minutes of Meeting, Operating Procedures_
5. Parent Artifact ID is the hash of the block that the current artifact depends on. But for the first artifact there is no parent artificat. So you can give "no parent artifact".
7. Object is the smallest possible element of the document of a design activity. For instance, in a requirement document, a requirement is the object. In Minutes of meeting, each critical bullet point can become an object. For the first artifact it can be the system objective.
   _Ex. This is the system objective_
9. Parent Object is the smallest possible element that the current Object depends on. For the first artifact there is no parent objets. So, you can give "no parent object"
10. Link Type should be specified for artifact and object traces. Possible link types can be DEPENDS_ON, EVOLVED_TO, JUSTIFIES, SATISFIES. For the first aritfact as there are no parent objects you can give "not-applicable".


## Graph Visualization:   
Download and install Neo4J following the instructions from Neo4J website. You also need the file _graph_visualization.ipynb_ from _graph_visualization_ directory in this repository.
### Neo4J browser
1. Create Neo4J database and open Neo4J browser. Credentials used to create the database is needed for your Neo4J code.
2. Neo4J browser displays the graph. The command used to generate the graph is
```
Match (n)
Return n
```
3. However, at the beginining of the experiment there won't be any information to display. Hence no graph is seen.
4. Graph visualization code is in the visualization directory. Before running the Neo4J code, user will be required to clear the graph database. In case if there is any unwanted graph, the necessary command to delete existing graph database is
```
Match (n) 
Detach Delete n.
```
### Neo4J Code
1. The necessary python code to create graph will be opened in the visual studio (VS) and ready to use. The user must run this code to extract the information from the RequirementChain text file and create Neo4J graph.
2. To run the Jupyter notebook code the user has to click the run button at the left of the cell as shown in the Figure 2. <br>

![](/experiment/assets/neo4j_code_snippet.png) <br>
*Figure 2: Portion of python code to create the Neo4J commands.* <br>
<br>
3. Now if you run the below command you should be able to see the requirement graph. 
```
Match (n)
Return n
```

### Experiment
1. Follow the instructions in the experiment directory to replicate and use the various functionalities of the framework
