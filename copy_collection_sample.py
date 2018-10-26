import csv
import json
import time
from watson_developer_cloud import DiscoveryV1

# This is a sample script for copying a collection with training data to a new collection in the 
# same environment. This can be used for up to 1000 documents. 

discovery = DiscoveryV1(
    version='2018-08-01',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/discovery/api',
    username=USERNAME,
    password=PASSWORD)

#add environment and collection id to copy from 
environment_id = FILL IN ENVIRONMENT_ID
source_collection_id = FILL IN COLLECTION_ID

#get source collection details
response = discovery.get_collection(environment_id, source_collection_id).get_result()
collection_name = response["name"]
configuration_id = response["configuration_id"]

#create new copy collection
destination_collection_name= collection_name + "_copy"
create_response = discovery.create_collection(environment_id, name=destination_collection_name, configuration_id=configuration_id).get_result()
destination_collection_id = create_response["collection_id"]

#get documents from the source collection 
query_results = discovery.query(
    environment_id,
    source_collection_id,
    query="",
    count=1000).get_result()

for result in query_results["results"]:
	document_id = result["id"]
	with open("./temp/temp.json", "w+") as out_file:
		json.dump(result, out_file)
	with open("./temp/temp.json") as file:
		add_doc = discovery.update_document(environment_id, destination_collection_id, document_id=document_id, file=file).get_result()
	time.sleep(0.5) #sleep between adds to avoid rate limits

#get training data from source
training_data = discovery.list_training_data(environment_id, source_collection_id).get_result()

for training in training_data["queries"]:
	example = training["examples"]
	natural_language_query = training["natural_language_query"]
	filter = training["filter"]
	discovery.add_training_data(environment_id, destination_collection_id, natural_language_query, filter, example)
	time.sleep(0.1)
