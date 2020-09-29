from flask import jsonify
from flask.views import MethodView


from .models import Activity, Attribute, AttributeValueList, Skill


class PaymentResource(MethodView):
    def get(self):
        return jsonify(ok=True)

    def post(self):
        pass


class WantToHelpResource(MethodView):
    def post(self):
        return jsonify(ok=True)


class NeedHelpResource(MethodView):
    def post(self):
        return jsonify(ok=True)


class FacultyResource(MethodView):
    def get(self):
        faculty_attribute = Attribute.query.filter_by(name="Fakulta").one()
        faculties = AttributeValueList.query.filter_by(attribute_id=faculty_attribute.id).all()
        return jsonify(faculties)


class ActivityResource(MethodView):
    def get(self):
        activities = Activity.query.all()
        return jsonify(activities)


class SkillResource(MethodView):
    def get(self):
        skills = Skill.query.filter_by(visible=True, validated=True).all()
        return jsonify(skills)
