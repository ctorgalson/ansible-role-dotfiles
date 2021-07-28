# Ansible Role Dotfiles

[![Build Status](https://travis-ci.com/ctorgalson/ansible-role-ssl.svg?branch=master)](https://travis-ci.com/ctorgalson/ansible-role-dotfiles)

This role clones one or more dotfiles repositories from Github (or wherever), scans each one for files, then symlinks each file into a specified user's home directory. If a allowlist is provided, only allowlisted files will be linked.

## Breaking Changes

v2.0.0 includes what might be a breaking change: **the playbook no longer symlinks directories**, but continues to symlink files at any directory depth. The practical effect of this is that it's no longer possible, for example, to add `.vim` to a dotfile repository's `allowlist` and expect the _directory_ to be symlinked into place. If the `allowlist` is empty, or if files _within_ `.vim` are contained in an `allowlist`, those files will continue to be symlinked.

## Role Variables

| Variable name       | Default value             | Description |
|---------------------|---------------------------|-------------|
| `dotfiles_conf_dir` | `.config/ansible-managed-config` | The name of the directory to clone dotfiles repos into. Created by the role if it does not exist. |
| `dotfiles_repos`    | `[]`                      | A list of dotfiles to clone and use to create dotfiles in the user directory. See the following variables for the available properties of each item in the list. |
| `.repo`             | `-`                       | The dotfile repo to clone. |
| `.owner`            | `-`                       | The user name of the user whose account dotfiles will be linked into. |
| `.group`            | `-`                       | The group name of the user whose account dotfiles will be linked into. |
| `.name`             | `-`                       | The name of the repository. Corresponds to the `dest` property of Ansible's Git module. |
| `.version`          | `-`                       | The branch name, release/tag, or commit id to checkout. Corresponds to the `version` property of Ansible's Git module. |
| `.allowlist`        | `-`                       | A list of files from the repo to symlink into the user directory. |
| `.denylist`         | `-`                       | A list of files from the repo **not** to symlink into the user directory. Files specified in both `allowlist` _and_ `denylist` will **not** be symlinked. |
| `.force_links`      | `-`                       | Whether or not to force the link creation (i.e. even if a file or directory already exists at the path). |

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
            name: "dotfiles"
            version: "master"
            owner: "molecule-1"
            group: "molecule-1"
            allowlist:
              - ".git"
              - ".gitconfig"
              - ".vimrc"
          - repo: "https://git@github.com/paulirish/dotfiles.git"
            name: "dotfiles"
            version: "master"
            owner: "molecule-2"
            group: "molecule-2"
            allowlist:
              - ".vim"
              - ".zshrc"
          - repo: "https://git@github.com/paulirish/dotfiles.git"
            name: "dotfiles"
            version: "master"
            owner: "molecule-3"
            group: "molecule-3"
            denylist:
              - ".zshrc"
            force_links: true

## License

GPLv3
