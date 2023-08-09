
from flask import Flask, jsonify
import os
from api.views import blueprint
#--- env
from dotenv import load_dotenv
#--- database
from extensions import db
from extensions import migrate



load_dotenv()



app = Flask(__name__)
app.register_blueprint(blueprint=blueprint)
app.config.from_object("config")


db.init_app(app)
migrate.init_app(app,db)
#debug = os.environ.get("FLASK_DEBUG", False)

if __name__ == "__main__":
    app.run(host=os.environ.get("FLASK_RUN_HOST", "0.0.0.0"), 
            port=os.environ.get("FLASK_RUN_PORT", 8000), 
            debug=True)
    
