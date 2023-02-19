import requests

def send_telegram(text: str):
    token = "292473877:AAG1gIDNEHPs7nle9BB78BIcCOC6PmNz-x4"
    url = "https://api.telegram.org/bot"
    channel_id = "-1001684053875"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })

    if r.status_code != 200:
        raise Exception("post_text error")

if __name__ == '__main__':
  send_telegram("hello world!")
