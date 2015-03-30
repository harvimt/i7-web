#!/usr/bin/python3.4
import subprocess
from pathlib import Path
import tempfile
import shutil

NI_PATH = Path('/usr/lib/x86_64-linux-gnu/gnome-inform7/ni')
INFORM6_PATH = Path('/usr/lib/x86_64-linux-gnu/gnome-inform7/inform6')
INFORM7_HOME = Path('/usr/share/gnome-inform7')
PROJECT_TEMPLATE_PATH = Path('/root/project.inform')

def compilei7(story, output):
    story_path = Path(story)
    output_path = Path(output)
    with tempfile.TemporaryDirectory() as tempdir:
        tempdir_path = Path(tempdir)
        project_path = tempdir_path / 'project.inform'
        shutil.copytree(str(PROJECT_TEMPLATE_PATH), str(project_path))
        shutil.copyfile(str(story_path), str(project_path / 'Source/story.ni'))

        print(subprocess.check_output(list(map(str, [NI_PATH, '-internal', INFORM7_HOME, '-format=ulx', '-project', project_path]))).decode('utf8'))
        print(subprocess.check_output(list(map(str, [INFORM6_PATH, '-wxE2kSDG', '$huge', project_path / 'Build/auto.inf', project_path / 'Build/output.ulx']))).decode('utf8'))

        shutil.copyfile(str(project_path / 'Build/output.ulx'), str(output_path))

if __name__ == '__main__':
    compilei7('/root/story.ni', '/root/output.ulx')
