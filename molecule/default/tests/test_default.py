import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('user,path', [
    ('molecule-1', '/home/molecule-1/.ansible-managed-config'),
    ('molecule-1', '/home/molecule-1/.gitconfig'),
    ('molecule-1', '/home/molecule-1/.vimrc'),
    ('molecule-2', '/home/molecule-2/.ansible-managed-config'),
    ('molecule-2', '/home/molecule-2/.vim'),
    ('molecule-2', '/home/molecule-2/.zshrc'),
])
def test_present_dotfiles(host, user, path):
    f = host.file(path)

    assert f.exists
    assert f.user == user
    assert f.group == user


@pytest.mark.parametrize('user,path', [
    ('molecule-1', '/home/molecule-1/.git'),
])
def test_absent_dotfiles(host, user, path):
    f = host.file(path)

    assert not f.exists
