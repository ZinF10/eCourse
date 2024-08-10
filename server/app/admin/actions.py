from flask import flash, jsonify
from flask_babel import gettext
from ..models import db

def change_active(self=None, ids=None):
    try:
        query = self.get_query().filter(self.model.id.in_(ids))
        
        for model in query.all():
            model.is_active = not model.is_active if model else True

        db.session.commit()
        flash(gettext('Successfully changed active status.'), category='success')
    except Exception as e:
        flash(gettext(f'Failed to change active status. {str(e)}'), category='error')


def view_json(self=None, ids=None):
    query = self.get_query().filter(self.model.id.in_(ids))
    result = []
    for model in query.all():
        result.append(model.to_dict())
    return jsonify(result)