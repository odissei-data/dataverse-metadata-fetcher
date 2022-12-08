from pydantic import BaseModel, Field


class DataverseInformation(BaseModel):
    base_url: str = Field(example="https://portal.odissei.nl/")
    api_token: str = Field(example="12345678-ab12-12ab-abcd-a1b2c3d4e5g6")


class FetcherInput(BaseModel):
    pid: str = Field(example="doi:10.5072/FK2/1YCZOL")
    metadata_format: str = Field(example="dataverse_json")
    dataverse_information: DataverseInformation
