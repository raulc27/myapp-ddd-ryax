import logging

from fastapi import FastAPI
import uvicorn

from myapp_ryax_ddd.container import ApplicationContainer
from myapp_ryax_ddd.infrastructure.api.setup import setup
from myapp_ryax_ddd import __version__

def init() -> FastAPI:
    container = ApplicationContainer()

    # Setup logging

    container.configuration.log_level.from_env("TODO_APP_LOG_LEVEL", "INFO")

    str_level = container.configuration.log_level()
    numeric_level = getattr(loggin, str_level.upper(), None)

    if not isinstance(numeric_level, int):
        raise ValueError("Invalid log level: %s" % str_level)
    logging.basicConfig(level=numeric_level)
    logger = loggin.getLogger(__name__)
    logger.info("Logging level is set to %s" % str_level.upper())

    # init Database
    container.configuration.storage_dir.from_env("TODOAPP_STORAGE_DIR", "/tmp/todoapp")
    Path(container.configuration.storage_dir()).mkdir(parents=True, exist_ok=True)

    # Init API and attach the container
    app = FastAPI()
    app.extra["container"] = container

    # Do setup and dependencies wiring
    setup(app, container)

    # TODO add other initialization here

    return app

def start() -> None:
    """Start application"""
    logger = logging.getLogger(__name__)
    logger.info(f"My TODO app version: {__version__}")
    app = init()
    uvicorn.run(
        app, 
        host="0.0.0.0",
        port=8080
    )

if __name__ == "__main__":
    start()