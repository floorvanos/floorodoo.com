# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ArticleTag(models.Model):
    _name = "bam.article.tag"
    _description = "BAM Article Tag"

    #article type fields
    
    name = fields.Char('Article Tag Name', required=True)