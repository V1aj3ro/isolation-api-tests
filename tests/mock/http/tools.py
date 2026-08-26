from typing import Annotated

from fastapi import Header, HTTPException, status

from tests.context.scenario import Scenario


def get_scenario_http(
    scenario: Annotated[Scenario | None, Header(alias="X-Test-Scenario")] = None
) -> Scenario:
    if not scenario:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="X-Test-Scenario header is required",
        )

    return scenario
