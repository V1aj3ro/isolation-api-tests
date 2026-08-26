import uvicorn
from fastapi import FastAPI

from tests.config import test_settings
from tests.mock.http.api.accounts import accounts_mock_router
from tests.mock.http.api.cards import cards_mock_router
from tests.mock.http.api.users import users_mock_router

app = FastAPI(title="mock-service")

app.include_router(users_mock_router)
app.include_router(cards_mock_router)
app.include_router(accounts_mock_router)

if __name__ == "__main__":
    uvicorn.run(
        app="tests.mock.http.server:app",
        host=str(test_settings.mock_http_server.address),
        port=test_settings.mock_http_server.port,
        workers=3
    )
