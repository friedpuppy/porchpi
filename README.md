# 🏡 PorchPi: Real-Time Personal Temperature Monitor

A project to create a real-time, personal temperature monitor using a Raspberry Pi.

## 🎯 Project Goal

The primary objective is to continuously monitor and display the current temperature in real-time. This system is designed to be self-contained on a Raspberry Pi device, allowing for easy deployment.

## ✨ Features & Future Ideas

* **Real-Time Display:** Constantly updates the current temperature reading.
* **Automated Updates:** A script runs every **30 seconds** to fetch and display the latest data.
* **Dedicated Hardware:** Designed to run on a Raspberry Pi 3 or 4 with a dedicated monitor.
* **Graphical Enhancements (Future):**
    * Design a simple graphical application to display the temperature on the screen (no reliance on a Windows system).
    * Implement conditional styling (e.g., change the text color to **blue** if the temperature drops below a certain **"cold" threshold**).

## 🛠️ Setup and Installation

### 1. Hardware

This project can be run on:
* Raspberry Pi 4 (if currently in use/testing)
* **Raspberry Pi 3 (target/production hardware)**
* [A connected monitor and keyboard for initial setup.](https://thepihut.com/products/official-raspberry-pi-7-touchscreen-display)

### 2. Initial Pi Configuration

1.  Decommission the current Raspberry Pi 4 setup (if applicable) and rebuild the **Raspberry Pi 3**.
2.  Set up **Wi-Fi** connectivity on the Raspberry Pi 3.
3.  Ensure Python is installed and configured.

### 3. Program Execution

The core logic is handled by a single Python program that runs in a loop.

1.  Log into the monitor connected to the Pi (using the keyboard).
2.  Navigate to the project directory.
3.  Execute the main Python program:
    ```bash
    python3 main_temp_monitor.py # (or whatever you name your script)
    ```

### 4. Continuous Monitoring Script

The main Python program must contain:
1.  The logic to read the temperature data.
2.  A loop that calls this logic and displays the result every **30 seconds**.

## 📝 Testing Notes (Windows System)

* The temperature logic/script needs to be **tested on a Windows system** first to ensure functionality and data retrieval are correct before porting it to the Pi.

## 💻 Design Thoughts: Graphical Application (GUI)

Think about how to design a simple graphical application (e.g., using **Tkinter**, **Pygame**, or another lightweight Python GUI library) to display the temperature. This application should be able to run directly on the Raspberry Pi without requiring external services or a Windows environment.

---

## 🚀 Next Steps

* Write the initial temperature reading Python script.
* Implement the 30-second loop logic.
* Begin planning the graphical application structure.
