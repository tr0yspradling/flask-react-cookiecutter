# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template
from flask_login import login_required

blueprint = Blueprint('user', __name__, url_prefix='/user', static_folder='../static')

@blueprint.route('/')
@login_required
def index():
    """Show index."""
    return render_template('user/index.html')
