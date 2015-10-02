import requests
import json
import time
import calendar
from fulcrum_config import *


def getRecords(formId, userId, timestamp):
    params = {
        'form_id': formId,
        'per_page': 10,
        'created_by': userId,
        'created_before': timestamp + 60,
        'created_since': timestamp - 60
    }
    headers = {'X-ApiToken': apiToken}
    response = requests.get(urlBase + 'records.json', headers=headers, params=params)
    responseDecoded = json.loads(response.text)
    if 'records' in responseDecoded:
        return responseDecoded
    else:
        return False


def deleteRecord(recordId):
    headers = {'X-ApiToken': apiToken}
    response = requests.delete(urlBase + 'records/' + recordId + '.json', headers=headers)
    if (response.ok):
        print "Deleted record: " + recordId
        return True
    else:
        print "Error on record: " + recordId
        return False

formName = raw_input("Enter name of form from which records should be deleted: ")
if formName not in formIds:
    print "Unknown form name"
    exit(0)

userName = raw_input("Enter name of user for which records should be deleted: ")
if userName not in creatorIds:
    print "Unknown user name"
    exit(0)

timestamp = raw_input("Enter timestamp to be deleted, e.g. '2015-09-29 21:54:31 UTC': ")

# Get full list of records by timestamp.
epochTime = (int)(calendar.timegm(time.strptime(timestamp, "%Y-%m-%d %H:%M:%S %Z")))

records = getRecords(formIds[formName], creatorIds[userName], epochTime)
if not records:
    print "Error fetching records."
    exit(0)

if records['total_count'] == 0:
    print "No records found matching that timestamp."
    exit(0)

doDelete = raw_input("Preparing to delete " + str(records['total_count']) + " records. Confirm? (type 'DELETE' to continue): ")
records = records['records']

if doDelete == 'DELETE':
    while len(records) > 0:
        for record in records:
            if not deleteRecord(record['id']):
                exit(0)
        records = getRecords(formIds[formName], creatorIds[userName], epochTime)['records']
else:
    exit(0)
    
exit(1)
