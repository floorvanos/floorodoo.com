from odoo import fields, models

class WamArticleCategory(models.Model):
    _name = "wam.article.category"
    _description = "Article Category"
    _order = "name"
    
    name = fields.Char('Article Name', required=True, translate=True, default="De titel")
    published = fields.Boolean('Published', default=True)
    publish_up = fields.Datetime('Publish Up')
    publish_down = fields.Datetime('Publish Down')
    
    active = fields.Boolean('Active', default=True)
    
