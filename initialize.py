# Copyright (c) 2015-2021 Anish Athalye (me@anishathalye.com)
#
# This software is released under AGPLv3. See the included LICENSE.txt for
# details.

if __name__ == '__main__':
    from gavel.models import db
    from gavel import app
    with app.app_context():
        db.create_all()
