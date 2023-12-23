# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ArticleCategory(models.Model):
    _name = "bam.article.category"
    _description = "BAM Article Category"
    _order = "sequence"

    #article category fields
    
    name = fields.Char('Article Category Name', required=True)
    parent_id = fields.Many2one("bam.article.category", string="Parent Menu", placeholder="Root")
    sequence = fields.Integer('Sequence', default=0)