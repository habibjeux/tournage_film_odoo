from odoo import models, fields, api

class Tournage(models.Model):
    _name = 'tournage_film.tournage'
    _description = 'Tournage'

    name = fields.Char(string='Numéro de tournage', required=True)
    date_debut = fields.Date(string='Date de début')
    date_fin = fields.Date(string='Date de fin')
    duree_tournage = fields.Float(string='Durée du tournage (en jours)', compute='_compute_duree_tournage', store=True)
    film_id = fields.Many2one('tournage_film.film', string='Film tourné')

    @api.depends('date_debut', 'date_fin')
    def _compute_duree_tournage(self):
        for tournage in self:
            if tournage.date_debut and tournage.date_fin:
                delta = tournage.date_fin - tournage.date_debut
                tournage.duree_tournage = delta.days + 1
            else:
                tournage.duree_tournage = 0