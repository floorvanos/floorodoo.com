from datetime import datetime, time
from odoo import fields, models

class WamArticle(models.Model):
    _name = "wam.article"
    _description = "Article "
    _order = "id"
    
    name = fields.Char('Article Name', required=True, translate=True)
    intro_text = fields.Html('Intro text', translate=True)
    main_text = fields.Html('Main text', translate=True)
    published = fields.Boolean('Published', default=True)
    publish_up = fields.Datetime('Publish Up')
    publish_down = fields.Datetime('Publish Down')
    author_id = fields.Many2one('res.users', string='Author', index=True, tracking=True, default=lambda self: self.env.user)
    category_id = fields.Many2one('wam.article.category', string='Category', index=True, tracking=True)
    tag_ids = fileds.Many2many('wam.article.tag', string='Tags', index=True, tracking=True)
    
    active = fields.Boolean('Active', default=True)
    
