import toml

try:
    data = toml.load("honeycore_saga.toml")
    print("TOML file is valid!")
except toml.decoder.TomlDecodeError as e:
    print(f"TOML error: {e}")
