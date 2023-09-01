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

def download_video(video):
    stream = video.streams.get_highest_resolution()
    stream.download()
    print("Download completed!")

def download_audio(video):
    # Download audio stream in MP3 format
    audio_stream = video.streams.filter(only_audio=True).first()
    audio_stream.download(filename=f"{video.title}.mp3")
    print("Audio download completed!")

def search_and_download():
    query = input("Enter your search query: ")
    search_results = Search(query)
    
    for index, result in enumerate(search_results.results, start=1):
        print(f"{index}. {result.title}")
    
    choice = int(input("Select a video to download (enter the corresponding number): "))
    selected_video = search_results.results[choice - 1]
    
    video = YouTube(selected_video.watch_url)
    
    print("\nChoose an option:")
    print("1. Download Video")
    print("2. Download Audio (MP3)")
    
    download_choice = input("Enter your choice (1 or 2): ")
    
    if download_choice == '1':
        download_video(video)
    elif download_choice == '2':
        download_audio(video)
    else:
        print("Invalid choice. Please select a valid option.")

def main():
    clear_screen()
    print(logo)
    print("Welcome to Video Downloader!")
    
    while True:
        print("\nMain Menu:")
        print("1. Search and Download")
        print("2. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '1':
            search_and_download()
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == '__main__':
    main()
