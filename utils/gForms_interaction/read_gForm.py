import os
from googleapiclient import discovery
from httplib2 import Http
from oauth2client import client, file, tools
from typing import Dict, Any

from dotenv import load_dotenv
load_dotenv()

SCOPES = "https://www.googleapis.com/auth/forms.responses.readonly"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage("token.json")
creds = None
if not creds or creds.invalid:
  flow = client.flow_from_clientsecrets("utils/gForms_interaction/client_secrets.json", SCOPES)
  creds = tools.run_flow(flow, store)
service = discovery.build(
    "forms",
    "v1",
    http=creds.authorize(Http()),
    discoveryServiceUrl=DISCOVERY_DOC,
    static_discovery=False,
)


def get_form_responses() -> Dict[str, Any]:
    print("getting form responses...")
    form_id = os.getenv('GOOGLE_FORM_ID')
    result = service.forms().responses().list(formId=form_id).execute()
    print(result)
    return result