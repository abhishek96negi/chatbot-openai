from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv()

# Create a dictionary of environment variables
env_var = {key: value for key, value in os.environ.items()}
