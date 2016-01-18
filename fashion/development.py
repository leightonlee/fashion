"""
Runs a development version of a server that serves fashion items
"""

from fashion.app import create_app

DEFAULT_PORT = 5000


def main():
    app = create_app(debug=True)
    app.run(port=DEFAULT_PORT)
