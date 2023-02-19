import requests

def send_msg(text):
    token = "292473877:AAG1gIDNEHPs7nle9BB78BIcCOC6PmNz-x4"
    # Канал Sweet Home
    #chat_id = "-1001735243835"
    # Группа Sweet Home
    chat_id = "-1001684053875"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())

send_msg("Hello!")