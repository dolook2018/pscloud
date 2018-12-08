from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
import datetime
from odoo.tools import DEFAULT_SERVER_DATE_FORMAT as DATE_FORMAT

class TrainingLesson(models.Model):
    _name = 'pscloud.training.classroom'
    _description = "教室"
    name = fields.Char(string='房间号')
    seats= fields.Integer(string='座位数')
    areasize = fields.Integer(string ='教室面积')


    state = fields.Selection([('draft', '未启用'), ('vaild', '启用'), ], string='状态', readonly=True, copy=False, index=True,default='draft')

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', '房间号必须唯一.')
    ]

    @api.multi
    def action_confirm(self):
        return self.write({'state': 'vaild'})