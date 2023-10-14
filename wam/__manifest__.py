{
    'name': 'Website Article Manager',
    'category': 'Website',
    'sequence': 20,
    'summary': 'Website Article Manager',
    'author': 'Floor van Os',
    'website': 'https://www.floorodoo.com/',
    'version': '0.12',
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/wam_article_views.xml',
        'views/wam_article_category_views.xml',
        'views/wam_article_tag_views.xml',
        'views/wam_menus.xml',
    ],
    'application': True,
}
