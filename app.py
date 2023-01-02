import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'ARMYSQUAD'

#Ex https://Greymattersbot:ghp_147bkkabcdefgh@github.com/Greymattersbot/Mogenius
os.system("git clone https://github.com/Rahan1432/GdriveSearcherBot okk && cd okk && pip3 install -U -r requirements.txt && python3 generate_drive_token.py && nohup python3 main.py &")
