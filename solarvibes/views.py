from flask import redirect, url_for
from solarvibes import app

#############################
# SITE INDEX
#############################
@app.route('/', methods=['GET'])
# @login_required
def site_index():
    return redirect(url_for('site.index'))
