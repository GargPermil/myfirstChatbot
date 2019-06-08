#comment
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "agent-prg-ssweyk-6c97f2efb7af.json"
import dialogflow_v2 as dialogflow

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
        Stations = {
            "Red Line": "Shaheed Sthal (New Bus Adda), Hindon River, Arthala, Mohan Nagar, Shyam Park, Major Mohit Sharma, Rajender Nagar, Raj Bagh, Shahid Nagar, Dilshad Garden, Jhilmil, Mansarovar Park, Shahdara, Welcome, Seelampur, Shastri Park, Kashmere Gate, Tis Hazari, Pul Bangash, Pratap Nagar, Shastri Nagar, Inderlok, Kanhiya Nagar, Keshav Puram, Netaji Subhash Place, Kohat Enclave, Pitam Pura, Rohini East, Rohini West, Rithala",
            "Yellow Line" : "Siraspur, Samaypur Badli, Rohini Sector 18/19, Haiderpur, Jahangirpuri, Adarsh Nagar, Azadpur, Model Town, GTB Nagar, Vishwa Vidyalaya, Vidhan Sabha, Civil Lines, Kashmere Gate, Chandni Chowk, Chawri Bazar, New Delhi, Rajiv Chowk, Patel Chowk, Central Secretariat, Udyog Bhawan, Lok Kalyan Marg, Jor Bagh INA, AIIMS, Green Park, Hauz Khas, Malviya Nagar, Saket, Qutab Minar, Chhatarpur, Sultanpur, Ghitorni, Arjan Garh, Guru Dronacharya, Sikandarpur, MG Road, IFFCO Chowk, HUDA City Centre",
            "Blue Line" : "Dwarka Sector 21, Dwarka Sector 8, Dwarka Sector 9, Dwarka Sector 10, Dwarka Sector 11, Dwarka Sector 12, Dwarka Sector 13, Dwarka Sector 14, Dwarka, Dwarka Mor, Nawada Uttam Nagar West, Uttam Nagar East, Janakpuri West, Janakpuri East, Tilak Nagar, Subhash Nagar, Tagore Garden, Rajouri Garden, Ramesh Nagar, Moti Nagar, Kirti Nagar, Shadipur, Patel Nagar, Rajendra Place, Karol Bagh, Jhandewalan, Ramakrishna, Ashram Marg, Rajiv Chowk, Barakhamba Road, Mandi House, Pragati Maidan, Indraprastha, Yamuna Bank, Akshardham, Mayur Vihar-I, Mayur Vihar Extension, New Ashok Nagar, Noida Sector 15, Noida Sector 16, Noida Sector 18, Botanical Garden, Golf Course, Noida City Centre, Noida Sector 34, Noida Sector 52, Noida Sector 61, Noida Sector 59, Noida Sector 62, Noida Electronic City",
            "Green Line" : "Inderlok, Ashok Park Main, Punjabi Bagh East, Shivaji Park, Madipur, Paschim Vihar East, Paschim Vihar West, Peera Garhi, Udyog Nagar, Surajmal Stadium, Nangloi, Nangloi Railway Station, Rajdhani Park, Mundka, Mundka Industrial, Area Ghevra Metro Station, Tikri Kalan, Tikri Border, Pandit Shri Ram Sharma, Bahadurgarh City, Brigadier Hoshiyar Singh",
            "Violet Line" : "Kashmere Gate, Lal Qila, Jama Masjid, Delhi Gate, ITO, Mandi House, Janpath, Central Secretariat, Khan Market, Jawaharlal Nehru Stadium, Jangpura, Lajpat Nagar, Moolchand, Kailash Colony, Nehru Place, Kalkaji Mandir, Govind Puri, Harkesh Nagar Okhla, Jasola Apollo, Sarita Vihar, Mohan Estate, Tughlakabad Station, Badarpur Border, Sarai, NHPC Chowk,- Mewala Maharajpur, Sector-28, Badkhal Mor, Old Faridabad, Neelam Chowk Ajronda, Bata Chowk, Escorts Mujesar, Sant Surdas (Sihi), Raja Nahar Singh",
            "Airport Express" : "New Delhi, Shivaji Stadium, Dhaula Kuan, Delhi, Aerocity Airport, Dwarka, Sector 21",
            "Pink Line" : "Majlis Park, Azadpur, Shalimar Bagh, Netaji Subhash Place, Shakurpur, Punjabi Bagh West, ESI Hospital, Rajouri Garden, Mayapuri, Naraina Vihar, Delhi Cantt, South Campus, Sir Vishveshwaraiah Moti Bagh, Bhikaji Cama Place, Sarojini Nagar, INA, South Extension, Lajpat Nagar, Vinoba Puri, Ashram, Hazrat Nizamuddin, Mayur Vihar, Mayur Vihar Pocket I, Trilokpuri-Sanjay Lake, Vinod Nagar, East-Mayur Vihar-II, Mandawali-West Vinod Nagar, IP Extension, Anand Vihar, Karkarduma, Krishna Nagar, East Azad Nagar, Welcome, Jaffrabad, Maujpur, Gokulpuri Johri Enclave, Shiv Vihar",
            "Magenta line" : "Janakpuri West, Dabri Mor, Dashrath Puri, Palam, Sadar Bazaar, Cantonment Terminal 1-IGI Airport, Shankar Vihar, Vasant Vihar, Munirka, R.K Puram, IIT Delhi, Hauz Khas, Panchsheel Park, Chirag Delhi, Greater Kailash, Nehru Enclave, Kalkaji Mandir, Okhla NSIC, Sukhdev Vihar, Jamia Millia Islamia, Okhla Vihar, Jasola Vihar Shaleen Bagh, Kalindi Kunj, Okhla Bird Sanctuary, Botanical Garden"
        }
        return Stations[response.parameters["LineColor"]]
    elif response.intent.display_name == 'Fare':
        print(response.parameters)
        return "Fare from {} to {} is 10\nMinimum Fare : 10\nMaximum Fare : 50 / 60".format(response.parameters["SourceStation"], response.parameters["DestinationStation"])
    else:
        print(response.fulfillment_text)
        return response.fulfillment_text

def reply(msg, sessionId):
    print("called fetch reply")
    response = detect_intent_from_text(msg, sessionId)
    return fetch_reply(response), response.intent.display_name