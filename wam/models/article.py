from datetime import datetime, time
from odoo import fields, models
STATE = [
    ('concept', 'Concept'),
    ('approved', 'Approved'),
    ('awaits', 'Awaits Publishing'),
    ('published', 'Published'),
    ('unpublished', 'Unpublished'),
    ('archived', 'Archived'),
]

class article(models.Model):
    _name = "article"
    _description = "Article "
    _order = "id"
    
    name = fields.Char('Article Name', required=True, translate=True, default="De titel")
    intro_text = fields.Html('Intro text', translate=True, default="De intro tekst")
    main_text = fields.Html('Main text', translate=True, default="De hoofd tekst" )
    state = fields.Selection(STATE, string='Article Status', store=True,
        help="It indicates the article status.\n" default='concept')
    publish_up = fields.Datetime('Publish Up')
    publish_down = fields.Datetime('Publish Down')
    # select a portal user as author?
    author = fields.Char('Author', required=True, translate=True)
    # -----------------------------------
    show_date = fields.Boolean('Show publishing date', default=False)
    show_author = fields.Boolean('Show author', default=False)
    
    
    active = fields.Boolean('Active', default=True)
    
