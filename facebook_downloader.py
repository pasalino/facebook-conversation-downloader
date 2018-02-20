#!/usr/bin/env python
import requests
import json
import argparse


def get_conversations(pageid, accesstoken):
    conversations = []
    url = "https://graph.facebook.com/" + pageid + "/conversations?access_token=" + accesstoken
    print(f'Loading coversations from page id {pageid}', end='', flush=True)
    while True:
        r = requests.get(url)
        print('.', end='', flush=True)
        if r.status_code != 200:
            print(f'\nReceived {r.status_code} from facebook')
            print(f'Check your page id and access token')
            break

        try:
            conversation = json.loads(r.text)
            conversations.extend(conversation["data"])
            url = conversation["paging"]["next"]
        except (KeyError, ValueError):
            break

    return conversations


def save_conversation(output, conversation):
    with open(output, 'a+') as file:
        for c in conversation:
            file.write(f"{c['created_time']} # {c['from']['name']} : {c['message']} \n")
        file.write('--------------------\n')


def get_messages(conversation, accesstoken):
    url = "https://graph.facebook.com/" + conversation[
        "id"] + "/messages?fields=message,created_time,from&access_token=" + accesstoken

    messages = []
    print('.', end='', flush=True)

    while True:
        r = requests.get(url)

        if r.status_code != 200:
            break

        try:
            messagesjson = json.loads(r.text)
            messages.extend(messagesjson["data"])
            url = messagesjson["paging"]["next"]

        except (KeyError, ValueError):
            break

    return reversed(messages)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download facebook conversations')
    parser.add_argument('-a', dest='accesstoken', required=True,
                        help='Facebook access token')
    parser.add_argument('-p', dest='pageid', required=True,
                        help='Facebook page_id')
    parser.add_argument('-f', dest='output', required=True, default='output.txt',
                        help='Output filename')

    args = parser.parse_args()

    convs = get_conversations(args.pageid, args.accesstoken)
    print('\nLoading messages', end='', flush=True)
    msgs = [save_conversation(args.output, get_messages(conversation, args.accesstoken)) for conversation in convs]
    print('\nAll conversations loaded')
