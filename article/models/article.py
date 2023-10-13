from odoo import fields, models


class article(models.Model):
    _name = "article"
    _description = "Article "
    _order = "sequence"

    name = fields.Char('Article Name', required=True, translate=True)
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence', default=10)
    