 app.register_blueprint(api_bp, url_prefix="/api")
 
 if __name__ == '__main__':
     debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
     app.run(debug=debug_mode)