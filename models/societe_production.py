from odoo import models, fields, api

class SocieteProduction(models.Model):
    _name = 'tournage_film.societe_production'
    _description = 'Société de production'

    name = fields.Char(string='Nom', required=True)
    film_ids = fields.One2many('tournage_film.film', 'societe_production_id', string='Films produits')
    nombre_films = fields.Integer(string='Nombre de films produits', compute='_compute_nombre_films', store=True)
    capital = fields.Float(string='Capital')

    @api.depends('film_ids')
    def _compute_nombre_films(self):
        for societe in self:
            societe.nombre_films = len(societe.film_ids)