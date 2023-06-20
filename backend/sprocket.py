from flask import Flask, jsonify, request
import database as db
import os

#Initiate MongoDB
db_instance = db.DataBase()

app = Flask(__name__)

#GET /sprocket/all
#Returns all sprocket factory data
@app.route("/sprockets/all", methods=["GET"])
def get_allsprockets():
    return jsonify(db_instance.get_data('sprocket'))

#GET /factory/{id}
#Returns factory data for a given factory id
@app.route("/factory/<int:factory_id>", methods=["GET"])
def get_factory(factory_id):
    #Check if factory exist
    if not db_instance.check_data('factory', {"id": factory_id}):
        return jsonify({"Error": "ID not found"}), 404
    
    return jsonify(db_instance.get_data('factory', {"id": factory_id}))

#GET /sprocket/{id}
#Returns sprockets for a given id
@app.route("/sprocket/<int:sprocket_id>", methods=["GET"])
def get_sprocket(sprocket_id):
    #Check if sprocket exist
    if not db_instance.check_data('sprocket', {"id": sprocket_id}):
        return jsonify({"Error": "ID not found"}), 404
    
    return jsonify(db_instance.get_data('sprocket', {"id": sprocket_id}))

#POST /sprocket/new
#Create new sprocket
@app.route("/sprocket/new", methods=["POST"])
def create_sprocket():
    new_sprocket = request.get_json()
    #Check if new sprocket has a unique id
    if db_instance.check_data('sprocket', {"id": new_sprocket['id']}):
        return jsonify({"Error": "ID not unique"}), 404
    
    db_instance.add_data('sprocket', new_sprocket)
    return jsonify({'Message': 'Data created successfully'})

#PUT /sprocket/update/{id}
#Update sprocket for a given id
@app.route("/sprocket/update/<int:sprocket_id>", methods=["PUT"])
def update_sprocket(sprocket_id):
    update_sprocket = request.get_json()
    #Check if sprocket exist
    if not db_instance.check_data('sprocket', {"id": sprocket_id}):
        return jsonify({"Error": "ID not found"}), 404
    
    db_instance.update_data('sprocket', {"id": sprocket_id}, update_sprocket)
    return jsonify({'Message': 'Data updated successfully'})

if __name__ == "__main__":
    #Seeding sprocket and factory datas
    db_instance.seed_data('sprocket', os.environ['SEED_PATH'] + '/seed_sprocket_types.json')
    db_instance.seed_data('factory',  os.environ['SEED_PATH'] + '/seed_factory_data.json')

    #Run Flask app
    app.run()

