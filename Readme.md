# 📅 **Leet-Daily**

This repository contains a Python script that fetches the daily question from LeetCode and opens it in your default browser. It also includes instructions on how to build the script into an executable file using PyInstaller.

## 🎯 **Purpose**

The purpose of this application is to automate the process of accessing the daily question on LeetCode. By running the script, you can quickly navigate to the problem statement without manually searching for it.

## 🚀 **Quick Run**

1. Download the `leet.exe` from the repository or by clicking [here](https://github.com/MrDracs/Leet-Daily/raw/main/leet.exe).
2. Double-click on the executable. On the warning screen, click on **More Info**, then **Run**.
3. You can also shift-right-click on `leet.exe` and add it to your taskbar for one-click access to the daily question.

## 🛠️ **Prerequisites**

To run the script, ensure that you have:

- Python installed on your machine.

For the .exe Windows app, Python is not required.

## 🖥️ **Running the Script**

To run the Python script, follow these steps:

1. Clone this repository to your local machine by running the following command in your terminal or command prompt:
    ```bash
    git clone https://github.com/MrDracs/Leet-Daily.git
    ```

2. Open a terminal or command prompt.
3. Navigate to the project directory:
    ```bash
    cd folder-name/Leet-Daily/
    ```
4. Run the script using the following command:
    ```bash
    python leet.py
    ```

The script will fetch the daily question from LeetCode and open it in your default browser.

## ⚙️ **Building the Executable**

To build the Python script into an executable file, use PyInstaller. Follow these steps:

1. Ensure that PyInstaller is installed. If not, install it using the following command:
    ```bash
    pip install pyinstaller
    ```
2. Open a terminal or command prompt.
3. Navigate to the project directory:
    ```bash
    cd folder-name/Leet-Daily/
    ```
4. Build the executable using the following command:
    ```bash
    pyinstaller --onefile leet.py
    ```
5. After the build process completes, you will find the executable file in the `dist` directory.

You can now run the generated `leet.exe` file to fetch the daily question from LeetCode and open it in your default browser.

---