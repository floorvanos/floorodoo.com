# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Article(models.Model):
    _name = "bam.article"
    _description = "BAM Article"
    _order = "sequence"

    name = fields.Char('Article Name', required=True)
    # author_id = fields.One2many('res.users', string='Author', default=lambda self: self.env.user)
    # type = fields.One2many('bam.article.type', string="Type")
    # category = fields.One2many('bam.article.category', string="Category")
    # tag_ids = fields.Many2many('bam.article.tag', string="Tags")
    introtext = fields.Html('Intro Text')
    bodytext = fields.Html('Body Text')
    publish_up = fields.Datetime('Publish')
    archive = fields.Datetime('Archive')
    trash = fields.Datetime('Trash')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('queued', 'Queued'),
        ('published', 'Published'),
        ('archived', 'Archived'),
        ('trashed', 'Trashed'),
        ], string='State', required=True, default='draft'),
    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence', default=10)