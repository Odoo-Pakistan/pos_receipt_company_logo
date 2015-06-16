# -*- coding: utf-8 -*-
##############################################################################
#
#   Copyright (c) 2015- Vizucom Oy (http://www.vizucom.com)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Company Logo for POS Receipt',
    'category': 'Point of Sale',
    'version': '0.1',
    'author': 'Vizucom Oy',
    'website': 'http://www.vizucom.com',
    'depends': ['point_of_sale'],
    'description': """
Company Logo for POS Receipt
============================
 * Adds the company logo to the Point of Sale receipt

""",
    'qweb': [
        'static/src/xml/pos_ticket.xml',
    ],
    'data': [
        'views/assets.xml',
    ],
    
}
