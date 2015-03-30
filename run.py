#!/usr/bin/python3.4
from pathlib import Path
import tempfile
import shutil
import asyncio
from asyncio.subprocess import PIPE, STDOUT

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

        ni_proc = yield from asyncio.create_subprocess_exec(
            *ni_args, stdout=PIPE, stderr=PIPE)
        ni_out, ni_err = yield from ni_proc.communicate()
        print(ni_out.decode('utf8'))

        i6_proc = yield from asyncio.create_subprocess_exec(
            *i6_args, stdout=PIPE, stderr=PIPE)
        i6_out, i6_err = yield from i6_proc.communicate()
        print(i6_out.decode('utf8'))

        shutil.copyfile(
            str(project_path / 'Build/output.ulx'), str(output_path))

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(
        compilei7('/root/story.ni', '/root/output.ulx'))
