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
    archive = fields.Datetime('Archive')
    active = fields.Boolean('Active', compute="_compute_is_archived", store=True)
    author_id = fields.Many2one('res.users', string='Author', index=True, default=lambda self: self.env.user)
    category_ids = fields.Many2many('wam.article.category', string='Category', index=True)
    tag_ids = fields.Many2many('wam.article.tag', string='Tags', index=True)
    
    my_selection_field = fields.Selection([('option1', 'Label 1'), ('option2', 'Label 2')], string='My Selection Field')
    
    # settings related fields
    show_title = fields.Selection([('-1', 'Inherit'), ('0', 'No'), ('1', 'Yes')], string='Show title', default='-1')
    show_datetime = fields.Selection([('-1', 'Inherit'), ('0', 'No'), ('1', 'Yes')], string='Show publishing date time', default='-1')
    show_author = fields.Selection([('-1', 'Inherit'), ('0', 'No'), ('1', 'Yes')], string='Show Author', default='-1')
    
    @api.constrains('publish_down')
    def check_publish_down(self):
        for record in self:
            if record.publish_down and record.publish_down <= record.publish_up:
                raise ValidationError("Publish down cannot be before publish up ")

    @api.depends("archive")
    def _compute_is_archived(self):
        now = datetime.now()
        for record in self:
            if record.archive:
                record.active = now < record.archive

    def action_publish_up(self):
        for record in self:
            record.publish_up = datetime.now()
        return True

    def action_publish_down(self):
        for record in self:
            record.publish_up = ''
        return True
