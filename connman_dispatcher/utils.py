import os
import subprocess
import logbook
logger = logbook.Logger('connman-dispatcher')


def is_executable(path):
    return all([os.path.isfile(path), os.access(path, os.X_OK)])

def execute_scripts_in_dirs(paths, state):
    for path in sorted(paths):
        if os.path.exists(path) and os.path.isdir(path):
            execute_scripts_in_dir(path, state)

def execute_scripts_in_dir(path, state):
    for script in sorted(os.listdir(path)):
        full_scirpt_path = os.path.join(path, script)
        if os.path.exists(full_scirpt_path):
            if is_executable(full_scirpt_path):
                logger.info('executing: %s %s' % (full_scirpt_path, state))
                subprocess.Popen([full_scirpt_path, state])
            else:
                logger.error('%s is not executable file' % full_scirpt_path)

