Here is a copy-paste prompt for AI image generation (ChatGPT, GPT-Image, Midjourney, DALL-E, Bing/Cline, Flux, Ideogram, Leonardo). It will generate Fritzing-style circuit assembly image.

Prompt:
\"Generate a professional, clean Fritzing-style circuit assembly diagram for 'AgriStorage-Room'. Show breadboard view (top) and schematic view (bottom) in one image.

Include:
- Raspberry Pi 4 (40-pin) central; label GPIO, I2C, SPI
- 20W 12V solar panel -> MPPT -> 12V LiFePO4 battery with fuse + blocking diode
- Dual-axis tracker: pan/tilt bracket, 2x MG996R servos, 4x LDRs on corners -> voltage dividers -> MCP3008 (SPI) -> Pi
- Sensors: BME280 (I2C), TSL2591 (I2C), Raspberry Pi Camera
- ESP32 connected to Pi via UART (actuation)
- 4-channel opto-isolated relay module controlling 12V DC fans, exhaust fan, heater, humidifier
- Buck converters: 12V->5V (servos/relays), 12V/5V->3.3V (logic)
- HDMI industrial display connected to Pi
- Common GND, power rails labeled 12V/5V/3.3V
- Fritzing-style symbols/colors, legible labels, no cloud/internet icons
- Tomato crate icons minimal, room outline optional

Style: technical diagram, monochrome PCB-friendly with colored power rails, educational. Output: high-resolution PNG.\" 

Save image as docs/circuit/agristorage_room_circuit.png in repo.
