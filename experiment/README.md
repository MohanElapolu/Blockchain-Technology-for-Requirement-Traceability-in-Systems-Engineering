# Introduction
## Scenario
1. The objective of this experiment is to generate requirements for an autonomous vehicle. System objective is <br>
   _A high-speed autonomous off-road reconnaissance vehicle._
2. In this experimental scenario, three teams will collaborate to generate the requirements based on the system objective.
3. The requirement artifacts which are given to each team is there in directories Team_1 , Team_2, Team_3.
4. The mission statements that provide the intended utility of the system is also given.
5. Teams must generate and document mission, vehicle, and sub-system requirements in that heierarchy.
6. For more details about this scenario, check our paper "Blockchain Technology for Requirement Traceability in Systems Engineering"

## Tools
1. Teams use various tools to document and communicate the requirements.
2. Neo4J for graph-based visualization of requirements, a template to document the artifact and object traces, and the blockchain web application to upload the documents. Further details on the tools are provided in the following sections.

# Graph Visualization:   
## Neo4J browser
1. Download and install Neo4J following the instructions in their website. Figure 1, Shows the sample requirement graph displayed in the Neo4J browser. However, at the beginining of the experiment there won't be any information to display. Hence no graph is seen. The command used to generate the graph is
```
Match (n)
Return n
```
![](/experiment/assets/neo4j_browser.png) <br>
*Figure 1: Neo4J requirement graph* <br>
<br>
2. Graph visualization code is in the visualization directory. Before running the Neo4J code, user will be required to clear the graph database. The necessary command to delete existing graph database is
```
Match (n) 
Detach Delete n.
```
## Neo4J Code
1. The necessary python code to create graph will be opened in the visual studio (VS) and ready to use. The user must run this code to extract the information from the RequirementChain text file and create Neo4J graph.
2. To run the Jupyter notebook code the user has to click the run button at the left of the cell as shown in the Figure 2. <br>

![](/experiment/assets/neo4j_code_snippet.png) <br>
*Figure 2: Portion of python code to create the Neo4J commands.* <br>
<br>

# Data Collection
## Artifact Creation
1. Use the template as shown in Figure 3 and fill all the necessary requirement traceability information. <br>
   
![](/experiment/assets/art_template.png) <br>
*Figure 3: Template to fill the necessary requirements traceability information* <br>
<br> 

3. Artifact Creators will be the stake holders involved in creating the artifact. <br>
   _Ex. Stake holder 1, Stake holder 2, Stake holder 3, Stake holder 4, Stake holder 5, Stake holder 6._
4. Artifact Name is the name of the artifact. Please use the below names to have consistency throughout the process. <br>
  _Ex: Mission Requirements, System Requirements, Vehicle Requirements, Subsystem Requirements, Minutes of Meeting, Operating Procedures_
5. Parent Artifact ID is the hash of the block that the current artifact depends on. This block can depend on more than one parent artifact. The parent artifact hash can be found from Neo4J browser as shown in Figure 4. You select the parent artifact block, and the hash will be found on the right side of the browser. <br> 

![](/experiment/assets/neo4j_browser_2.png) <br>
*Figure 4: Neo4j graph showing the hash of the block 0.* <br>
<br>

7. Object is the smallest possible element of the document of a design activity. For instance, in a requirement document, a requirement is the object. In Minutes of meeting, each critical bullet point can become an object.
8. Parent Object is the smallest possible element that the current Object depends on.
9. Link Type should be specified for artifact and object traces. Possible link types can be DEPENDS_ON, EVOLVED_TO, JUSTIFIES, SATISFIES. <br> 

## Multiple parents
1. If a single object/artifact has multiple parents, we must create copies of the same object and document all the parent objects/artifacts and links types.   For instance, if object A has two parent objects B and C, it will be documented as shown in Figure 5. <br>
   
![](/experiment/assets/art_template2.png) <br>
*Figure 5: A sample artifact illustrating the scenario where one object "A" has two parent objects "B" and "C".* <br>
<br> 

# User Interface
## Home page
1. Figure 6 shows the home page of the user interface. User can start using the web application by clicking the start button. <br>
   
![](/experiment/assets/web_app_welcome.png) <br>
*Figure 6: Home page of the web application* <br>
<br> 

## Login page
1. An existing user will enter the credentials in the login page which is shown in Figure 7. <br>
   
![](/experiment/assets/web_app_login.png) <br>
*Figure 7: Login Page of the web application* <br>
<br> 

3. New user will click on the Register button to create username and password. Figure 8 shows the web application page where user can create the account. <br>
   
![](/experiment/assets/web_app_create_account.png) <br>
*Figure 8: Create account page of the web application.* <br>
<br> 

## Create wallet
1. For a new user once the account is created, he will be directed to the page as shown in Figure 9 for entering his wallet (public key and private key) details. <br>

![](/experiment/assets/web_app_create_wallet.png) <br>
*Figure 9: Wallet page of the web application.* <br>
<br> 

3. If user doesn’t have the public key and private key, he can click on Create Wallet and a new public key and private key is created for the user. He can check the details of the wallet by clicking on My wallet on the top task bar of the web application as shown in Figure 9.

## Upload artifact
1. a.	To upload the artifact, user will be using the page as shown in Figure 10. The user will provide the link of the artifact in the slot Enter Path to requirement artifact and uploads the artifact by clicking Add Requirement Block. If the upload is successful, the newly created block will be shown, if not the error in uploading the artifact is shown. <br>
   
![](/experiment/assets/web_app_upload_artifact.png) <br>
*Figure 10: The page to upload the artifact.* <br>
<br> 

