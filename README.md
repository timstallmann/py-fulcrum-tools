# py-fulcrum-tools

Tools for interacting with the fulcrum app API using python. See http://www.fulcrumapp.com/developers/api/ for more info on the Fulcrum API.

## Tools

* `deleteRecords.py` - Bulk delete records belonging to a particular changeset.

## Setup

Copy `fulcrum_config_example.py` to `fulcrum_config.py`, fill in your API token, and populate the form and creator UUID dictionaries.

## Usage

### deleteRecords

1. Run `python deleteRecords.py`. 
2. At the prompt, enter the name of a form and a user (these must match keys in `fulcrum_config.py`).
3. Copy and paste the `created` timestamp from the changeset page on `fulcrumapp.com`. *Note - this code deletes anything within +/- 60 seconds of that timestamp, so be sure to edit the accuracy in the code if you need a tighter time window*
4. Confirm deletion.