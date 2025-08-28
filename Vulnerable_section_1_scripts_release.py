 def run_command(command, capture_output=False):
     """Run a shell command and return the result."""
     print(f"Running: {command}")
    result = subprocess.run(command, shell=True, capture_output=capture_output, text=True)
     if result.returncode != 0:
         print(f"Command failed with exit code {result.returncode}")
         if capture_output: