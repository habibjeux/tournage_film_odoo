from odoo import models, fields, api

class Film(models.Model):
    _name = 'tournage_film.film'
    _description = 'Film'

    name = fields.Char(string='Nom', required=True)
    date_sortie = fields.Date(string='Date de sortie')
    duree = fields.Float(string='Durée (en heures)')
    realisateur_id = fields.Many2one('tournage_film.realisateur', string='Réalisateur')
    lieu_id = fields.Many2one('tournage_film.lieu', string='Lieu de tournage')
    societe_production_id = fields.Many2one('tournage_film.societe_production', string='Maison de production')
    type_film = fields.Selection([
        ('action', 'Action'),
        ('comedie', 'Comédie'),
        ('drame', 'Drame'),
        ('science_fiction', 'Science-fiction'),
        ('autre', 'Autre')
    ], string='Type de film')
    taille = fields.Float(string='Taille (en Go)')
    prix_vente = fields.Float(string='Prix de vente')

    tournage_ids = fields.One2many('tournage_film.tournage', 'film_id', string='Tournages')