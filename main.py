"""
Ponto de entrada para o Downloader Assíncrono.
"""
from views.user_view import UserView

if __name__ == "__main__":
    print("Downloader Assíncrono de Arquivos")
    user_view = UserView()

    while True:
        print("\nMenu:")
        print("1. Adicionar URLs para download")
        print("2. Iniciar downloads")
        print("3. Controlar downloads (pausar/retomar)")
        print("4. Sair")

        choice = input("Escolha uma opção: ")
        if choice == "1":
            user_view.add_url()
        elif choice == "2":
            user_view.start_download()
        elif choice == "3":
            user_view.control_downloads()
        elif choice == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")