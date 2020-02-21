# -*- coding: utf-8 -*-
# from odoo import http


# class Estudio(http.Controller):
#     @http.route('/estudio/estudio/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estudio/estudio/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('estudio.listing', {
#             'root': '/estudio/estudio',
#             'objects': http.request.env['estudio.estudio'].search([]),
#         })

#     @http.route('/estudio/estudio/objects/<model("estudio.estudio"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estudio.object', {
#             'object': obj
#         })
