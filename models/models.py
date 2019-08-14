# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime as dt
import dateutil.parser

datetimeFormat = '%Y-%m-%d %H:%M:%S'


class erreur(models.Model):
    _name = 'projectgi.erreur'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()


class ProjectTask(models.Model):
    _inherit = 'project.task'

    date_import = fields.Datetime( readonly=True, select=True
                                , default=lambda self: fields.datetime.now())

    date_travail = fields.Datetime(string="Date debut")
    date_deadline = fields.Datetime(string="Date fin")
    duree = fields.Char(string="Durée", compute="_duration", store=True)

    @api.depends('date_travail','date_deadline')
    def _duration(self):

        if self.date_travail and self.date_deadline:

            for rec in self:
                init_date = dt.strptime(rec.date_travail, datetimeFormat)
                end_date = dt.strptime(rec.date_deadline, datetimeFormat)
                time = str((end_date - init_date).seconds)
                time = int(time)
                day = str((end_date - init_date).days)
                time = time % (24 * 3600)
                hour = time // 3600
                time %= 3600
                minutes = time // 60
                time %= 60
                seconds = time
                if int(day) == 0:
                    rec.duree = dt.strptime(str(hour) + ":" + str(minutes) + ":" + str(seconds), '%H:%M:%S').time()
                else:
                    td = dt.strptime( str(hour) + ":" + str(minutes)  + ":" +  str(seconds), '%H:%M:%S').time()
                    rec.duree = str(day) +" jours et " + str(td)


class rapport(models.Model):
    _name = 'projectgi.rapport'
    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    num_rapport = fields.Char("Rapport num")
    is_done = fields.Boolean()
    date_travail = fields.Datetime(string="Date debut")
    date_deadline = fields.Datetime(string="Date fin")
    duree = fields.Char(string="Durée", compute="_duration", store=True)



