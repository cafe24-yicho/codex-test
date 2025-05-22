import argparse


def greet(name: str = "World") -> None:
    """Print a greeting to the specified name."""
    print(f"Hello, {name}!")


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple greeting script")
    parser.add_argument("name", nargs="?", default="World", help="Name to greet")
    args = parser.parse_args()
    greet(args.name)


if __name__ == "__main__":
    main()
