from datetime import datetime, time
from odoo import fields, models

class article(models.Model):
    _name = "article"
    _description = "Article "
    _order = "id"
    
    @tools.ormcache()
    def _get_default_category_id(self):
        # Deletion forbidden (at least through unlink)
        return self.env.ref('product.product_category_all')

    def _read_group_categ_id(self, categories, domain, order):
        category_ids = self.env.context.get('default_categ_id')
        if not category_ids and self.env.context.get('group_expand'):
            category_ids = categories._search([], order=order, access_rights_uid=SUPERUSER_ID)
        return categories.browse(category_ids)

    name = fields.Char('Article Name', required=True, translate=True)
     categ_id = fields.Many2one(
        'article.category', 'Article Category',
        change_default=True, default=_get_default_category_id, group_expand='_read_group_categ_id',
        required=True)

    intro_text = fields.Html('Intro text', translate=True)
    main_text = fields.Html('Main text', translate=True)
    published = fields.Boolean('Published', default=False)
    publish_up = fields.Datetime('Publish Up')
    publish_down = fields.Datetime('Publish Down')
    
    active = fields.Boolean('Active', default=True)
    
