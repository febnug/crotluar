#!/usr/bin/env python3
import argparse
from core.engine import Engine
from utils.banner import show_banner

def main():
    show_banner()

    parser = argparse.ArgumentParser(
        description="CROT LUAR - Cyber Reconnaissance & Offensive Testing"
    )

    subparsers = parser.add_subparsers(dest="command")

    recon_parser = subparsers.add_parser("recon")
    recon_parser.add_argument("--target", required=True)

    web_parser = subparsers.add_parser("web")
    web_parser.add_argument("--url", required=True)

    internal_parser = subparsers.add_parser("internal")
    internal_parser.add_argument("--target", required=True)

    privilege_parser = subparsers.add_parser("privilege")
    privilege_parser.add_argument("--target", required=False)

    args = parser.parse_args()

    engine = Engine()

    if args.command == "recon":
        engine.run_recon(args.target)

    elif args.command == "web":
        engine.run_web(args.url)

    elif args.command == "internal":
        engine.run_internal(args.target)

    elif args.command == "privilege":
        engine.run_privilege()

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
