#!/usr/bin/python3.4
import subprocess
from pathlib import Path

NI_PATH = Path('/usr/lib/x86_64-linux-gnu/gnome-inform7/ni')
INFORM6_PATH = Path('/usr/lib/x86_64-linux-gnu/gnome-inform7/inform6')
INFORM7_HOME = Path('/usr/share/gnome-inform7')
project_path = Path('/root/project.inform')

print(subprocess.check_output(list(map(str, [NI_PATH, '-internal', INFORM7_HOME, '-format=ulx', '-project', project_path]))).decode('utf8'))
print(subprocess.check_output(list(map(str, [INFORM6_PATH, '-wxE2kSDG', '$huge', project_path / 'Build/auto.inf', project_path / 'Build/output.ulx']))).decode('utf8'))
