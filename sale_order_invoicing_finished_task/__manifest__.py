# -*- coding: utf-8 -*-
# Copyright 2017 Sergio Teruel <sergio.teruel@tecnativa.com>
# Copyright 2017 Carlos Dauden <carlos.dauden@tecnativa.com>
# Copyright 2017 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Sale Order Invoicing Finished Task",
    "summary": "Control invoice order lines if his task has been finished",
    "version": "10.0.1.0.1",
    "category": "Sales",
    "website": "https://github.com/OCA/sale-workflow",
    "author": "Tecnativa, "
              "Camptocamp, "
              "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "sale_timesheet",
    ],
    "data": [
        "views/product_view.xml",
        "views/project_view.xml",
    ],
}
