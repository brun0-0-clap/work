import argparse

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--name")
    args = p.parse_args()

    if args.name is None or args.name.strip() == "":
        raise SystemExit(2)

    print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
