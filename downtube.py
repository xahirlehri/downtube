from pytube import YouTube, Search
import os

logo = """
\033[91m██████╗  ██████╗ ██╗    ██╗███╗   ██╗████████╗██╗   ██╗██████╗ ███████╗
██╔══██╗██╔═══██╗██║    ██║████╗  ██║╚══██╔══╝██║   ██║██╔══██╗██╔════╝
██║  ██║██║   ██║██║ █╗ ██║██╔██╗ ██║   ██║   ██║   ██║██████╔╝█████╗  
██║  ██║██║   ██║██║███╗██║██║╚██╗██║   ██║   ██║   ██║██╔══██╗██╔══╝  
██████╔╝╚██████╔╝╚███╔███╔╝██║ ╚████║   ██║   ╚██████╔╝██████╔╝███████╗
╚═════╝  ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝\033[0m
                                          \033[91mCreated by Zahir Lehri\033[0m
"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def search_and_download_video():
    query = input("Enter your search query: ")
    search_results = Search(query)
    
    for index, result in enumerate(search_results.results, start=1):
        print(f"{index}. {result.title}")
    
    choice = int(input("Select a video to download (enter the corresponding number): "))
    selected_video = search_results.results[choice - 1]
    
    video = YouTube(selected_video.watch_url)
    stream = video.streams.get_highest_resolution()
    stream.download()
    
    print("Download completed!")

def main():
    clear_screen()
    print(logo)
    print("Welcome to Video Downloader!")
    while True:
        print("\nMain Menu:")
        print("1. Search and Download Video")
        print("2. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            search_and_download_video()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
