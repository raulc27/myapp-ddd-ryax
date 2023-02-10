from dataclasses import dataclass
from typing import Optional

from myapp_ryax_ddd.todo import TodoEntry
from myapp_ryax_ddd.todo_entry_repository import ITodoEntryRepository

@dataclass
class TodoService:
    todo_repository: ITodoEntryRepository

    def add_entry(self, content: str) -> str:
        entry = TodoEntry.create_from_content(content)
        self.todo_repository.add(entry)
        return entry.id

    def add_tag(self, entry_id: str, tag: str) -> None:
        entry = self.todo_repository.get(entry_id)
        entry.set_tag(tag)

    def get_all(self, search: Optional[str] = None) -> list[TodoEntry]:
        return self.todo_repository.get_all(search)


# With this test, we find out that the repository does not open the files in "write in bytes" mode 
# but in "read in utf-8" mode which is the default in Python. So I've added the mode="wb" in my add function and 
# the mode="rb" in my get function
