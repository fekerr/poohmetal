import toml
import zlib

def load_data(filename="honeycore_saga.toml"):
    """Load the TOML file content."""
    try:
        with open(filename, "r") as file:
            return toml.load(file)
    except Exception as e:
        print(f"Failed to load {filename}: {e}")
        exit(1)

def decompress_content(section: str, key: str, data: dict) -> str:
    """Decompress a compressed string from a given section and key."""
    try:
        compressed_str = data[section][key]
        return zlib.decompress(compressed_str.encode()).decode("utf-8")
    except Exception as e:
        return f"Error decompressing {section}.{key}: {e}"

def list_available_content(data: dict) -> None:
    """List all sections and keys in the TOML data."""
    print("Available Content:")
    for section, content in data.items():
        # Skip sections that are not dictionaries
        if isinstance(content, dict):
            print(f"\n[{section}]")
            for key in content:
                print(f"  - {key}")

def interactive_menu(data: dict) -> None:
    """Interactive CLI for listing and playing content."""
    while True:
        list_available_content(data)
        section = input("\nEnter a section name (or 'exit' to quit): ").strip()
        if section.lower() == "exit":
            break
        if section not in data or not isinstance(data[section], dict):
            print(f"Section '{section}' not found. Try again.")
            continue

        key = input(f"Enter a key from [{section}] (or 'back' to choose another section): ").strip()
        if key.lower() == "back":
            continue
        if key not in data[section]:
            print(f"Key '{key}' not found in section [{section}]. Try again.")
            continue

        content = decompress_content(section, key, data)
        print("\n--- Decompressed Content ---")
        print(content)
        print("------------------------------\n")
        input("Press Enter to continue...")

def main():
    print("Welcome to the Honeycore Saga Interactive Player!")
    data = load_data()
    interactive_menu(data)
    print("Exiting... Embrace the metal!")

if __name__ == "__main__":
    main()
