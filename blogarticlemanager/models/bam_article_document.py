# part of BAM

from odoo import models

class Document(models.Model):
    _name = 'bam.article.document'
    _inherit = ['documents.mixin']