#!/usr/bin/env python

import sys
import requests
import json
import datetime

pageid= sys.argv[1]
accesstoken = sys.argv[2]

conversations = []

loop = True
url = "https://graph.facebook.com/" + pageid + "/conversations?access_token=" + accesstoken


while loop:
    #recupera le conversazioni
    r = requests.get(url)
    print ("Connessione per conversazione")
    print (r.status_code)
    #se lo stato non è 200
    if(r.status_code != 200):
        loop= False
        break
    #recupera i dati di conversazione
    conversation = json.loads(r.text)
    conversations.extend(conversation["data"])
    #se non ci sono più conversazioni esce dal ciclo
    if (len(conversation["data"])==0):
       loop = False
       break
    #se non c'è il link alla pagina successiva esce dal ciclo oppure recupera il link della pagina successiva
    if ("paging" in conversation.keys()):
        url = conversation["paging"]["next"]
    else:
        loop = False
        break

    print ("Conversazioni :" + str(len(conversation["data"])))
    print("Conversazioni totali :" + str(len(conversations)))



#recupero messaggi
convmessage = []

out_file = open("conversation.txt","w")
out_file.write("Export del " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n\n")

tot = str(len(conversations))
print("Totale conversations:" + tot)

j = 0
for c in conversations:
    #Cicla le conversazioni
    j+=1
    print ("Conv n:" + str(j) + " di " + tot)
    print (c["id"])

    # recupera la conversazione
    url = "https://graph.facebook.com/" + c["id"] + "/messages?fields=message,created_time,from&access_token=" + accesstoken
    #recupera i messaggi per ogni conversazione
    messages = []
    loop = True
    while loop:
        r = requests.get(url)
        print("Connessione per messaggi conversazione")
        print(r.status_code)
        # se lo stato non è 200
        if (r.status_code != 200):
            loop = False
            break
        # recupera i dati di conversazione
        messagesjson = json.loads(r.text)
        messages.extend(messagesjson["data"])
        # se non ci sono più conversazioni esce dal ciclo
        if (len(messagesjson["data"]) == 0):
            loop = False
            break
        # se non c'è il link alla pagina successiva esce dal ciclo oppure recupera il link della pagina successiva
        if ("paging" in messagesjson.keys()):
            url = messagesjson["paging"]["next"]
        else:
            loop = False
            break

        convmessage.append(reversed(messages))

print ("Conversazioni Totali" + str(len(convmessage)))
convmessage = reversed(convmessage)
#
#    out_file.write("Data: " + c["updated_time"] + " id: " + c["id"] + "\n")
for c in convmessage:
    out_file.write("--------------------------------------------------------\n")
    for dd in c:
        out_file.write(dd["created_time"] + "# " + dd["from"]["name"] + ":" + dd["message"] + "\n")
    out_file.write("\n")



out_file.close()

print("End")