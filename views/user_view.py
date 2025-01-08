"""
Interage com o usuário e exibe o progresso.
"""
from models.url_model import URL
from controllers.download_controller import DownloadController, DownloadManager
import asyncio

class UserView:
    """Gerencia a interação com o usuário."""
    def __init__(self):
        self.urls = []
        self.manager = DownloadManager()

    def add_url(self):
        """Solicita ao usuário URLs e nomes de arquivos para download."""
        while True:
            url = input("Digite a URL do arquivo (ou 'done' para finalizar): ")
            if url.lower() == "done":
                break
            filename = input("Digite o nome do arquivo para salvar: ")
            self.urls.append(URL(url, filename))

    def start_download(self):
        """Inicia o processo de download."""
        interval = float(input("Digite o intervalo entre downloads (em segundos): "))
        print("Iniciando os downloads...")

        coro = asyncio.create_task(DownloadController.download_all(self.urls, interval))
        asyncio.run(self.manager.monitor_downloads(coro))

    def control_downloads(self):
        """Permite pausar ou retomar os downloads."""
        while True:
            action = input("Digite 'pause' para pausar, 'resume' para retomar ou 'done' para encerrar o controle: ")
            if action.lower() == "pause":
                self.manager.pause()
                print("Downloads pausados.")
            elif action.lower() == "resume":
                self.manager.resume()
                print("Downloads retomados.")
            elif action.lower() == "done":
                print("Encerrando controle de downloads.")
                break
            else:
                print("Comando inválido. Tente novamente.")