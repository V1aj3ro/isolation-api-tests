from pydantic import BaseModel

from tests.context.scenario import Scenario


class RequestContext(BaseModel):
    scenario: Scenario


def build_grpc_test_metadata(context: RequestContext) -> list[tuple[str, str]]:
    return [("x-test-scenario", context.scenario)]


def build_http_test_headers(context: RequestContext) -> dict[str, str]:
    return {"x-test-scenario": context.scenario}
