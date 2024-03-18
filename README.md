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
1. To broadcast the app running in the local network, you can use ngrok. Register and follow the instructions to download the ngrok. Suppose your loacal network is running on https://localhost:5000, in the ngrok terminal you use the below command..
```
ngrok http 5000
```
2. The ngrok will provide you the address that can be accessed by your peers.

## Experiment
1. Follow the instructions in the experiment directory to replicate and use the various functionalities of the framework
