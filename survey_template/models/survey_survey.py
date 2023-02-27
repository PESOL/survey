from odoo import fields, models


class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    template = fields.Boolean(
        string='Is Template')
    
    survey_template_id = fields.Many2one(
        comodel_name='survey.survey',
        string='Template')
    
    def create_from_template(self):
        self.ensure_one()
        survey = self.copy({
            'template': False,
            'survey_template_id': self.id,
            'question_and_page_ids': [],
        })
        for template_page in self.page_ids:
            page = template_page.copy({
                'survey_id': survey.id,
            })
            page.question_ids = False
        for template_question in self.question_ids:
            question = template_question.copy({
                'survey_id': survey.id,
                'question_template_id': template_question.id,
                'suggested_answer_ids': [],
                'matrix_row_ids': []
            })
            for answer in template_question.suggested_answer_ids:
                answer.copy({
                    'question_id': question.id,
                    'answer_template_id': answer.id
                })
            # for answer in question.matrix_row_ids:
            #     answer.copy({
            #         'matrix_question_id': question.id,
            #         'answer_template_id': answer.id
            #     })
        return survey