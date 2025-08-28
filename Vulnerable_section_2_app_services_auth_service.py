     role_id = m.Role.query.filter_by(name="patient").first().id
 
     # Add picture
    pic_id = m.UploadedFile.query.filter_by(file_name="default").first().id
 
     # Convert string to date object
     dob_str = user_data["dob"]  # This comes from your input data