 def return_file():
     try:
         file = request.args.get('file')
        return send_file(os.path.join(os.getcwd(), file))
     except Exception as e:
         return str(e)
 