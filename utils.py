#comment
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "agent-prg-ssweyk-6c97f2efb7af.json"
import dialogflow_v2 as dialogflow
import database

dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "agent-prg-ssweyk"

def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    print("detecting intent")
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def fetch_reply(response):
    if response.intent.display_name == 'Map':
        res_Str = "Here is your map\n\n\n"
        return res_Str
    elif response.intent.display_name == 'LineColor':
        Information = database.findInformation(response.parameters["LineColor"])
        print(Information)
        return "{}\nTotal Stations : {}\nLine Length : {}\nFirst Time : {}\nLast Time: {}\n\nStations\n{}".format(
            Information["Name"], Information["NoStations"],Information["LineLength"], Information["FirstTime"], Information["LastTime"],Information["Stations"]
            )
    elif response.intent.display_name == 'Fare':
        print(response.parameters)
        if response.parameters["SourceStation"] != "" and response.parameters["DestinationStation"] != "":
            #retrieve fare
            fare = str("10")
            MinFare = "10"
            MaxFare = "50 / 60"
            return "Fare from {} to {} is {}\nMinimum Fare : {}\nMaximum Fare : {}".format(
                response.parameters["SourceStation"], response.parameters["DestinationStation"], fare, MinFare, MaxFare
                )
        else:
            return response.fulfillment_text
    elif response.intent.display_name == 'Directory':
        rtn_Str = "Here is your directory"
        return rtn_Str
    else:
        print(response.fulfillment_text)
        return response.fulfillment_text

def reply(msg, sessionId):
    print("called fetch reply")
    response = detect_intent_from_text(msg, sessionId)
    return fetch_reply(response), response.intent.display_name