from django.db import models

class Equipe(models.Model):
    idequipe = models.AutoField(db_column='IDEquipe', primary_key=True)  # Field name made lowercase.
    nomequipe = models.TextField(db_column='NomEquipe')  # Field name made lowercase.
    refcoach = models.ForeignKey('Coach', models.DO_NOTHING, db_column='RefCoach')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'equipe'


class Coach(models.Model):
    idcoach = models.AutoField(db_column='IDCoach', primary_key=True)  # Field name made lowercase.
    nomcoach = models.TextField(db_column='NomCoach')  # Field name made lowercase.
    prenomcoach = models.TextField(db_column='PrenomCoach')  # Field name made lowercase.
    agecoach = models.IntegerField(db_column='AgeCoach')  # Field name made lowercase.
    motdepasse = models.TextField(db_column='MotDePasse')  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'coach'


class Joueur(models.Model):
    idjoueur = models.AutoField(db_column='IDJoueur', primary_key=True)  # Field name made lowercase.
    nomjoueur = models.TextField(db_column='NomJoueur')  # Field name made lowercase.
    prenomjoueur = models.TextField(db_column='PrenomJoueur')  # Field name made lowercase.
    refposte = models.ForeignKey('Poste', models.DO_NOTHING, db_column='refPoste')  # Field name made lowercase.
    refrole = models.ForeignKey('Role', models.DO_NOTHING, db_column='refRole')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'joueur'

class Role(models.Model):
    idrole = models.AutoField(db_column='IDRole', primary_key=True)  # Field name made lowercase.
    nomrole = models.TextField(db_column='NomRole')  # Field name made lowercase.
    descriptionrole = models.TextField(db_column='DescriptionRole')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role'

class Poste(models.Model):
    idposte = models.AutoField(db_column='IDPoste', primary_key=True)  # Field name made lowercase.
    nomposte = models.TextField(db_column='NomPoste')  # Field name made lowercase.
    descriptionposte = models.TextField(db_column='DescriptionPoste')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'poste'


class Stats(models.Model):
    idstats = models.AutoField(db_column='IDStats', primary_key=True)  # Field name made lowercase.
    refjoueur = models.ForeignKey('Joueur', models.DO_NOTHING, db_column='refJoueur')  # Field name made lowercase.
    nbmatchs = models.IntegerField(db_column='nbMatchs')  # Field name made lowercase.
    buts = models.IntegerField()
    passed = models.IntegerField(db_column='passeD')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'stats'

class Tactique(models.Model):
    idtactique = models.AutoField(db_column='IdTactique', primary_key=True)
    nom = models.TextField(db_column='Nom')  # Changé de IntegerField à TextField
    refequipe = models.ForeignKey(Equipe, models.DO_NOTHING, db_column='refEquipe')

    class Meta:
        managed = False
        db_table = 'tactique'


class PositionJoueur(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    reftactique = models.ForeignKey('Tactique', models.DO_NOTHING, db_column='RefTactique')  # Field name made lowercase.
    refjoueur = models.ForeignKey(Joueur, models.DO_NOTHING, db_column='RefJoueur')  # Field name made lowercase.
    positionx = models.FloatField(db_column='PositionX')  # Field name made lowercase.
    positiony = models.FloatField(db_column='PositionY')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'position_joueur'
