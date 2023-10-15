from datetime import datetime, time
from odoo import api, fields, models

class WamArticle(models.Model):
    _name = "wam.article"
    _description = "Article "
    _order = "id"
    
    name = fields.Char('Article Name', required=True, translate=True)
    intro_text = fields.Html('Intro text', translate=True)
    main_text = fields.Html('Main text', translate=True)
    published = fields.Boolean('Published', compute="_compute_is_published", inverse="_inverse_is_published", store=True)
    publish_up = fields.Datetime('Publish Up')
    publish_down = fields.Datetime('Publish Down')
    author_id = fields.Many2one('res.users', string='Author', index=True, tracking=True, default=lambda self: self.env.user)
    category_id = fields.Many2one('wam.article.category', string='Category', index=True, tracking=True)
    tag_ids = fields.Many2many('wam.article.tag', string='Tags', index=True, tracking=True)
    
    active = fields.Boolean('Active', default=True)
    
    @api.depends('publish_up', 'publish_down')
    def _compute_is_published(self):
        now = fields.Datetime.now()
        for record in self:
            if record.publish_up and record.publish_down:
                record.published = record.publish_up <= now < record.publish_down
            elif record.publish_up and not record.publish_down:
                record.published = record.publish_up <= now

    def _inverse_is_published(self):
        for record in self:
                record.publish_up = datetime.now()
