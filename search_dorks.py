import webbrowser
import argparse
import os

def load_dorks(file_path):
    """Read dorks from file and return list"""
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]

def get_search_url(query, engine):
    """Return search URL based on chosen engine"""
    if engine == "google":
        return f"https://www.google.com/search?q={query}"
    elif engine == "duckduckgo":
        return f"https://duckduckgo.com/?q={query}"
    elif engine == "bing":
        return f"https://www.bing.com/search?q={query}"
    elif engine == "yandex":
        return f"https://yandex.com/search/?text={query}"
    else:
        return f"https://www.google.com/search?q={query}"  # default fallback

def search_dorks(dorks, batch_size, engine):
    """Open search engine queries in batches"""
    print(f"\nLoaded {len(dorks)} queries.")
    print(f"Using search engine: {engine.capitalize()}")
    print("Press Enter to open next batch, or type q to quit.\n")

    index = 0
    while index < len(dorks):
        user_input = input(">> ")
        if user_input.lower() == "q":
            print("Exiting...")
            break

        batch = dorks[index:index+batch_size]
        for dork in batch:
            url = get_search_url(dork, engine)
            webbrowser.open_new_tab(url)

        print(f"Opened {len(batch)} queries (from {index+1} to {index+len(batch)}).")
        index += batch_size

    print("\nAll queries processed!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Dork Search Automation")
    parser.add_argument("-p", "--path", required=True, help="Path to dorks file")
    parser.add_argument("-b", "--batch", type=int, default=5, help="Number of queries to open per batch (default=5)")
    parser.add_argument("-e", "--engine", choices=["google", "duckduckgo", "bing", "yandex"], default="google",
                        help="Choose search engine: google, duckduckgo, bing, yandex (default=google)")
    args = parser.parse_args()

    if not os.path.exists(args.path):
        print(f"Error: File '{args.path}' not found!")
    else:
        dorks = load_dorks(args.path)
        search_dorks(dorks, batch_size=args.batch, engine=args.engine)
