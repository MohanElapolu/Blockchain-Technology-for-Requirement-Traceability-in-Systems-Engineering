## Flask module will allow to setup the Flask application which is a server
## render_template module will allow you to import the html files in templates directory
## Flask module will allow to setup the routes or api end-points 
from flask import Flask, render_template, jsonify
from flask import redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from flask_cors import CORS
from sympy import block_collapse
from threading import Lock

## Applications and modules from Blockchain
from requirement_chain import app, db
from requirement_chain.wallet import Wallet
from requirement_chain.blockchain_operations import *
from requirement_chain.file_operations import *
from requirement_chain.user_inputs import *
from requirement_chain.genesis_block import *
from requirement_chain.models import User
from requirement_chain.forms import RegisterForm, LoginForm, WalletForm, AddBlockForm, RemoveNodeForm, AddNodeForm

## This is Flask application
#app = Flask(__name__)
## You are importing wallet to set it up from the beginining
## Make blockchain as an object
## Work on this code ##
## CORS is a mechanism allows other nodes connect to it
#CORS(app)

## To send a dummy request you have to create end-points
## This block with bunch of decorators will allow us to do that

## This is a test route 
## Route is just an end-point
## 1st argument is the path
## 2nd argument is the type of request
@app.route("/")
@app.route("/Home")
def home_page():
    #print(request.host.split(":")[1])
    return render_template("home.html")

#@login_manager.user_loader
#def load_user(user_id):
#    return User.query.get(user_id)

@app.route("/contact_us")
def contact_us_page():
    return render_template("contact_us.html")

@app.route("/more_info")
def more_info_page():
    return render_template("more_info.html")

## Wallet page to load or create wallet
@app.route("/wallet_page")
@login_required
def wallet_page():
    return render_template("my_wallet.html")

## This route is to navigate to selection page
## The selection page allows to perform different functionalities with blockchain
@app.route("/RequirementChain", methods=["POST", "GET"])
@login_required
def requirement_page():
    if current_user.public_key:
        form =  AddBlockForm()
        if form.validate_on_submit():
            name, depends_on, authors, requirement_data = get_user_input(form.path_artifact.data)
            RequirementChain, peer_nodes                = get_requirement_chain()
            wallet = Wallet()
            wallet.public_key = current_user.public_key
            wallet.private_key = current_user.private_key
            artifact_data                               = get_artifact_data(requirement_data, wallet)
            requirement_artifact                        = add_requirement_artifact(name, depends_on, authors, artifact_data)
            length_Chain                                = len(RequirementChain)
            block, succeed, mine_block_message          = mine_block(RequirementChain, requirement_artifact, peer_nodes, length_Chain)
            if succeed:
                add_block_message, add_block_success = add_block(RequirementChain, block)
                if add_block_success:
                    save_data(RequirementChain, peer_nodes)
                    response = {"message": "Block Added Successfully", "block": [block], "Id": [0], "numb":[len(RequirementChain)-1]}
                    return render_template('added_block.html', response=response)
                else:
                    message = "There was an error in adding the block, " + add_block_message
                    flash(message, category="danger")
            else:
                message = "There was an error in minnig the block, " + mine_block_message
                flash(message, category="danger")  
        if form.errors !={}: #If there are not errors from the validators
            for err_msg in form.errors.values():
                flash("There was an error in adding the block: {}".format(err_msg), category="danger")
        return render_template("RequirementChain.html", form=form)
    else:
        form =  WalletForm()
        if form.validate_on_submit():
            current_user.public_key = form.public_key.data
            current_user.private_key = form.private_key.data
            db.session.commit()
            #login_user(user_to_create)
            flash("Wallet created successfully!", category="info")
            return redirect( url_for("requirement_page") ) 
        if form.errors !={}: #If there are not errors from the validators
            for err_msg in form.errors.values():
                flash("There was an error in createing the wallet: {}".format(err_msg), category="danger")
        return render_template("load_wallet.html", form=form)


##This route will broadcast the block
@app.route("/broadcast_block", methods=["POST", "GET"])
def broadcast_block():
    if request.method == "POST":
        block1 = request.get_json()
        block = block1["block"]
        if not block:
            response = {"message": "No data found."}
            return jsonify(response), 400
        required = ["index","previous_hash", "hash", "Time_Stamp",
                    "name", "artifact_trace", "authors",
                    "proof", "artifact_data"]
        if not all(key in list(block.keys()) for key in required):
            response = {"message": "Some data is missing"}
            return jsonify(response), 400
        RequirementChain, peer_nodes = get_requirement_chain()
        if len(RequirementChain) == 0:
            add_block_message, add_block_success = add_block(RequirementChain, block)
            if add_block_success:
                save_data(RequirementChain, peer_nodes)
                response = {"message": "Block added successfully"}
                return jsonify(response), 201
            else:
                response = {"message": "Block seems invalid because " + add_block_message}
                return jsonify(response), 501

        else:
            if block["index"] ==  RequirementChain[-1]["index"]+1:
                add_block_message, add_block_success = add_block(RequirementChain, block)
                if add_block_success:
                    save_data(RequirementChain, peer_nodes)
                    response = {"message": "Block added successfully"}
                    return jsonify(response), 201
                else:
                    response = {"message": "Block seems invalid because " + add_block_message}
                    return jsonify(response), 501
            #elif block["index"] < RequirementChain[-1]["index"]:
            #    pass
            else:
                response = {"message": "Blockchain seems to be shorter, block not added"}
                return jsonify(response), 409
    #if request.method == "GET":
    #    print("I came here first: {}".format(request.method))
    return render_template("broadcast_block.html")

## This route will take you to the network page
@app.route("/add_node_page", methods=["POST","GET"])
@login_required
def add_node_page():
    form = AddNodeForm()
    if form.validate_on_submit():

        """
        if not values:
            response = {
                "message": "No data attached"
            }
            return jsonify(response), 400
        if "node" not in values:
            response = {
                "message": "No node data found"
            }
        """
        RequirementChain, peer_nodes = get_requirement_chain()
        peer_nodes.add(form.add_Node_URL.data)
        save_data(RequirementChain, peer_nodes)
        flash("Node added to network successfully", category="info")
        """
        response = {
            "message": "Node added successfully",
            "all_nodes": list(peer_nodes)
        }
        """
        return render_template("add_node.html", form=form)
    if form.errors !={}:
        for err_msg in form.errors.values():
            flash("There was an error in adding the node to network: {}".format(err_msg), category="danger")
    return render_template("add_node.html", form=form)

## This route will take you to the network page
@app.route("/remove_node_page", methods=["POST", "GET"])
@login_required
def remove_node_page():
    form = RemoveNodeForm()
    if form.validate_on_submit():
        """
        if not values:
            response = {
                "message": "No data attached"
            }
            return jsonify(response), 400
        if "node" not in values:
            response = {
                "message": "No node data found"
            }
        """
        #print("I am here")
        RequirementChain, peer_nodes = get_requirement_chain()
        if form.remove_Node_URL.data in list(peer_nodes):
            peer_nodes.remove(form.remove_Node_URL.data)
            save_data(RequirementChain, peer_nodes)
            flash("Node removed from network successfully", category="info")
        else:
            flash("Node URL is not in the network", category="danger")
        """
        response = {
            "message": "Node added successfully",
            "all_nodes": list(peer_nodes)
        }
        """
        return render_template("remove_node.html", form=form)
    if form.errors !={}:
        for err_msg in form.errors.values():
            flash("There was an error in adding the node to network: {}".format(err_msg), category="danger")
    return render_template("remove_node.html", form=form)


## This route creates the wallet
@app.route("/create_wallet")
def create_wallet_page():
    wallet = Wallet()
    wallet.create_keys()
    current_user.public_key  =  wallet.public_key
    current_user.private_key =  wallet.private_key
    db.session.commit()
    flash("Wallet Created Successfully!", category="info")
    return redirect( url_for("requirement_page") )

##Registration page route
@app.route("/load_wallet", methods=["GET","POST"])
def load_wallet_page():
    form =  WalletForm()
    if form.validate_on_submit():
        current_user.public_key = form.public_key.data
        current_user.private_key = form.private_key.data
        db.session.commit()
        #login_user(user_to_create)
        flash("Wallet created successfully!", category="info")
        return redirect( url_for("requirement_page") ) 
    if form.errors !={}: #If there are not errors from the validators
        for err_msg in form.errors.values():
            flash("There was an error in createing the wallet: {}".format(err_msg), category="danger")
    return render_template("load_wallet.html", form=form)

## This route adds the new block to the requirement chain
@app.route("/add_genesis_block")
def add_genesis_block():
    #print("I am here")
    #RequirementChain = []
    wallet = Wallet()
    #wallet_name = input("Enter the wallet name: ")
    wallet.public_key = current_user.public_key
    wallet.private_key = current_user.private_key
    RequirementChain, peer_nodes = get_requirement_chain()
    RequirementChain = []
    RequirementChain.append(genesis(wallet, peer_nodes))
    save_data(RequirementChain, peer_nodes)
    response = {"message": "Block Added Successfully", "block": RequirementChain, "Id": [0], "numb":[len(RequirementChain)-1]}
    return render_template("added_block.html", response=response)

##Registration page route
@app.route("/register", methods=["GET","POST"])
def register_page():
    form =  RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, 
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash("Account created successfully! You are now logged in as {}".format(user_to_create.username), category="info")
        return redirect( url_for("load_wallet_page") ) 
    if form.errors !={}: #If there are not errors from the validators
        for err_msg in form.errors.values():
            flash("There was an error with creating a user: {}".format(err_msg), category="danger")
    return render_template("register.html", form=form)

##Login page route
@app.route("/login", methods=["GET", "POST"])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
            attempted_password=form.password.data
            ):
            login_user(attempted_user)
            flash("Success! You are logged in as: {}".format(attempted_user.username), category="success")
            return redirect(url_for("requirement_page"))
        else:
            flash("Username and password does not match! Please try again", category="danger")
    if form.errors !={}: #If there are not errors from the validators
        for err_msg in form.errors.values():
            flash("There was an error with logining in user: {}".format(err_msg), category="danger")
    return render_template("login.html", form=form)

##Logout page route
@app.route("/logout")
def logout_page():
    logout_user()
    flash("You have been logged out!", category="info")
    return redirect(url_for("home_page"))
    
## This route gets the requirement chain 
@app.route("/get_chain", methods=['GET'])
def get_chain():
    print(10)
    print(request.host)
    RequirementChain, peer_nodes = get_requirement_chain()
    response = {"message": "Complete Blockchain", "block": RequirementChain, "Id": list(range(len(RequirementChain))), "numb": list(range(len(RequirementChain)))}
    return render_template('added_block.html', response=response)


## this route will get all nodes in the network
@app.route("/get_node_page", methods=["GET"])
@login_required
def get_node_page():
    RequirementChain, peer_nodes = get_requirement_chain()
    
    return render_template("get_node.html", peer_nodes = list(peer_nodes))