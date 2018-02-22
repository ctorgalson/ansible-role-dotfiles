import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('path', [
    '/home/molecule/.config/konsolerc',
    '/home/molecule/.local/share/konsole',
    '/home/molecule/.vimrc.after',
    '/home/molecule/.vimrc.before',
])
def test_packages(host, path):
    f = host.file(path)

    assert f.exists
    assert f.user == 'molecule'
    assert f.group == 'molecule'
