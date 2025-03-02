# ESP32-S3 Debugging Helper

## Overview
This Python script helps analyze ESP32-S3 backtrace logs for debugging purposes in **PlatformIO**. It decodes backtrace addresses into human-readable function names and source file locations.

## Installation & Setup
### 1. Locate Required Files
Before running the script, find the necessary files on your system:

- **xtensa-esp32s3-elf-addr2line.exe**  
  - Located in:  
    ```
    C:\Users\{Your Account Name}\.platformio\packages\toolchain-xtensa-esp32s3\bin
    ```

- **firmware.elf**  
  - Found in:  
    ```
    .pio/build/{your_board_name}/
    ```

### 2. Configure Paths in `debug.py`
Edit `debug.py` and update the following paths:
```python
ADDR2LINE_PATH = r"C:\Users\YourUser\.platformio\packages\toolchain-xtensa-esp32s3\bin\xtensa-esp32s3-elf-addr2line.exe"
ELF_FILE_PATH = r"C:\Users\YourUser\Documents\PlatformIO\Projects\YourProject\.pio\build\your_board\firmware.elf"
```

### 3. Run the Script
To analyze a backtrace, execute:

python debug.py
Then, enter the backtrace addresses when prompted.

Example
PS C:\Users\admin\Documents\PlatformIO\Projects\MyProject> python debug.py
Backtrace: 0x403785da:0x3fcaffd0 0x4037e4d5:0x3fcafff0 0x40385025:0x3fcb0010 0x40384bf5:0 0x40378c09:0x3fcb0160 0x40385055:0x3fcb0180 0x4200a786:0x3fcb01a0 0x4200a117:0x3fcb03b

=== Backtrace Decoded ===
0x403785da: [Function A] at [SourceFile1]:[LineNumber]

0x4037e4d5: [Function B] at [SourceFile2]:[LineNumber]

0x40385025: [Function C] at [SourceFile3]:[LineNumber]

...
