from datetime import datetime, time
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class WamArticle(models.Model):
    _name = "wam.article"
    _description = "Article "
    _order = "id"
    
    fvo_name = fields.Char('Article Name', required=True)
    
    # content related fields
    fvo_intro_text = fields.Html('Intro text')
    fvo_main_text = fields.Html('Main text')
    
    # publishing related fields
    publish_up = fields.Datetime('Publish Up')
    publish_down = fields.Datetime('Publish Down')
    published = fields.Boolean('Published', compute="_compute_is_published", store=True)
    archive = fields.Datetime('Archive')
    active = fields.Boolean('Active', compute="_compute_is_archived", store=True)
    author_id = fields.Many2one('res.users', string='Author', index=True, default=lambda self: self.env.user)
    category_ids = fields.Many2many('wam.article.category', string='Category', index=True)
    tag_ids = fields.Many2many('wam.article.tag', string='Tags', index=True)

    # settings related fields
    show_title = fields.Boolean("Show title")
    show_datetime = fields.Boolean("Show datetime")
    show_author = fields.Boolean("Show Author")
    
    
    
    
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
