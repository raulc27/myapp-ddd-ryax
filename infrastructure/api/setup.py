from fastapi import FastAPI

from myapp_ryax_ddd.container import ApplicationContainer
from myapp_ryax_ddd.infrasctructure.api import todo_controller

def setup(app: FastAPI, container: ApplicationContainer) -> None:

    # Add other controllers here
    app.include_router(todo_controller.router)

    # Inject dependencies

    container.wire(
        modues=[
            todo_controller
        ]
    )