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
        'views/article_menus.xml',
        'views/article_views.xml',
    ],
    'application': True,
}
