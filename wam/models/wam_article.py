from datetime import datetime, time
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class WamArticle(models.Model):
    _name = "wam.article"
    _description = "Article "
    _order = "id"
    
    name = fields.Char('Article Name', required=True)
    intro_text = fields.Html('Intro text')
    main_text = fields.Html('Main text')
    publish_up = fields.Datetime('Publish Up')
    publish_down = fields.Datetime('Publish Down')
    published = fields.Bool('Published', compute="_compute_is_published")
    author_id = fields.Many2one('res.users', string='Author', index=True, default=lambda self: self.env.user)
    category_id = fields.Many2one('wam.article.category', string='Category', index=True)
    tag_ids = fields.Many2many('wam.article.tag', string='Tags', index=True)
    
    active = fields.Boolean('Active', default=True)
    
    @api.depends("publish_up", "publish_down")
    def _compute_is_published(self):
        now = datetime.now()
        for record in self:
            if record.publish_up and record.publish_down:
                record.published = record.publish_up <= now < record.publish_down
            elif record.publish_up and not record.publish_down:
                record.published = record.publish_up <= now
    
    @api.constrains('publish_down')
    def check_publish_down(self):
        for record in self:
            if record.publish_down and record.publish_down <= record.publish_up:
                raise ValidationError("Publish down cannot be before publish up ")

