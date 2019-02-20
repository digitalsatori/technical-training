from odoo import models, fields

class Books(models.Model):
    _description= 'Library Books'
    _name = 'library.books'
    
    name = fields.Char(string="Name")
    ISBN = fields.Char(String="ISBN")
    publish_date = fields.Date(string="Publish Date")
    book_type = fields.Selection(selection=[('hard', 'Hard Cover'), ('soft', 'Soft Cover')], string="Book Type")