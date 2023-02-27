from odoo import models, api, fields, _


class SurveyUserInputLine(models.Model):
    _inherit = 'survey.user_input.line'

    question_template_id = fields.Many2one(
        'survey.question', string='Template Question',
        related='question_id.question_template_id', store=True)

    answer_template_id = fields.Many2one(
        'survey.question.answer', string='Template Suggested Answer',
        related='suggested_answer_id.answer_template_id', store=True)

    # template_matrix_row_id = fields.Many2one(
    #     'survey.question.answer', string='Template Matrix Row',
    #     related='matrix_row_id.template_answer_id', store=True)