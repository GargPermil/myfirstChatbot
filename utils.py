#comment
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "agent-prg-ssweyk-6c97f2efb7af.json"
import dialogflow_v2 as dialogflow

dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "agent-prg-ssweyk"

def get_news(parameters):
    print(parameters)
    #client.topic = parameters.get('type')
    #client.language = parameters.get('language')
    #client.location = parameters.get('geo-country')
    print("getting news")
    return client.get_news()


def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    print("detecting intent")
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def fetch_reply(msg, sessionId):
    print("called fetch reply")
    response = detect_intent_from_text(msg, sessionId)

    if response.intent.display_name == 'Map':
        res_Str = "Here is your map\n\n\n"
        return res_Str
        #news = get_news(dict(response.parameters))
        #news_str = 'Here is your news:'
        #print("Building Response")
        #for row in news:
        #    news_str += "\n\n{}\n\n{}\n\n".format(row['title'], row['link'])
        #return news_str
    else:
        return response.fulfillment_text
