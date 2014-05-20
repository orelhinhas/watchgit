#!/usr/bin/python

# Copyright 2014 Joao Gabriel
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.
#
# @author: Joao Gabriel <jglisanti@gmail.com>.


import os
import time
import ConfigParser
from daemon import runner
from git import Repo, GitCommandError

config = ConfigParser.RawConfigParser()
config.read('/etc/watchgit.conf')

class WatchGit():
  def __init__(self):
    self.stdin_path = '/dev/null'
    self.stdout_path = config.get('GLOBAL', 'log')
    self.stderr_path = config.get('GLOBAL', 'log')
    self.pidfile_path = config.get('GLOBAL', 'pid')
    self.pidfile_timeout = 5

  def run(self):
    while True:
      git_action()
      time.sleep(5)

def git_action():
  local_repo = config.get('GIT', 'local_repo')
  remote_repo = config.get('GIT', 'remote_repo')
  repo_name = config.get('GIT', 'repo_name')
  if not os.path.exists(local_repo):
    os.umask(0022)
    Repo.clone_from(remote_repo, local_repo)
  else:
    repo = Repo(local_repo)
    try:
      remote = repo.create_remote(repo_name, remote_repo)
    except GitCommandError:
      pass
    origin = repo.remotes.origin
    origin.pull()

if __name__ == "__main__":
  watchgit = WatchGit()
  daemon_runner = runner.DaemonRunner(watchgit)
  try:
    daemon_runner.do_action()
  except runner.DaemonRunnerStopFailureError:
    print "Watchgit is not running"
