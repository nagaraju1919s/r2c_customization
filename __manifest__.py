# -*- coding: utf-8 -*-

{
    'name':'bhargav_equipment',
    'summary':"""this a module of root2cloud sol""",
    'depends':['partner_autocomplete','product','stock','mail','purchase'],
    'description':"""this is a test module""",
    'data':[
    'views/equipment_view.xml',
    'views/partner_view.xml',
    'views/product_view.xml',
    'security/ir.model.access.csv',
    'security/security.xml',
    'wizard/equipment_cancel_wizard_view.xml',
    'report/report.xml',
    'report/machine_report.xml',
    'report/sale_report_inherit.xml',
    ],
}