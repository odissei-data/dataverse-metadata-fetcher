import requests
from fastapi import FastAPI, HTTPException

from schema.input import FetcherInput
from version import get_version

app = FastAPI()


@app.get("/version", tags=["Version"])
async def info():
    result = get_version()
    return {"version": result}


@app.post('/dataverse-metadata-fetcher', tags=['Dataverse metadata fetcher'])
async def dataverse_metadata_fetcher(fetcher_input: FetcherInput):
    url = f'{fetcher_input.base_url}' \
          f'/api/datasets/export?exporter={fetcher_input.metadata_format}' \
          f'&persistentId={fetcher_input.doi}'
    response = requests.get(url)
    if not response.ok:
        raise HTTPException(status_code=response.status_code,
                            detail=response.json())
    return response.json()
