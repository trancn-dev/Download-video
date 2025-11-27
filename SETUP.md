# Setup Guide for WSL/Windows Users

This setup guide will provide detailed steps to configure your environment for downloading videos using this repository.

## Prerequisites
Before starting, ensure you have the following installed:
- Windows 10/11 or WSL (Windows Subsystem for Linux)
- Python (3.6 or higher)
- FFmpeg

### Step 1: Install Python
1. Download the Python installer from the [official Python website](https://www.python.org/downloads/).
2. Run the installer and check the box that says 'Add Python to PATH'.
3. Follow the installation instructions.

### Step 2: Install FFmpeg
1. Download the latest FFmpeg build from the [FFmpeg official site](https://ffmpeg.org/download.html).
2. Extract the downloaded zip file to a location of your choice, e.g., `C:\ffmpeg`.
3. Add FFmpeg to your system PATH:
   - Right-click on 'This PC' or 'My Computer' and select 'Properties'.
   - Click on 'Advanced system settings'.
   - In the System Properties window, click on 'Environment Variables'.
   - Find the 'Path' variable in the 'System variables' section and click 'Edit'.
   - Add `C:\ffmpeg\bin` (or the path where you extracted FFmpeg).
4. Verify FFmpeg installation by opening Command Prompt and typing `ffmpeg -version`.

### Step 3: Set up a Virtual Environment
1. Open Command Prompt or your WSL terminal.
2. Navigate to your project directory using `cd path/to/your/project`.
3. Create a virtual environment:
   - For Command Prompt: `python -m venv env`
   - For WSL: `python3 -m venv env`
4. Activate the virtual environment:
   - For Command Prompt: `.\
v\Scripts\activate`
   - For WSL: `source env/bin/activate`

### Step 4: Path Handling between WSL and Windows
When using WSL, paths differ from Windows. Here are some tips:
- Windows Path: `C:\path\to\file`  
  WSL Equivalent: `/mnt/c/path/to/file`
- Always ensure you're using the correct path depending on whether you're in Command Prompt or WSL.

### Step 5: Troubleshooting
If you run into issues:
- **Python Command Not Found**: Ensure Python is added to your PATH.
- **FFmpeg Not Found**: Check that `C:\ffmpeg\bin` is in your PATH.
- **Virtual Environment Activation Issues**: Make sure you're using the correct method for activation based on your terminal.

By following these steps, you should have a fully functional setup for downloading videos using this repository. Happy coding!