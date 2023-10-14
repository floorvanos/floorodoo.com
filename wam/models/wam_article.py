from datetime import datetime, time
from odoo import fields, models

class WamArticle(models.Model):
    _name = "wam.article"
    _description = "Article "
    _order = "id"
    
    name = fields.Char('Article Name', required=True, translate=True, default="De titel")
    intro_text = fields.Html('Intro text', translate=True, default="De intro tekst")
    main_text = fields.Html('Main text', translate=True, default="De hoofd tekst" )
    published = fields.Boolean('Published', default=True)
    publish_up = fields.Datetime('Publish Up')
    publish_down = fields.Datetime('Publish Down')
    author_id = fields.Many2one("res.partner", string="Author")
    
    active = fields.Boolean('Active', default=True)
    
