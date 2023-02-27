from odoo import models, api, fields, _

class SurveyQuestion(models.Model):
    _inherit = 'survey.question'

    question_template_id = fields.Many2one('survey.question', string='Question Template')