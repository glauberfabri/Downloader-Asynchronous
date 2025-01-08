"""
Gerencia o download assíncrono dos arquivos.
"""
import aiohttp
import aiofiles
import asyncio
import os
from tqdm import tqdm

class DownloadController:
    """Realiza downloads assíncronos."""

    @staticmethod
    async def download_file(url: str, filename: str, progress_bar):
        """Baixa um arquivo de uma URL e o salva no sistema com barra de progresso."""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    response.raise_for_status()

                    total_size = int(response.headers.get("Content-Length", 0))
                    downloaded = 0

                    async with aiofiles.open(filename, "wb") as f:
                        async for chunk in response.content.iter_chunked(1024):
                            await f.write(chunk)
                            downloaded += len(chunk)
                            progress_bar.update(len(chunk))

                    print(f"\nDownload concluído: {filename}")
        except Exception as e:
            print(f"Erro ao baixar {url}: {e}")

    @staticmethod
    async def download_all(urls, interval):
        """Gerencia o download de múltiplos arquivos simultaneamente."""
        for url in urls:
            progress_bar = tqdm(total=100, desc=f"Baixando {url.filename}")
            await DownloadController.download_file(url.url, url.filename, progress_bar)
            progress_bar.close()
            await asyncio.sleep(interval)


class DownloadManager:
    """Gerencia o estado dos downloads com pausa e retomada."""
    def __init__(self):
        self.is_paused = False

    def pause(self):
        """Pausa os downloads."""
        self.is_paused = True

    def resume(self):
        """Retoma os downloads."""
        self.is_paused = False

    async def monitor_downloads(self, coro):
        """Monitora os downloads permitindo pausa e retomada."""
        while not coro.done():
            if self.is_paused:
                await asyncio.sleep(1)
            else:
                await coro