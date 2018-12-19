# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models

AVAILABLE_PRIORITIES = [
    ('0', 'Normal'),
    ('1', 'Low'),
    ('2', 'High'),
    ('3', 'Urgent'),
]


class FSMStage(models.Model):
    _name = 'fsm.stage'
    _description = 'Field Service Stage'
    _order = 'sequence, name, id'

    name = fields.Char(string='Name', required=True)
    sequence = fields.Integer('Sequence', default=1,
                              help="Used to order stages. Lower is better.")
    legend_priority = fields.Text('Priority Management Explanation',
                                  translate=True,
                                  help='Explanation text to help users using'
                                       ' the star and priority mechanism on'
                                       ' stages or orders that are in this'
                                       ' stage.')
    fold = fields.Boolean('Folded in Kanban',
                          help='This stage is folded in the kanban view when '
                               'there are no record in that stage to display.')
    is_closed = fields.Boolean('Is a close stage',
                               help='Services in this stage are considered '
                                    'as closed.')
    custom_color = fields.Char("Color Code", default="#FFFFFF")

    @api.multi
    def get_color_information(self):
        # get stage ids
        stage_ids = self.search([])
        color_information_dict = []
        for stage in stage_ids:
            color_information_dict.append({
                'color': stage.custom_color,
                'field': 'stage_id',
                'opt': '==',
                'value': stage.name,
            })
        return color_information_dict
