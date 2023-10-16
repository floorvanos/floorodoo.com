from odoo import fields, models

class WamArticleTag(models.Model):
    _name = "wam.article.tag"
    _description = "Article Tag"
    _order = "name"
    
    name = fields.Char('Article Tag Name', required=True, translate=True, default="De titel")
    published = fields.Boolean('Published', default=True)
    publish_up = fields.Datetime('Publish Up')
    publish_down = fields.Datetime('Publish Down')
    
    active = fields.Boolean('Active', default=True)

class WamArticleTagItems(models.Model):
    _name = "wam.article.tag.items"
    _description = "Article Tag Items"
    _order = "name"
    
