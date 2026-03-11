#!/usr/bin/env python3

import clisky.model as model
import os
import click
import platform
import json
from getpass import getpass

CONFIG_FILE = os.path.expanduser("~/.clisky_config.json")


def execute_command(command):
    """Execute a command in the system shell"""
    print(f"\n🚀 Executing:\n{command}\n")
    os.system(command)


def get_linux_distro():
    """Detect Linux distribution"""
    try:
        distro = platform.freedesktop_os_release()["NAME"]
        if not distro:
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("NAME="):
                        distro = line.strip().split("=")[1].replace('"', "")
                        break
        return distro
    except Exception:
        return "Unknown"


def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {}


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)


def ensure_api_key(config):
    api_key = config.get("groq_api_key")

    if not api_key:
        print("\n🔑 Groq API key not found.")
        print("Get it from: https://console.groq.com/\n")

        api_key = getpass("Paste your Groq API key: ").strip()

        config["groq_api_key"] = api_key
        save_config(config)

        print("✅ API key saved.\n")

    os.environ["OPENAI_API_KEY"] = api_key


def load_or_set_distro(config):
    distro = config.get("distro")

    if not distro:
        distro = get_linux_distro()
        config["distro"] = distro
        save_config(config)

    return distro


@click.command()
@click.argument("prompt", type=str)
def ai_cli(prompt):
    """AI CLI that recommends and optionally runs commands"""

    config = load_config()

    ensure_api_key(config)

    distro = load_or_set_distro(config)

    suggestion = model.cli_recommend(prompt + " for " + distro)

    print("\n💡 Suggested Command:\n")
    print(suggestion)
    
    dangerous = ["rm -rf /", "mkfs", "dd ", "shutdown", "reboot"]

    if any(d in suggestion for d in dangerous):
        print("⚠️ Potentially dangerous command blocked.")
        return

    run = input("\nRun this command? [y/N]: ").strip().lower()

    if run == "y":
        execute_command(suggestion)
    else:
        print("Command not executed.")


if __name__ == "__main__":
    ai_cli()