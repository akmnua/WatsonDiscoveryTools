import csv
import json

discovery_source = DiscoveryV1(
    version='2018-08-01',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/discovery/api',
    username=USERNAME,
    password=PASSWORD)

discovery_destination = DiscoveryV1(
    version='2018-08-01',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    # url='https://gateway.watsonplatform.net/discovery/api',
    username=USERNAME,
    password=PASSWORD)

#add environment and collection id to copy from 
source_environment_id = FILL IN ENVIRONMENT_ID
source_collection_id = FILL IN COLLECTION_ID

dest_environment_id = FILL IN ENVIRONMENT_ID
dest_collection_id = FILL IN COLLECTION_ID

training_data = discovery_source.list_training_data(environment_id, source_collection_id).get_result()

for training in training_data["queries"]:
	natural_language_query = training["natural_language_query"]
	discovery_destination.add_training_data(environment_id, dest_collection_id, natural_language_query)
	