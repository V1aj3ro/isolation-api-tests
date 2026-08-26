from pydantic import BaseModel, IPvAnyAddress


class GRPCServerTestConfig(BaseModel):
    port: int
    address: IPvAnyAddress

    @property
    def url(self):
        return f"{self.address}:{self.port}"


class GRPCClientTestConfig(BaseModel):
    port: int
    address: IPvAnyAddress

    @property
    def url(self):
        return f"{self.address}:{self.port}"


