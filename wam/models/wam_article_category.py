from odoo import fields, models

class WamArticleCategory(models.Model):
    _name = "wam.article.category"
    _description = "Article Category"
    _order = "name"
    
    name = fields.Char('Article Category Name', required=True, translate=True, default="De titel")
    published = fields.Boolean('Published', default=True)
    publish_up = fields.Datetime('Publish Up')
    publish_down = fields.Datetime('Publish Down')
    active = fields.Boolean('Active', default=True)
    article_ids = fields.One2many('wam.article.line', 'category_id', string="Articles")

class WamArticleLine(model.Model):

    _name = "wam.article.line"
    _description = "Wam Article"
    _oder = "name"

    name = fields.Char("Name", required=True, translate=True)
    published = fields.Boolean('Published', store=True, index=True)
    author_id = fields.Many2one('res.users', string='Author', index=True)
    category_id = fields.Many2one('wam.article.category', string='Category', index=True)
    tag_ids = fields.Many2many('wam.article.tag', string='Tags', index=True)
