from odoo import models, fields, api

class Lieu(models.Model):
    _name = 'tournage_film.lieu'
    _description = 'Lieu de tournage'

    name = fields.Char(string='Nom', required=True)
    film_ids = fields.One2many('tournage_film.film', 'lieu_id', string='Films tournés')
    nombre_films = fields.Integer(string='Nombre de films tournés', compute='_compute_nombre_films', store=True)

    @api.depends('film_ids')
    def _compute_nombre_films(self):
        for lieu in self:
            lieu.nombre_films = len(lieu.film_ids)