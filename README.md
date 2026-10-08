# AgriStorage-Room
Multi-modal edge-AI system for early post-harvest tomato spoilage detection with solar tracking, environmental auto-regulation, and offline monitoring. Runs fully on-device (no cloud dependency).

## Background & Motivation
Post-harvest losses remain a major challenge for rural communities in Cameroon. Studies estimate that 30-40% of fresh tomatoes are wasted annually due to poor storage, limited cold-chain access, and lack of affordable spoilage detection in rural areas. This directly impacts market losses for rural business owners, reducing their ability to earn a stable income from their harvest.

Fresh tomatoes are the most consumed ingredient in nearly every Cameroonian dish, making them both economically and culturally important. Inspired by the need to reduce waste, improve shelf-life, and help rural farmers/producers store their harvest longer to sell at better prices, AgriStorage-Room was developed to bring affordable edge-AI technology to low-resource settings.

## Key Features
- Edge AI spoilage detection (TFLite/ONNX/OpenCV fallback) – fully offline
- Solar panel dual-axis tracking to locate highest light intensity (energy autonomy)
- Auto-regulation for tomatoes-only storage (temp/humidity/Ventilation targets)
- Display options (UL-listed/NVIDIA/industrial) for local room monitoring
- FIFO crate queue for stock rotation
- Modular, low-power design for rural conservatories

## Hardware Components (Suggested)
- Microcontroller/Edge: Raspberry Pi 4/CM4, Jetson Nano Orin (NVIDIA), or ESP32 + SBC (hybrid)
- Solar tracking: 2x SG90/MG996R or linear actuators, LDRs (4-quadrant) or light sensor array, MPPT charge controller
- Sensors: BME280/DHT22 (temp/RH), light (TSL2591/BH1750), optional gas (MQ series avoided or calibrated)
- Display: Industrial HDMI/LCD (UL-listed solutions recommended), NVIDIA Jetson-compatible touch displays
- Actuators: DC fans, small heater/exhaust, servo motors for panel

## Solar Tracking Logic
Simple LDR-based maximum light search (pan/tilt) with hysteresis, day/night detection, wind/stall protection. Runs offline on microcontroller.

## Room Auto-Regulation (Tomatoes-only)
Target ranges (tomatoes): ~12–15 °C, RH ~85–90% (green/mature varies). Control logic uses deadbands to avoid oscillation; priority on spoilage prevention.

## Display & Monitoring
Recommended credentialed/industrial options: UL-listed panel PCs/displays for safety, or NVIDIA Jetson ecosystem displays. Local UI shows queue, rot risk, env, panel position, power.
