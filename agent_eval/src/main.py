from utils import format_status


def main() -> None:
    status = format_status("development", "ready")
    print(status)


if __name__ == "__main__":
    main()
