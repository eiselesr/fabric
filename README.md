run with
fab -R '<role to run command on, e.g c2_1>' runCommand:<command to run>
or to run on a specific host:
fab -H '10.0.2.194:2222' runCommand:'hostname'


# check device has btrfs with /etc/fstab. The text btrfs will be in there. Alternatively run $ df -Th from /. There will be an /app directory of type btrfs. 
