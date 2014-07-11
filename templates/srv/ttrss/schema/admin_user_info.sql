UPDATE ttrss_users
   SET login    = '{{ ttrss_admin_username }}',
       pwd_hash = '{{ ttrss_admin_password|ttrss_password_hash(ttrss_admin_password_salt) }}',
       salt     = '{{ ttrss_admin_password_salt }}'
 WHERE id = 1;
