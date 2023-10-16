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

    line_ids = fields.One2many("wam_article_category_line", "model_id")

class WamArticleCategoryLine(models.model):
    _name = "wam_article_category_line"
    _description = "Article Category Line"

    model_id = fields.Many2one("wam_article_category")
    
    
    
