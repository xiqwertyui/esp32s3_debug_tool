import os
import subprocess


ADDR2LINE_PATH = r"xtensa-esp32s3-elf-addr2line.exe"  # Your addr2line executable file
ELF_FILE_PATH = r"firmware.elf" # You elf file, under ".pio/" folder


def run_addr2line(backtrace_addresses):
    """invoke addr2line to parse backtrace info"""
    cmd = [ADDR2LINE_PATH, "-pfiaC", "-e", ELF_FILE_PATH] + backtrace_addresses
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, check=True)
        print("\n=== Backtrace Decoded ===")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print("Failed to execute addr2line:", e)


def main():
    while True:
        user_input = input("Backtrace: ").strip()
        if user_input.lower() == "exit":
            break
        backtrace_addresses = user_input.split()
        print(backtrace_addresses)
        run_addr2line(backtrace_addresses)

if __name__ == "__main__":
    main()
