
Open Terminal for the following
-------------------------------

To allow scripts to run:
=========================
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

To install a virtual environment called "dev"
REM: Remember that a virtual environment creates a small project-specific set of code libraries, which makes them easier to delete and avoids versioning hell,
encountered when running multiple projects on one machine.
=========================================================
python -m venv .venv

To activate virtual environment:
================================
.venv\scripts\activate

source venv/bin/activate

To install Flask, if not already installed
==========================================
pip install pypdf
pip install yt-dlp
pip install ffmpeg-python # ffmpeg must be installed on the machine https://www.ffmpeg.org/download.html

To install ffmpeg, if not already installed
==========================================
See https://www.ffmpeg.org/download.html
choco install ffmpeg


To run:
=======
python app.py






