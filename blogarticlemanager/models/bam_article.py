# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class Article(models.Model):
    _name = "bam.article"
    _description = "BAM Article"
    _order = "publish_up desc"

    #article fields
    
    name = fields.Char('Title', required=True)
    alias = fields.Char('Alias', compute="_compute_alias", store=True)
    # type = fields.One2many('bam.article.type', string="Type")
    # category = fields.One2many('bam.article.category', string="Category")
    
    introtext = fields.Html('Intro Text')
    bodytext = fields.Html('Body Text')
    author_id = fields.Many2one("res.users", string="Author", default=lambda self: self.env.user)
    
    # article publishing fields
    
    publish_up = fields.Datetime('Publish')
    archive = fields.Datetime('Archive')
    trash = fields.Datetime('Trash')
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence', default=10)
    
    #article property fields
    
    category_id = fields.Many2one("bam.article.category", string="Category")
    type_id = fields.Many2one("bam.article.type", string="Type")
    tag_ids = fields.Many2many('bam.article.tag', string="Tags")
    state = fields.Selection([
        ('draft', 'Draft'),
        ('queued', 'Queued'),
        ('published', 'Published'),
        ('archived', 'Archived'),
        ('trashed', 'Trashed'),
        ], string='State', required=True, default='draft', compute="_compute_state")
    
    #article media fields
    
    image_1920 = fields.Image("Image", max_width=1920, max_height=1920)
    document_ids = fields.Many2many("documents.document", string="Attached Documents")
    
    # extra vacancy fields
    
    partner_id = fields.Many2one("res.partner", string="Provider")
    
    # article preference fields
    
    show_title = fields.Boolean('Show title', default=True)
    show_date = fields.Boolean('Show date', default=True)
    show_author_id = fields.Boolean('Show author', default=True)
    show_introtext = fields.Boolean('Show introtext', default=False)
    
    # buttons
    
    def action_preview(self):
        return True
    
    def action_draft(self):
        for record in self:
            record.publish_up = ''
            record.state = 'draft'
        
    def action_publish_up(self):
        for record in self:
            record.publish_up = fields.Datetime.now()
            record.state = 'published'
        return True
        
    def action_archive(self):
        for record in self:
            record.archive = fields.Datetime.now()
        return True
    
    def action_trash(self):
        for record in self:
            record.trash = fields.Datetime.now()
        return True    
    
    # computed fields
   
    # this should also CRON
    @api.depends("publish_up","archive","trash")
    def _compute_state(self):
        for record in self:
            if record.publish_up and record.trash and record.trash <= fields.Datetime.now():
                record.state = "trashed"
            elif record.publish_up and record.archive and record.archive <= fields.Datetime.now():
                record.state = "archived"
            elif record.publish_up and record.publish_up <= fields.Datetime.now():
                record.state = "published"
            elif record.publish_up and record.publish_up => fields.Datetime.now():
                record.state = "queued"
            else:
                record.state = "draft"
    
    # to finish make alias
    @api.onchange("name")
    def _onchange_name(self):
        self.name.replace("  "," ")
        self.alias = self.name.replace(" ","-").lower()
        
        
    @api.constrains('publish_up', 'archive', 'trash', '')
    def _check_dates(self):
        for article in self:
            if article.publish_up and article.archive and article.archive <= article.publish_up:
                raise ValidationError(_('The archiving date cannot be earlier than the publishing date.'))
            if article.publish_up and article.trash and article.trash <= article.publish_up:
                raise ValidationError(_('The trashing date cannot be earlier than the publishing date.'))
                