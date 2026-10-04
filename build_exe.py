# app.py
import os
import sys
import webbrowser
from pathlib import Path


def resource_path(relative_path: str) -> str:
    """Return a path suitable for bundled or source execution."""
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def main() -> None:
    html_file = resource_path('index.html')

    if not os.path.exists(html_file):
        print('index.html not found')
        input('Press Enter to exit...')
        return

    webbrowser.open(f'file://{html_file}')
    print('Opening HTML app...')


if __name__ == '__main__':
    main()
