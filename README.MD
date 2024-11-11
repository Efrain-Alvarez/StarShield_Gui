# How to Run

## Copy the repo from Github onto your local pc
## 1. Clone the GitHub Repository
To clone the repository to your local machine, follow these steps:
1. Open your terminal (Command Prompt, PowerShell, or Terminal on macOS/Linux).
2. Navigate to the directory you want clone the github repo to
3. Use git command: git clone https://github.com/Efrain-Alvarez/StarShield_Gui.git

## Set up your virtual enviroment (optional)
### Make sure you have python and pip installed:
python3 --version  
pip --version  

1. python3 -m venv venv
2. .\venv\Scripts\activate

To install dependencies 
1. pip install -r requirements.txt

To exit out of Virtual Enviorment
1. deactivate

## Links to Installer of QT Designer
https://build-system.fman.io/qt-designer-download  

## Troubleshooting 
PyQt5 is built on Qt, which is coded in C++. PyQt5 is not your standard library that is "native" Python, but it is a plugin that runs partly in C++. This is why your computer needs to have "C++ build tools" installed. Those build tools are installed if you have Visual Studio installed (note: Visual Studio Code is different and does not include the tools), which could be why some instructions skip this step.