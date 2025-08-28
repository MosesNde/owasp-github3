 app = Flask(__name__)
 if __name__ == '__main__':
     app.run(threaded=True) # Run threaded so we can test how our bg process works
app.config["MONGO_URI"] = "mongodb://admin:password@db:27017/my_database?authSource=admin"
 mongo = PyMongo(app)
 
 @app.route("/")