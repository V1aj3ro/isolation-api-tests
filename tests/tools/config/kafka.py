from pydantic import BaseModel, IPvAnyAddress


class KafkaClientTestConfig(BaseModel):
    port: int = 9092
    address: IPvAnyAddress

    @property
    def bootstrap_servers(self) -> str:
        return f"{self.address}:{self.port}"
