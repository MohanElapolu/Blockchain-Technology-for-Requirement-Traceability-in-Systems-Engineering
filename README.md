# Blockchain application for Requirement Traceability

## Setup the application
1. Download the blockchain_app directory...
2. Create and activate the virtual environment in the blockchain_app directory:
  - Windows
```
python -m venv venv
.\venv\Scripts\activate
```
  - macOS
```
python3 -m venv venv
source venv/bin/activate
```
3. Install all the dependencies in the virtual environment
```
pip install -r dependencies.txt
```
4. Run the local node and web app:
```
python run.py
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
   
![](/assets/web_app_welcome.png) <br>
*Figure 1: Home page of the web application* <br>
<br> 

### Login page
1. An existing user will enter the credentials in the login page which is shown in Figure 2. <br>
   
![](/assets/web_app_login.png) <br>
*Figure 2: Login Page of the web application* <br>
<br> 

3. New user will click on the Register button to create username and password. Figure 3 shows the web application page where user can create the account. <br>
   
![](/assets/web_app_create_account.png) <br>
*Figure 3: Create account page of the web application.* <br>
<br> 

### Create wallet
1. For a new user once the account is created, he will be directed to the page as shown in Figure 4 for entering his wallet (public key and private key) details. <br>

![](/assets/web_app_create_wallet.png) <br>
*Figure 4: Wallet page of the web application.* <br>
<br> 

3. If user doesn’t have the public key and private key, he can click on Create Wallet and a new public key and private key is created for the user. He can check the details of the wallet by clicking on My wallet on the top task bar of the web application as shown in Figure 4.

### Upload artifact
1. To upload the artifact, user will be using the page as shown in Figure 5. The user will provide the link of the artifact in the slot Enter Path to requirement artifact and uploads the artifact by clicking Add Requirement Block. If the upload is successful, the newly created block will be shown, if not the error in uploading the artifact is shown. <br>
   
![](/assets/web_app_upload_artifact.png) <br>
*Figure 5: The page to upload the artifact.* <br>
<br> 


### Experiment
1. Follow the instructions in the experiment directory to replicate and use the various functionalities of the framework
