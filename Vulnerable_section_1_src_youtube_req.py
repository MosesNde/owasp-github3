 "GLOBAL"
 
 
def last_exe_date(logging_path: str = '../log/last_exe.log'):
     """Extract last execution datetime from a log file (supposing first line is containing the right datetime).
    :param logging_path: .log file path
     :return date: last execution date.
     """
    with open(logging_path, 'r', encoding='utf8') as log_file:
         first_log = log_file.readlines()[0]  # Get first log
 
     date_str = re.search(r'(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})\+(\d{4})', first_log).group()  # Extract date