import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_users(host):
    assert host.user('newrelic').group == 'newrelic'


def test_packages(host):
    packages = ['python-pip']
    for package in packages:
        assert host.package(package).is_installed
