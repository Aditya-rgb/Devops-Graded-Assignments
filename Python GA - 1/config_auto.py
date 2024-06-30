import yaml  # Import YAML for parsing YAML files
import json  # Import JSON for JSON serialization
import os    # Import OS for interacting with the operating system
import glob  # Import Glob for file path matching
from flask import Flask, request, jsonify  # Import Flask for web framework, request handling, and JSON response
from pymongo import MongoClient  # Import MongoClient from pymongo for MongoDB interaction

# Initialize Flask application
app = Flask(__name__)

# Connect to MongoDB server running on localhost
client = MongoClient('mongodb://localhost:27017/')

# Select or create a database named 'myconfigdata'
db = client['myconfigdata']

# Select or create a collection named 'configs' within the database
collection = db['configs']

# Test MongoDB connection
try:
    client.server_info()  # Check if MongoDB server is available
    print("MongoDB connected successfully!")
except Exception as e:
    print(f"Error connecting to MongoDB: {e}")

# Route for the root URL to verify MongoDB connection status
@app.route('/')
def index():
    try:
        client.server_info()  # Check MongoDB server status
        return "MongoDB connected successfully!"
    except Exception as e:
        return f"Error connecting to MongoDB: {e}"

# Route to insert YAML configurations into MongoDB
@app.route('/insert', methods=['POST'])
def convert_and_insert():
    try:
        cwd = os.getcwd()  # Get current working directory
        yaml_files = glob.glob(os.path.join(cwd, "*.yaml"))  # Find all YAML files in the current directory

        if yaml_files:
            print("Config files found")
            for file in yaml_files:
                try:
                    with open(file, 'r') as config:
                        yaml_data = yaml.safe_load(config)  # Safely load YAML data from file
                        if not yaml_data:
                            raise ValueError(f"YAML file {os.path.basename(file)} is empty or invalid")
                        
                        
                        # Optionally save the JSON file (not necessary for MongoDB insert)
                        json_data = json.dumps(yaml_data, indent=2)  # Convert YAML to JSON for readability
                        json_file = open(f"{os.path.basename(file)}.json", "w")  # Create a JSON file
                        json_file.write(json_data)  # Write JSON data to file
                        json_file.close()  # Close the JSON file after writing

                        # Insert JSON data into MongoDB as a dictionary
                        collection.insert_one(yaml_data)
                        
                        print(f"Converted file '{os.path.basename(file)}' and inserted into MongoDB")
                
                except yaml.YAMLError as yaml_error:
                    print(f"Error parsing YAML file {os.path.basename(file)}: {yaml_error}")
                    # Log specific YAML parsing errors
                except ValueError as ve:
                    print(ve)
                    # Log specific value errors, e.g., empty YAML file
                except Exception as e:
                    print(f"An error occurred while processing {os.path.basename(file)}: {e}")
                    # Log any other unexpected errors while processing files

            return jsonify({'message': 'All YAML files processed and inserted into MongoDB'}), 200

        else:
            print("No config YAML files found!!")
            return jsonify({'message': 'No config YAML files found'}), 404
                
    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
    
# Route to fetch all configurations from MongoDB
@app.route('/configs', methods=['GET'])
def get_configs():
    try:
        # Fetch all documents from the 'configs' collection as a list of dictionaries
        cursor = collection.find({})
        config_list = list(cursor)
        
        # Serialize the list of dictionaries to JSON
        json_data = json.dumps(config_list, default=str)  # Handle ObjectId serialization
        
        # Return JSON response
        return jsonify(json_data), 200
    
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

# Run the Flask application in debug mode
if __name__ == '__main__': 
    app.run(debug=True)
