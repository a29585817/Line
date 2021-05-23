# flask(做程式) , django(做網頁)

from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

#權杖
#access 存取,秘密
line_bot_api = LineBotApi('RD2ntBNMfUxqk4ezdjMy7WFLWA4VxNWOS93Ag9epErl5w73kcY+trpuoRRoYH4JIMFlWdanAcPDkdDx3us5Xf/+qRmXpaHyLKjboPKX0ykQyVWdrTubgoJ0dywqBD2UnMLfptxiTJc78X7ywaXLR6gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('bc7ccb8d645ec27d66addba9aef68042')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()