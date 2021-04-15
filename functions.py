import os, json


def unmount(disk_name, disks):
    if disk_name in disks:
        os.system(f'umount {disk_name}')
    del disks[disk_name]
    return disks


def mount(disk_name):
    os.system(f'mount {disk_name}')
    disks = make_request()
    return disks


def formating(disk_name, disks):
    if disk_name in disks:
        os.system(f'mkfs -t xfs {disk_name}')


def make_request(log_name):
    request = os.system(f'lsblk -J > {log_name}')
    with open(log_name) as f:
        request = json.load(f)
    return {item['name']: (item['size'], item['mountpoint']) for item in request['blockdevices']}
    