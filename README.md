# Ansible Role Dotfiles

[![Build Status](https://travis-ci.com/ctorgalson/ansible-role-ssl.svg?branch=master)](https://travis-ci.com/ctorgalson/ansible-role-dotfiles)

This role clones one or more dotfiles repositories from Github (or wherever), scans each one for files, then symlinks each file into a specified user's home directory. If a whitelist is provided, only whitelisted files will be linked.

## Role Variables

| Variable name       | Default value             | Description |
|---------------------|---------------------------|-------------|
| `dotfiles_conf_dir` | `.ansible-managed-config` | The name of the directory to clone dotfiles repos into. Created by the role if it does not exist. |
| `dotfiles_repos`    | `[]`                      | A list of dotfiles to clone and use to create dotfiles in the user directory. See the following variables for the available properties of each item in the list. |
| `.repo`             | `-`                       | The dotfile repo to clone. |
| `.owner`             | `-`                       | The user name of the user whose account dotfiles will be linked into. |
| `.group`             | `-`                       | The group name of the user whose account dotfiles will be linked into. |
| `.name`             | `-`                       | The name of the repository. Corresponds to the `dest` property of Ansible's Git module. |
| `.version`          | `-`                       | The branch name, release/tag, or commit id to checkout. Corresponds to the `version` property of Ansible's Git module. |
| `.whitelist`        | `-`                       | A list of files from the repo to symlink into the user directory. |
| `dotfiles_force_links` | `false` | Whether or not to force the link creation (i.e. even if a file or directory already exists at the path). |

## Example Playbook

The following playbook creates/links:

- Files, directories, and links in the home directory of the user `molecule-1`:
  - `.ansible-managed-config/dotfiles`
  - `.gitconfig`
  - `.vimrc`
- Files, directories, and links in the home directory of the user `molecule-2`:
  - `.ansible-managed-config/dotfiles`
  - `.vim`
  - `.zshrc`

For more information and tests, see the repository's `molecule/` directory.

    ---
    - hosts: all
      roles:
        - role: ansible-role-dotfiles
      vars:
        dotfiles_repos:
          - repo: "https://git@github.com/paulirish/dotfiles.git"
            owner: "molecule-1"
            group: "molecule-1"
            name: "dotfiles"
            version: "master"
            whitelist:
              - ".gitconfig"
              - ".vimrc"
          - repo: "https://git@github.com/paulirish/dotfiles.git"
            owner: "molecule-2"
            group: "molecule-2"
            name: "dotfiles"
            version: "master"
            whitelist:
              - ".vim"
              - ".zshrc"

## License

GPLv3
