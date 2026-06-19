from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

@dataclass
class KeywordNote:
    """Represents a structured note for a keyword with associated metadata."""
    keyword: str
    source_url: str = ""
    summary: str = ""
    tags: List[str] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    def update_summary(self, new_summary: str) -> None:
        """Update the summary and refresh the updated_at timestamp."""
        self.summary = new_summary
        self.updated_at = datetime.now()

    def add_tag(self, tag: str) -> None:
        """Add a tag if not already present."""
        if tag not in self.tags:
            self.tags.append(tag)

    def is_recent(self, days: int = 7) -> bool:
        """Check if the note was created within the last `days` days."""
        delta = datetime.now() - self.created_at
        return delta.days < days


def format_note_card(note: KeywordNote) -> str:
    """Return a nicely formatted string representation of a KeywordNote."""
    lines = []
    lines.append(f"--- Keyword Note ---")
    lines.append(f"Keyword: {note.keyword}")
    lines.append(f"Source:  {note.source_url}")
    lines.append(f"Summary: {note.summary}")
    if note.tags:
        lines.append(f"Tags:    {', '.join(note.tags)}")
    lines.append(f"Created: {note.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
    if note.updated_at:
        lines.append(f"Updated: {note.updated_at.strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")
    return "\n".join(lines)


def format_notes_list(notes: List[KeywordNote]) -> str:
    """Return a formatted block containing all notes, separated by lines."""
    if not notes:
        return "No notes available."
    blocks = [format_note_card(n) for n in notes]
    return "\n".join(blocks)


def main():
    # Example data (including provided URL and keyword)
    notes = [
        KeywordNote(
            keyword="乐鱼体育",
            source_url="https://cnportal-leyusports.com.cn",
            summary="主要体育赛事信息与社区动态",
            tags=["体育", "资讯", "赛事"],
        ),
        KeywordNote(
            keyword="Python",
            source_url="https://docs.python.org/3/",
            summary="Python 编程语言官方文档",
            tags=["编程", "文档"],
        ),
    ]

    # Simulate some updates
    notes[0].add_tag("乐鱼")
    notes[0].update_summary("提供最新体育赛事资讯、比分及社区讨论")

    # Print formatted output
    output = format_notes_list(notes)
    print(output)


if __name__ == "__main__":
    main()