# needed?
from datetime import datetime, time
# -------------
from odoo import fields, models

class article(models.Model):
    _name = "article"
    _description = "Article "
    _order = "id"
    
    name = fields.Char('Article Name', required=True, translate=True, default="De titel")
    intro_text = fields.Html('Intro text', translate=True, default="De intro tekst")
    main_text = fields.Html('Main text', translate=True, default="De hoofd tekst" )
    published = fields.Boolean('Published', default=True)
    publish_up = fields.Datetime('Publish Up')
    publish_down = fields.Datetime('Publish Down')
    
    active = fields.Boolean('Active', default=True)
    
