"""
Define a classe para armazenar URLs e metadados.
"""
class URL:
    """Representa uma URL a ser baixada."""
    def __init__(self, url: str, filename: str):
        self.url = url
        self.filename = filename
