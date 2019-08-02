# -*- coding: utf-8 -*-

from odoo import models, fields, api

class erreur(models.Model):
    _name = 'projectgi.erreur'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()


class ProjectTask(models.Model):
    _inherit = 'project.task'
    instructor = fields.Boolean("Instructor", default=False)

