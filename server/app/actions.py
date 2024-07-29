from flask import flash
from flask_babel import gettext
from .extensions import db

def change_active(self=None, ids=None):
    try:
        query = self.get_query().filter(self.model.id.in_(ids))
        
        for model in query.all():
            model.active = not model.active if model else True

        db.session.commit()
        flash(gettext('Successfully changed active status.'), category='success')
    except Exception as e:
        flash(gettext(f'Failed to change active status. {str(e)}'), category='error')
