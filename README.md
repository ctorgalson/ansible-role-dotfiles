# Ansible Role Dotfiles

[![Build Status](https://travis-ci.com/ctorgalson/ansible-role-ssl.svg?branch=master)](https://travis-ci.com/ctorgalson/ansible-role-dotfiles)

This role clones one or more dotfiles repositories from Github (or wherever), scans each one for files, then symlinks each file into a specified user's home directory. If a whitelist is provided, only whitelisted files will be linked.

## Role Variables

| Variable name       | Default value             | Description |
|---------------------|---------------------------|-------------|
| `dotfiles_conf_dir` | `.ansible-managed-config` | The name of the directory to clone dotfiles repos into. Created by the role if it does not exist. |
| `dotfiles_repos`    | `[]`                      | A list of dotfiles to clone and use to create dotfiles in the user directory. See the following variables for the available properties of each item in the list. |
| `.repo`             | `-`                       | The dotfile repo to clone. |
| `.user`             | `-`                       | The username of the user whose account dotfiles will be linked into. |
| `.name`             | `-`                       | The name of the repository. Corresponds to the `dest` property of Ansible's Git module. |
| `.version`          | `-`                       | The branch name, release/tag, or commit id to checkout. Corresponds to the `version` property of Ansible's Git module. |
| `.become_user`      | `-`                       | The name of the user to clone the repository as. This allows cloning of private repositories (when ssh keys are appropriately configured), and ensures that permissions are correctly set. When not present, the task will run as the user running the playbook. |
| `.whitelist`        | `-`                       | A list of files from the repo _not_ to symlink into the user directory. |

## Example Playbook

The following playbook creates/links:

- Files, directories, and links in the home directory of the user `molecule-1:
  - `.ansible-managed-config/dotfiles`
  - `.gitconfig`
  - `.vimrc`
- Files, directories, and links in the home directory of the user `molecule-1:
  - `.ansible-managed-config/dotfiles`
  - `.vim`
  - `.zshrc`

For more information and tests, see the repository's `molecule/` directory.

    ---
    - name: Converge
      hosts: all
      roles:
        - role: ansible-role-dotfiles
      vars:
        dotfiles_repos:
          - repo: "https://github.com/paulirish/dotfiles.git"
            user: "molecule-1"
            name: "dotfiles"
            version: "master"
            become_user: "molecule-1"
            whitelist:
              - ".gitconfig"
              - ".vimrc"
          - repo: "https://github.com/paulirish/dotfiles.git"
            user: "molecule-2"
            name: "dotfiles"
            version: "master"
            become_user: "molecule-2"
            whitelist:
              - ".vim"
              - ".zshrc"

## License

GPLv3

