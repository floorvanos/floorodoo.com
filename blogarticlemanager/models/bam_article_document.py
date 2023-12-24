# part of BAM

from odoo import models

class ArticleDocument(models.Model):
    _name = 'bam.article.document'
    _inherit = ['documents.mixin']
    _description = 'Article Document'