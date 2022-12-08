# dataverse-metadata-fetcher
Fetches the metadata of a dataset from a dataverse instance.

## Frameworks
This project uses:
- Python 3.10
- FastAPI
- Poetry

## Setup
The default port in the example .env is 8888, change it to fit your needs.
1. `cp dot_env_example .env`
2. `make build`


## End-points
### Version
Returns the current version of the API.

### Importer
Fetches Dataverse JSON from a give Dataverse instance.
#### Parameters
- metadata_format - e.g. 'dataverse_json' - The metadata format of the retrieved metadata. (use dataverse_json for the most extensive metadata)
- doi - e.g. doi:10.5072/FK2/1YCZOL - DOI permanently identifying the dataset.
- base_url - e.g. _https://portal.odissei.nl/_ - The URL of the Dataverse instance.
- api_token - e.g. _12345678-ab12-12ab-abcd-a1b2c3d4e5g6_ - API token of the specific Dataverse. (Login to the Dataverse instance as admin and click your username in the top right to find your token.)

#### Return value
When successful, the API call will return the metadata of the dataset with the give DOI in the specified format.
The call will return an exception on a failed attempt further elaborating what went wrong.
