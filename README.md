# Downloader Assíncrono de Arquivos

Este projeto é um programa Python que realiza downloads de arquivos de uma lista de URLs de forma assíncrona, aproveitando a biblioteca `asyncio` para máxima performance.

---

## Funcionalidades

- **Download Assíncrono:** Baixa múltiplos arquivos simultaneamente.
- **Interatividade:** Permite ao usuário adicionar URLs e definir os nomes dos arquivos.
- **Performance Otimizada:** Usa `aiohttp` e `aiofiles` para eficiência.

---

## Estrutura do Projeto

```plaintext
downloader-assincrono/
├── models/
│   ├── url_model.py            # Representa URLs e nomes de arquivos
├── controllers/
│   ├── download_controller.py  # Gerencia downloads assíncronos
├── views/
│   ├── user_view.py            # Interação com o usuário
├── main.py                     # Ponto de entrada do programa
