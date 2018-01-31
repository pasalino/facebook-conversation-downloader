# Facebook Conversations Downloader
This script is designed to create a file that contains a Page's Facebook conversations.
The script extract all facebook page's conversations.
This script use a graph API and create a single file with all conversations.


## Licensing
This script uses the [Apache License, version 2.0](https://www.apache.org/licenses/LICENSE-2.0) . Please see the library's individual files for more information.

## Reporting Issues
If you have bugs or other issues specifically pertaining to this script, file them [here](https://github.com/pasalino/facebook-conversation-downloader/issues) . 
Bugs with the Graph API should be filed on Facebook's [bugtracker](https://developers.facebook.com/bugs/) .

## Build & Install
After install python on your laptop, copy a script in any folder and launch it

### Requirements

Use `pip install -r requirements.txt` for install dependences 

## Using the script

Launch with:

    python getConv.py [page-id] [access-token]

Parameter | Description
--- | ---
**page-id** | Facebook page id
**access-token** | Access token with `pages_messaging` grant enabled

Use [Tool Graph API Explorer](https://developers.facebook.com/tools/explorer/) for get page-id and access-token

Use [this](https://developers.facebook.com/docs/graph-api/overview) link for understand how get facebook access token.

## Copyright and License

©2018 de Simone Pasqualino (pasalino). All Rights Reserved. 

## Contributor

* (Federico Blancato)[https://github.com/ksnll]