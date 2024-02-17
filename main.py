from datetime import datetime
import threading

from flask import Flask, request

from openai_api import ask_openai_assistant
from fb_graph_api import send_message_to_fb_messenger
import config

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return 'OK', 200


@app.route('/facebook', methods=['GET'])
def facebook_get():
    mode = request.args.get('hub.mode')
    token = request.args.get('hub.verify_token')
    challenge = request.args.get('hub.challenge')
    print(config.VERIFY_TOEKN)
    try:
        if mode == 'subscribe' and token == config.VERIFY_TOEKN:
            print('WEBHOOK_VERIFIED')
            return challenge
        else:
            return 403
    except:
        return 403


def call_ask_openai_assistant_and_send_message_to_fb_messenger(query: str, recipient_id: str) -> str:
    message_text = ask_openai_assistant(query, recipient_id)
    print(message_text)
    send_message_to_fb_messenger(recipient_id, message_text)


@app.route('/facebook', methods=['POST'])
def facebook_post():
    try:
        print('A new Facebook Messenger request...')
        body = request.get_json()
        recipient_id = body['entry'][0]['messaging'][0]['sender']['id']
        query = body['entry'][0]['messaging'][0]['message']['text']
        print(query)
        print(recipient_id)
        threading.Thread(target=call_ask_openai_assistant_and_send_message_to_fb_messenger,
                         args=(query, recipient_id)).start()
        print('Request success.')
    except:
        print('Request failed.')
        pass
    return 'OK', 200
