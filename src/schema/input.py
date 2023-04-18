from pydantic import BaseModel, Field


class FetcherInput(BaseModel):
    doi: str = Field(example="doi:10.5072/FK2/1YCZOL")
    metadata_format: str = Field(example="dataverse_json")
    base_url: str = Field(example="https://portal.staging.odissei.nl")
