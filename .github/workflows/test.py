#!/usr/bin/env python3
import os
from enum import Enum, auto, unique
from typing import Optional, final, Callable
from os import system as sh


@final
@unique
class Level(Enum):
    DEBUG = auto()
    NOTICE = auto()
    WARNING = auto()
    ERROR = auto()

    def __str__(self) -> str:
        return self.name.lower()


def group(title: str, action: Callable[[], None]) -> None:
    print(f'::group::{title}')
    action()
    print('::endgroup::')


def annotate(
    level: Level,
    message: str,
    title: Optional[str] = None,
    file: Optional[str] = None,
    start_line: Optional[int] = None,
    end_line: Optional[int] = None,
    start_column: Optional[int] = None,
    end_column: Optional[int] = None,
) -> None:
    properties = ','.join(filter(None, [
        f'title={title}' if title else None,
        f'file={file}' if file else None,
        f'line={start_line}' if start_line else None,
        f'end_line={end_line}' if end_line else None,
        f'col={start_column}' if start_column else None,
        f'endColumn={end_column}' if end_column else None,
    ]))
    properties = f' {properties}' if properties else ''
    print(f'::{level}{properties}::{message}')


def debug(message: str) -> None:
    return annotate(Level.DEBUG, message)


def notice(
    message: str,
    title: Optional[str] = None,
    file: Optional[str] = None,
    start_line: Optional[int] = None,
    end_line: Optional[int] = None,
    start_column: Optional[int] = None,
    end_column: Optional[int] = None,
) -> None:
    return annotate(Level.NOTICE, message, title, file, start_line, end_line, start_column, end_column)


def warning(
    message: str,
    title: Optional[str] = None,
    file: Optional[str] = None,
    start_line: Optional[int] = None,
    end_line: Optional[int] = None,
    start_column: Optional[int] = None,
    end_column: Optional[int] = None,
) -> None:
    return annotate(Level.NOTICE, message, title, file, start_line, end_line, start_column, end_column)


def error(
    message: str,
    title: Optional[str] = None,
    file: Optional[str] = None,
    start_line: Optional[int] = None,
    end_line: Optional[int] = None,
    start_column: Optional[int] = None,
    end_column: Optional[int] = None,
) -> None:
    return annotate(Level.NOTICE, message, title, file, start_line, end_line, start_column, end_column)


def install_gh(version: str = '2.4.0') -> None:
    sh(f'wget https://github.com/cli/cli/releases/download/v{version}/gh_{version}_linux_amd64.tar.gz')
    sh(f'tar -xzf gh_{version}_linux_amd64.tar.gz')
    sh(f'mv gh_{version}_linux_amd64 /usr/local/bin/gh')
    os.remove(f'gh_{version}_linux_amd64.tar.gz')


def main() -> None:
    group('install gh', install_gh)


if __name__ == '__main__':
    main()
