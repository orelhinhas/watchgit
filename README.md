Watchgit
========

Requirements
* Python 2.7 (not tested in Python 3)
* python-daemon

Installation

1. Install dependencies:
  ```
  apt-get install python-daemon
  ```

2. Clone a repository:
  ```
  git clone https://github.com/orelhinhas/watchgit.git
  ```

3. Install Watchgit:
  ```
  ./setup.sh
  ```

Usage

In /etc/watchgit.conf:

Section [GIT]:
  repo_name = is the name of repository
   local_repo = where is your project (local, of course)
  remote_repo = URL of your repository in GIT
