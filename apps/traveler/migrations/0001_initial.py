# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Country'
        db.create_table('traveler_country', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('latitude', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('longitude', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
        ))
        db.send_create_signal('traveler', ['Country'])

        # Adding model 'Trip'
        db.create_table('traveler_trip', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=120, null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=120)),
        ))
        db.send_create_signal('traveler', ['Trip'])

        # Adding M2M table for field countries on 'Trip'
        db.create_table('traveler_trip_countries', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trip', models.ForeignKey(orm['traveler.trip'], null=False)),
            ('country', models.ForeignKey(orm['traveler.country'], null=False))
        ))
        db.create_unique('traveler_trip_countries', ['trip_id', 'country_id'])

    def backwards(self, orm):
        # Deleting model 'Country'
        db.delete_table('traveler_country')

        # Deleting model 'Trip'
        db.delete_table('traveler_trip')

        # Removing M2M table for field countries on 'Trip'
        db.delete_table('traveler_trip_countries')

    models = {
        'traveler.country': {
            'Meta': {'object_name': 'Country'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'})
        },
        'traveler.trip': {
            'Meta': {'object_name': 'Trip'},
            'countries': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['traveler.Country']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['traveler']