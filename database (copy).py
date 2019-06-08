from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://bot:Nagarro190607@cluster0-olpok.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database("Preferences")
records = db.get_collection("Information")
count = records.insert_one({
                "Name" : "Blue Line",
                "LastTime" : "11.40 PM",
                "FirstTime" : "5.30 AM",
                "LineLength" : "70 Kms",
                "NoStations" : str(40),
                "Stations" : "Dwarka Sector 21, Dwarka Sector 8, Dwarka Sector 9, Dwarka Sector 10, Dwarka Sector 11, Dwarka Sector 12, Dwarka Sector 13, Dwarka Sector 14, Dwarka, Dwarka Mor, Nawada Uttam Nagar West, Uttam Nagar East, Janakpuri West, Janakpuri East, Tilak Nagar, Subhash Nagar, Tagore Garden, Rajouri Garden, Ramesh Nagar, Moti Nagar, Kirti Nagar, Shadipur, Patel Nagar, Rajendra Place, Karol Bagh, Jhandewalan, Ramakrishna, Ashram Marg, Rajiv Chowk, Barakhamba Road, Mandi House, Pragati Maidan, Indraprastha, Yamuna Bank, Akshardham, Mayur Vihar-I, Mayur Vihar Extension, New Ashok Nagar, Noida Sector 15, Noida Sector 16, Noida Sector 18, Botanical Garden, Golf Course, Noida City Centre, Noida Sector 34, Noida Sector 52, Noida Sector 61, Noida Sector 59, Noida Sector 62, Noida Electronic City"})
print(count.inserted_id)
count = records.insert_one({
                "Name" : "Green Line",
                "LastTime" : "11.40 PM",
                "FirstTime" : "5.30 AM",
                "LineLength" : "70 Kms",
                "NoStations" : str(40),
                "Stations" : "Inderlok, Ashok Park Main, Punjabi Bagh East, Shivaji Park, Madipur, Paschim Vihar East, Paschim Vihar West, Peera Garhi, Udyog Nagar, Surajmal Stadium, Nangloi, Nangloi Railway Station, Rajdhani Park, Mundka, Mundka Industrial, Area Ghevra Metro Station, Tikri Kalan, Tikri Border, Pandit Shri Ram Sharma, Bahadurgarh City, Brigadier Hoshiyar Singh"})
print(count.inserted_id)

count = records.insert_one({
                "Name" : "Violet Line",
                "LastTime" : "11.40 PM",
                "FirstTime" : "5.30 AM",
                "LineLength" : "70 Kms",
                "NoStations" : str(40),
                "Stations" : "Kashmere Gate, Lal Qila, Jama Masjid, Delhi Gate, ITO, Mandi House, Janpath, Central Secretariat, Khan Market, Jawaharlal Nehru Stadium, Jangpura, Lajpat Nagar, Moolchand, Kailash Colony, Nehru Place, Kalkaji Mandir, Govind Puri, Harkesh Nagar Okhla, Jasola Apollo, Sarita Vihar, Mohan Estate, Tughlakabad Station, Badarpur Border, Sarai, NHPC Chowk,- Mewala Maharajpur, Sector-28, Badkhal Mor, Old Faridabad, Neelam Chowk Ajronda, Bata Chowk, Escorts Mujesar, Sant Surdas (Sihi), Raja Nahar Singh"})
print(count.inserted_id)

count = records.insert_one({
                "Name" : "Airport Line",
                "LastTime" : "11.40 PM",
                "FirstTime" : "5.30 AM",
                "LineLength" : "70 Kms",
                "NoStations" : str(40),
                "Stations" : "New Delhi, Shivaji Stadium, Dhaula Kuan, Delhi, Aerocity Airport, Dwarka, Sector 21"})
print(count.inserted_id)

count = records.insert_one({
                "Name" : "Pink Line",
                "LastTime" : "11.40 PM",
                "FirstTime" : "5.30 AM",
                "LineLength" : "70 Kms",
                "NoStations" : str(40),
                "Stations" : "Majlis Park, Azadpur, Shalimar Bagh, Netaji Subhash Place, Shakurpur, Punjabi Bagh West, ESI Hospital, Rajouri Garden, Mayapuri, Naraina Vihar, Delhi Cantt, South Campus, Sir Vishveshwaraiah Moti Bagh, Bhikaji Cama Place, Sarojini Nagar, INA, South Extension, Lajpat Nagar, Vinoba Puri, Ashram, Hazrat Nizamuddin, Mayur Vihar, Mayur Vihar Pocket I, Trilokpuri-Sanjay Lake, Vinod Nagar, East-Mayur Vihar-II, Mandawali-West Vinod Nagar, IP Extension, Anand Vihar, Karkarduma, Krishna Nagar, East Azad Nagar, Welcome, Jaffrabad, Maujpur, Gokulpuri Johri Enclave, Shiv Vihar"})
print(count.inserted_id)

count = records.insert_one({
                "Name" : "Magenta Line",
                "LastTime" : "11.40 PM",
                "FirstTime" : "5.30 AM",
                "LineLength" : "70 Kms",
                "NoStations" : str(40),
                "Stations" : "Janakpuri West, Dabri Mor, Dashrath Puri, Palam, Sadar Bazaar, Cantonment Terminal 1-IGI Airport, Shankar Vihar, Vasant Vihar, Munirka, R.K Puram, IIT Delhi, Hauz Khas, Panchsheel Park, Chirag Delhi, Greater Kailash, Nehru Enclave, Kalkaji Mandir, Okhla NSIC, Sukhdev Vihar, Jamia Millia Islamia, Okhla Vihar, Jasola Vihar Shaleen Bagh, Kalindi Kunj, Okhla Bird Sanctuary, Botanical Garden"})
print(count.inserted_id)

