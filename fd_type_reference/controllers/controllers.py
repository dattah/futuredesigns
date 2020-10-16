# -*- coding: utf-8 -*-
# from odoo import http


# class FdTypeReference(http.Controller):
#     @http.route('/fd_type_reference/fd_type_reference/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fd_type_reference/fd_type_reference/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fd_type_reference.listing', {
#             'root': '/fd_type_reference/fd_type_reference',
#             'objects': http.request.env['fd_type_reference.fd_type_reference'].search([]),
#         })

#     @http.route('/fd_type_reference/fd_type_reference/objects/<model("fd_type_reference.fd_type_reference"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fd_type_reference.object', {
#             'object': obj
#         })
