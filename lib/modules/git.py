import subprocess
from lib.modules.mutils import which

class GitControl(object):
    def __init__(self, repo_config):
        self._repoDir = repo_config.dir if (dir in repo_config) else False
        self._remoteUrl = repo_config.url
        self._remoteName = repo_config.remote
        if which('git') is None:
            raise ValueError('Git needs to be installed in the sysem...')

        raise ValueError('Parameter should...')

    def add(self, add_string):
        cmd = ['git', 'add', add_string]
        p = subprocess.Popen(cmd, cwd=self._repoDir)
        p.wait()

    def clone(self):
        cmd = ['git', 'clone', self._remoteUrl]
        if self._repoDir:
            cmd.append(self._repoDir)
        p = subprocess.Popen(cmd, cwd='~')
        p.wait()

    def status(self):
        cmd = ['git', 'status']
        p = subprocess.Popen(cmd, cwd=self._repoDir)
        p.wait()

    def co(self, co_string):
        cmd = ['git', 'checkout', co_string]
        p = subprocess.Popen(cmd, cwd=self._repoDir)
        p.wait()
