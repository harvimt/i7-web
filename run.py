#!/usr/bin/python3.4
import subprocess
from pathlib import Path
import tempfile
import shutil
import asyncio

NI_PATH = Path('/usr/lib/x86_64-linux-gnu/gnome-inform7/ni')
INFORM6_PATH = Path('/usr/lib/x86_64-linux-gnu/gnome-inform7/inform6')
INFORM7_HOME = Path('/usr/share/gnome-inform7')
PROJECT_TEMPLATE_PATH = Path('/root/project.inform')


@asyncio.coroutine
def compilei7(story, output):
    story_path = Path(story)
    output_path = Path(output)
    with tempfile.TemporaryDirectory() as tempdir:
        tempdir_path = Path(tempdir)
        project_path = tempdir_path / 'project.inform'
        shutil.copytree(str(PROJECT_TEMPLATE_PATH), str(project_path))
        shutil.copyfile(
            str(story_path), str(project_path / 'Source/story.ni'))

        ni_args = [
            NI_PATH, '-internal', INFORM7_HOME, '-format=ulx',
            '-project', project_path]

        i6_args = [
            INFORM6_PATH, '-wxE2kSDG', '$huge',
            project_path / 'Build/auto.inf',
            project_path / 'Build/output.ulx']

        ni_args = list(map(str, ni_args))
        i6_args = list(map(str, i6_args))

        print(subprocess.check_output(ni_args).decode('utf8'))
        print(subprocess.check_output(i6_args).decode('utf8'))

        shutil.copyfile(
            str(project_path / 'Build/output.ulx'), str(output_path))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        compilei7('/root/story.ni', '/root/output.ulx'))
