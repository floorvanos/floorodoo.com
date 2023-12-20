# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Blog Articles Manager',
    'version': '0.1.002',
    'author': 'Floor van Os',
    'category': 'Website',
    'summary': 'Manage all your blog articles',
    'website': 'https://floorodoo.com',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/bam_article_views.xml',
        'views/bam_menus.xml',
    ],
    'installable': True,
    'application': True
}
