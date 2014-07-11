def ttrss_password_hash(*a, **kw):
    from hashlib import sha256
    password = a[0]
    salt = a[1]
    return 'MODE2:' + sha256("{}{}".format(salt, password)).hexdigest()


class FilterModule(object):
    ''' utility filter hash passwords '''

    def filters(self):
        return { 'ttrss_password_hash' : ttrss_password_hash }

