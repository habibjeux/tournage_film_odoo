from odoo import models, fields, api
from datetime import date

class Realisateur(models.Model):
    _name = 'tournage_film.realisateur'
    _description = 'Réalisateur'

    name = fields.Char(string='Nom', required=True)
    film_ids = fields.One2many('tournage_film.film', 'realisateur_id', string='Films réalisés')
    nombre_films = fields.Integer(string='Nombre de films réalisés', compute='_compute_nombre_films', store=True)
    sexe = fields.Selection([('homme', 'Homme'), ('femme', 'Femme'), ('autre', 'Autre')], string='Sexe')
    situation_matrimoniale = fields.Selection([
        ('celibataire', 'Célibataire'),
        ('marie', 'Marié(e)'),
        ('divorce', 'Divorcé(e)'),
        ('veuf', 'Veuf/Veuve')
    ], string='Situation matrimoniale')
    date_naissance = fields.Date(string='Date de naissance')
    age = fields.Integer(string='Âge', compute='_compute_age', store=True)

    @api.depends('film_ids')
    def _compute_nombre_films(self):
        for realisateur in self:
            realisateur.nombre_films = len(realisateur.film_ids)

    @api.depends('date_naissance')
    def _compute_age(self):
        today = date.today()
        for realisateur in self:
            if realisateur.date_naissance:
                age = today.year - realisateur.date_naissance.year - ((today.month, today.day) < (realisateur.date_naissance.month, realisateur.date_naissance.day))
                realisateur.age = age
            else:
                realisateur.age = 0