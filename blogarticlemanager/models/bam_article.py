# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Article(models.Model):
    _name = "bam.article"
    _description = "BAM Article"
    _order = "sequence"

    name = fields.Char('Article Name', required=True, translate=True)
    author_id = fields.Many2one('res.users', string='Author', default=lambda self: self.env.user)
    # type = fields.Onetomany('bam.article.type', string="Type")
    # category = fields.Onetomany('bam.article.category', string="Category")
    # tag_ids = fields.Many2many('bam.article.tag', string="Tags")
    introtext = fields.Html('Intro Text')
    bodytext = fields.Html('Body Text')
    publish_up = fields.Datetime('Publish')
    archive = fields.Datetime('Archive')
    trash = fields.Datetime('Trash')
    # state = fields.Selection(
    #    string='State',
    #    selection=[('draft', 'Draft'), ('queued', 'Queued'), ('published', 'Published'), ('archived', 'Archived'), ('trashed', 'Trashed')])
   

    active = fields.Boolean('Active', default=True)
    sequence = fields.Integer('Sequence', default=10)