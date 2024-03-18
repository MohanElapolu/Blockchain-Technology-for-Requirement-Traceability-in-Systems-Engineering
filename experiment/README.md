# Introduction
## Scenario
1. The objective of this experiment is to generate requirements for an autonomous vehicle. System objective is <br>
   _A high-speed autonomous off-road reconnaissance vehicle._
3. Mission statements that provide the intended utility of the system is also given. You must generate mission, vehicle, and sub-system requirements.

## Tools
1. You need various tool to document and communicate the requirements.
2. Neo4J for graph-based visualization of requirements, a template to document the artifact and object traces, and the blockchain web application to upload the documents. Further details on the tools are provided in the following sections.

# Graph Visualization:   
## Neo4J browser
1. Neo4J browser will be opened and ready to use. Figure 1. Shows the sample requirement graph displayed in the Neo4J browser. The command used to generate the graph is
```
Match (n)
Return n
```
2. Before running the Neo4J code, user will be required to clear the graph database. The necessary command to delete existing graph database is
```
Match (n) 
Detach Delete n.
```

## Neo4J Code
1. The necessary python code to create graph will be opened in the visual studio (VS) and ready to use. The user must run this code to extract the information from the requirement chain text file and create Neo4J graph.
2. To run the Jupyter notebook code the user has to click the run button at the left of the cell as shown in the Figure 2.

# Data Collection
## Artifact Creation
1. Use the template as shown in Figure 3 and fill all the necessary requirement traceability information.
2. b.	Artifact Creators will be the stake holders involved in creating the artifact. <br>
   _Ex. Stake holder 1, Stake holder 2, Stake holder 3, Stake holder 4, Stake holder 5, Stake holder 6._
4. Artifact Name is the name of the artifact. Please use the below names to have consistency throughout the process. <br>
  _Ex: Mission Requirements, System Requirements, Vehicle Requirements, Subsystem Requirements, Minutes of Meeting, Operating Procedures_
4. Parent Artifact ID is the hash of the block that the current artifact depends on. This block can depend on more than one parent artifact. The parent artifact hash can be found from Neo4J browser as shown in Figure 4. You select the parent artifact block, and the hash will be found on the right side of the browser.
5. Object is the smallest possible element of the document of a design activity. For instance, in a requirement document, a requirement is the object. In Minutes of meeting, each critical bullet point can become an object.
6. Parent Object is the smallest possible element that the current Object depends on.
7. Link Type should be specified for artifact and object traces. Possible link types can be DEPENDS_ON, EVOLVED_TO, JUSTIFIES, SATISFIES. <br>
  The description of these links will be given using two sample objects “O1” (parent object) and “O2” (child object). < br>
  DEPENDS_ON: If “O2” is derived from “O1” and any changes in “O1” will affect “O2”. <br>
  EVOLVED_TO: If “O2” is newer version of “O1”. <br>
  JUSTIFIES: If “O2” supports and justifies the existence of “O1”. <br>
  SATISFIES: If “O2” satisfies “O1”. 
## Multiple parents
1. If a single object/artifact has multiple parents, we must create copies of the same object and document all the parent objects/artifacts and links types.   For instance, if object A has two parent objects B and C, it will be documented as shown in Figure 5.

# User Interface
## Home page
1. Figure 6 shows the home page of the user interface. User can start using the web application by clicking the start button.
## Login page
1. An existing user will enter the credentials in the login page which is shown in Figure 7.
2. New user will click on the Register button to create username and password. Figure 8 shows the web application page where user can create the account.
## Create wallet
1. For a new user once the account is created, he will be directed to the page as shown in Figure 9 for entering his wallet (public key and private key) details.
2. If user doesn’t have the public key and private key, he can click on Create Wallet and a new public key and private key is created for the user. He can check the details of the wallet by clicking on My wallet on the top task bar of the web application as shown in Figure 9.
## Upload artifact
1. a.	To upload the artifact, user will be using the page as shown in Figure 10. The user will provide the link of the artifact in the slot Enter Path to requirement artifact and uploads the artifact by clicking Add Requirement Block. If the upload is successful, the newly created block will be shown, if not the error in uploading the artifact is shown. 
