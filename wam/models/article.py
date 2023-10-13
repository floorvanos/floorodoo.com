from odoo import fields, models

class article(models.Model):
    _name = "article"
    _description = "Article "
    _order = "sequence"

    name = fields.Char('Article Name', required=True, translate=True)
    intro_text = fields.Html('Intro text', translate=True)
    main_text = fields.Html('Main text', translate=True)
    active = fields.Boolean('Active', default=True)
