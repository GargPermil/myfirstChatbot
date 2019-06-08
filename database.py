from pymongo import MongoClient
import datetime

client = MongoClient("mongodb+srv://bot:Nagarro190607@cluster0-olpok.mongodb.net/test?retryWrites=true&w=majority")
db = client.get_database("Preferences")
information_records = db.get_collection("Information")
records = db.get_collection("Preferences")

def count():
	print(records.count_documents({}))
	return "The count of records " + str(records.count_documents({}))

def findInformation(Line):
	return information_records.find_one({"Name" : Line})

def insertData(Name, MobNo):
	count = records.insert_one({
		"Name" : "Permil Garg",
		"MobileNo" : "+919953905068",
		#"Source" : "Rithala",
		#"Destination" : "MG Road",
		#"Timing" : "Peak",
		"Timestamp" : str(datetime.datetime.utcnow())
		})
	print(count.inserted_id)
	return str(count.inserted_id)

def updateSource(Source):
	count = records.update_one({
		"MobileNo" : "+919953905068"
	} , {
		"$set" : {
			"Source" : Source,
			"Destination" : "MG Road-1",
			"Timing" : "Normal",
			"UpdateTimestamp" : str(datetime.datetime.utcnow())
	}})
	print(count.modified_count)
	return str(count.modified_count)

def updateDest(Dest):
	count = records.update_one({
		"MobileNo" : "+919953905068"
	} , {
		"$set" : {
			"Destination" : Dest,
			"UpdateTimestamp" : str(datetime.datetime.utcnow())
	}})
	print(count.modified_count)
	return str(count.modified_count)

def updateTiming(Timing):
	count = records.update_one({
		"MobileNo" : "+919953905068"
	} , {
		"$set" : {
			"Timing" : Timing,
			"UpdateTimestamp" : str(datetime.datetime.utcnow())
	}})
	print(count.modified_count)
	return str(count.modified_count)
