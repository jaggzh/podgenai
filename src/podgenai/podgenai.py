import datetime
from pathlib import Path
from typing import Optional

from podgenai.config import REPO_PATH
from podgenai.subtopics import get_subtopics
from podgenai.topic import is_topic_valid
from podgenai.util.openai import is_openai_key_available


def generate_podcast(topic: str, *, output_path: Optional[Path] = None) -> Path:
    """Return the output path after generating and writing a podcast to file for the given topic."""
    assert is_openai_key_available()
    assert is_topic_valid(topic)
    get_subtopics(topic)

    if output_path is None:
        now = datetime.datetime.now().isoformat(timespec='seconds')
        output_path = REPO_PATH / f'{now} {topic}.mp3'

    return output_path