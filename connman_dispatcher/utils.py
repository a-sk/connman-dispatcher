import os
import subprocess
import logbook
logger = logbook.Logger('connman-dispatcher')


def execute_scripts_in_dirs(paths, state):
    for path in paths:
        if os.path.exists(path) and os.path.isdir(path):
            execute_scripts_in_dir(path, state)

def execute_scripts_in_dir(path, state):
    for script in sorted(os.listdir(path)):
        full_scirpt_path = os.path.join(path, script)
        if os.path.exists(full_scirpt_path):
            logger.info('executing: %s' % full_scirpt_path)
            subprocess.Popen([full_scirpt_path, state])

