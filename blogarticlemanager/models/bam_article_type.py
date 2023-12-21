# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ArticleType(models.Model):
    _name = "bam.article.type"
    _description = "BAM Article Type"
    _order = "sequence"

    #article type fields
    
    name = fields.Char('Article Type Name', required=True)