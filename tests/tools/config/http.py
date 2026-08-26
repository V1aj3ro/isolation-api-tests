from pydantic import BaseModel, HttpUrl


class HTTPClientTestConfig(BaseModel):
    url: HttpUrl
    timeout: float = 120.0
