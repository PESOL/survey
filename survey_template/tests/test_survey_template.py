from odoo.tests import common


class TestPartnerSurvey(common.TransactionCase):
    @classmethod
    def setUpClass(self):
        super().setUpClass()

    def test_survey_template(self):
        survey_id = self.ref('survey.survey_feedback')
        survey = self.env['survey.survey'].browse(survey_id)
        survey.template = True
        new_survey = survey.create_from_template()
        self.assertEqual(len(new_survey.question_ids), len(survey.question_ids))
