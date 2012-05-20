# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Trip.tag_line'
        db.add_column('traveler_trip', 'tag_line',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Trip.synopsis'
        db.add_column('traveler_trip', 'synopsis',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Trip.content'
        db.add_column('traveler_trip', 'content',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Trip.date_left'
        db.add_column('traveler_trip', 'date_left',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Trip.date_returned'
        db.add_column('traveler_trip', 'date_returned',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field locations on 'Trip'
        db.create_table('traveler_trip_locations', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trip', models.ForeignKey(orm['traveler.trip'], null=False)),
            ('location', models.ForeignKey(orm['locations.location'], null=False))
        ))
        db.create_unique('traveler_trip_locations', ['trip_id', 'location_id'])

        # Adding M2M table for field images on 'Trip'
        db.create_table('traveler_trip_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trip', models.ForeignKey(orm['traveler.trip'], null=False)),
            ('image', models.ForeignKey(orm['gallery.image'], null=False))
        ))
        db.create_unique('traveler_trip_images', ['trip_id', 'image_id'])


    def backwards(self, orm):
        # Deleting field 'Trip.tag_line'
        db.delete_column('traveler_trip', 'tag_line')

        # Deleting field 'Trip.synopsis'
        db.delete_column('traveler_trip', 'synopsis')

        # Deleting field 'Trip.content'
        db.delete_column('traveler_trip', 'content')

        # Deleting field 'Trip.date_left'
        db.delete_column('traveler_trip', 'date_left')

        # Deleting field 'Trip.date_returned'
        db.delete_column('traveler_trip', 'date_returned')

        # Removing M2M table for field locations on 'Trip'
        db.delete_table('traveler_trip_locations')

        # Removing M2M table for field images on 'Trip'
        db.delete_table('traveler_trip_images')


    models = {
        'gallery.image': {
            'Meta': {'object_name': 'Image'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'locations.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'default_location': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'})
        },
        'traveler.country': {
            'Meta': {'object_name': 'Country'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'})
        },
        'traveler.trip': {
            'Meta': {'object_name': 'Trip'},
            'content': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'countries': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['traveler.Country']", 'null': 'True', 'blank': 'True'}),
            'date_left': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_returned': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['gallery.Image']", 'null': 'True', 'blank': 'True'}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['locations.Location']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '120'}),
            'synopsis': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'tag_line': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '120', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['traveler']