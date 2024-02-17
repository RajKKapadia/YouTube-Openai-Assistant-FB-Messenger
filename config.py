import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
ASSISTANT_ID = os.getenv('ASSISTANT_ID')

FB_PAGE_ACCESS_TOKEN = os.getenv('FB_PAGE_ACCESS_TOKEN')
VERIFY_TOEKN = os.getenv('VERIFY_TOEKN')

ERROR_MESSAGE = 'We are facing an issue at this momemnt, please try after sometime.'

MAPPINGS_DATA = {"mappings": {}}
