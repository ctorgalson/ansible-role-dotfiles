import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('user,path', [
    ('molecule-1', '/home/molecule-1/.config/ansible-managed-config'),
    ('molecule-1', '/home/molecule-1/.gitconfig'),
    ('molecule-1', '/home/molecule-1/.vimrc'),
    ('molecule-2', '/home/molecule-2/.config/ansible-managed-config'),
    ('molecule-2', '/home/molecule-2/.zshrc'),
    ('molecule-3', '/home/molecule-3/.config/ansible-managed-config'),
    ('molecule-3', '/home/molecule-3/.bashrc'),
])
def test_present_dotfiles(host, user, path):
    """ Test to verify that allowlisted files are present. """

    f = host.file(path)

    """ Note that we're not verifying permissions because symlinks will usually
    be owned by root, and can't ordinarily be changed. The role doesn't 'become'
    the user in question, so they will always be root:root. """
    assert f.exists


@pytest.mark.parametrize('user,path', [
    ('molecule-1', '/home/molecule-1/.git'),
    ('molecule-3', '/home/molecule-3/.zshrc'),
])
def test_absent_dotfiles(host, user, path):
    """ Test to verify that denylisted files are not present, .git/ is never
    present, and that files linked using 'force_links' are present. """

    f = host.file(path)

    assert not f.exists
