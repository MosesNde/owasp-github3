     sanitized = sanitized.replace('>', '&gt;')
     sanitized = sanitized.replace('"', '&quot;')
     sanitized = sanitized.replace("'", '&#x27;')
    
    # Handle potential javascript: URLs and similar schemes
    sanitized = re.sub(r'(?i)javascript:', 'blocked:', sanitized)
    sanitized = re.sub(r'(?i)data:', 'blocked:', sanitized)
    sanitized = re.sub(r'(?i)vbscript:', 'blocked:', sanitized)
    sanitized = re.sub(r'(?i)file:', 'blocked:', sanitized)
    sanitized = re.sub(r'(?i)about:', 'blocked:', sanitized)
    
    return sanitized

@api_bp.route("/check_url", methods=["POST"])
def check_url():
    data = request.get_json()
    url = data.get("url")

    if not url:
        return jsonify({"error": "No URL provided"}), 400
         
    # URL validation
    url = url.strip()
     
     # Check URL length to prevent DoS
     if len(url) > 2048:
     if file.filename == '':
         return jsonify({'error': 'No selected file'}), 400
 
     if file and allowed_image_file(file.filename):
         timestamp = int(time.time())
         filename = f"{timestamp}_{secure_filename(file.filename)}"
         filepath = os.path.join(UPLOAD_FOLDER, filename)
         file.save(filepath)
            if os.path.exists(filepath):
                os.remove(filepath)

    else:
        return jsonify({'error': 'Invalid image file type'}), 400

            # Extract URLs
            url_pattern = r'((https?:\/\/)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/\S*)?)'
            urls = re.findall(url_pattern, text)
            urls = [match[0] for match in urls if match[0]]

            if not urls:
                return jsonify({
                     "text": text,
                     "urls": [],
                     "message": "No URL found in image."
 
     else:
         return jsonify({'error': 'Invalid image file type'}), 400
\ No newline at end of file