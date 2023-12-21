# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Article(models.Model):
    _name = "bam.article"
    _description = "BAM Article"
    _order = "sequence"

    #article fields
    
    name = fields.Char('Article Name', required=True)
    # type = fields.One2many('bam.article.type', string="Type")
    # category = fields.One2many('bam.article.category', string="Category")
    # tag_ids = fields.Many2many('bam.article.tag', string="Tags")
    introtext = fields.Html('Intro Text')
    bodytext = fields.Html('Body Text')
    author_id = fields.Many2one("res.users", string="Author", default=lambda self: self.env.user)
    
    # article publishing fields
    
    publish_up = fields.Datetime('Publish')
    archive = fields.Datetime('Archive')
    trash = fields.Datetime('Trash')
    type = fields.Selection([
        ('article', 'Article'),
        ('vacancy', 'Vacancy'),
        ], string='Type', required=True, default='article')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('queued', 'Queued'),
        ('published', 'Published'),
        ('archived', 'Archived'),
        ('trashed', 'Trashed'),
        ], string='State', required=True, default='draft')
    
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence', default=10)
    
    # article preference fields
    
    show_title = fields.Boolean('Show title', default=True)
    show_date = fields.Boolean('Show date', default=True)
    show_author = fields.Boolean('Show author', default=True)
    show_introtext = fields.Boolean('Show introtext', default=False)
    