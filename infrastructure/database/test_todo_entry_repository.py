from tempfile import TemporaryDirectory

import pytest as pytest

from myapp_ryax_ddd.container import ApplicationContainer
from myapp_ryax_ddd.todo import TodoEntry
from myapp_ryax_ddd.infrastructure.database.todo_entry_repository import TodoEntryPickleRepository

@pytest.fixture()
def repository():
    with TemporaryDirectory() as tmp_dir:
        container = ApplicationContainer()

        container.configuration.storage_dir.from_value(tmp_dir)
        yield container.todo_entry_repository()

def test_add_and_get(repository: TodoEntryPickleRepository):
    entry = TodoEntry.create_from_content("test")
    repository.add(entry)
    assert entry == repository.get(entry.id)