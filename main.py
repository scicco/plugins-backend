from fastapi import FastAPI
import uvicorn
from endpoints import Endpoints


GITHUB_PLUGINS_JSON_URL = "https://raw.githubusercontent.com/cheshire-cat-ai/awesome-plugins/main/plugins.json"
DEFAULT_PAGE_SIZE = 10
CACHE_DURATION_MINUTES = 1440  # Set cache duration (1 day in minutes)

app = FastAPI()

if __name__ == "__main__":
    backend = Endpoints(app=app, json=GITHUB_PLUGINS_JSON_URL, page_size=DEFAULT_PAGE_SIZE, cache_duration=CACHE_DURATION_MINUTES)
    app = backend.app

    uvicorn.run(app, host="0.0.0.0", port=8000)