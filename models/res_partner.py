from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    team_sales_id = fields.Many2one(
        comodel_name='crm.team',
    )
