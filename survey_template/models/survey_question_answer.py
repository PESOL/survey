from odoo import models, api, fields, _

class SurveyQuestionAnswer(models.Model):
    _inherit = 'survey.question.answer'

    answer_template_id = fields.Many2one('survey.question.answer', string='Answer Template')