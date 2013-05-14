# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing unique constraint on 'CartItem', fields ['product_type', 'product_id', 'cart']
        db.delete_unique(u'fastcart_cartitem', ['product_type_id', 'product_id', 'cart_id'])

        # Deleting field 'CartItem.product_type'
        db.delete_column(u'fastcart_cartitem', 'product_type_id')

        # Deleting field 'CartItem.product_id'
        db.delete_column(u'fastcart_cartitem', 'product_id')

        # Adding field 'CartItem.products'
        db.add_column(u'fastcart_cartitem', 'products',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['product.Book']),
                      keep_default=False)

        # Adding unique constraint on 'CartItem', fields ['products', 'cart']
        db.create_unique(u'fastcart_cartitem', ['products_id', 'cart_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'CartItem', fields ['products', 'cart']
        db.delete_unique(u'fastcart_cartitem', ['products_id', 'cart_id'])


        # User chose to not deal with backwards NULL issues for 'CartItem.product_type'
        raise RuntimeError("Cannot reverse this migration. 'CartItem.product_type' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'CartItem.product_id'
        raise RuntimeError("Cannot reverse this migration. 'CartItem.product_id' and its values cannot be restored.")
        # Deleting field 'CartItem.products'
        db.delete_column(u'fastcart_cartitem', 'products_id')

        # Adding unique constraint on 'CartItem', fields ['product_type', 'product_id', 'cart']
        db.create_unique(u'fastcart_cartitem', ['product_type_id', 'product_id', 'cart_id'])


    models = {
        u'account.customuser': {
            'Meta': {'object_name': 'CustomUser'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'date_of_birth': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75', 'db_index': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'm_username': ('django.db.models.fields.CharField', [], {'max_length': '125', 'null': 'True', 'blank': 'True'}),
            'mobile_phone': ('django.db.models.fields.CharField', [], {'max_length': '13', 'null': 'True', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['custom_sites.Site']", 'symmetrical': 'False'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'custom_sites.site': {
            'Meta': {'object_name': 'Site'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'fastcart.cart': {
            'Meta': {'object_name': 'Cart'},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['account.CustomUser']", 'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'fastcart.cartitem': {
            'Meta': {'ordering': "['-created_on']", 'unique_together': "(('cart', 'products'),)", 'object_name': 'CartItem'},
            'cart': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'items'", 'to': u"orm['fastcart.Cart']"}),
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'products': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Book']"}),
            'quantity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1'})
        },
        u'product.author': {
            'Meta': {'object_name': 'Author'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'mssql_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'slug': ('django_autoslug.fields.AutoSlugField', [], {'null': 'True', 'recursive': 'False', 'populate_from': "('first_name', 'last_name')", 'max_length': '255', 'blank': 'True', 'unique': 'True'})
        },
        u'product.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'authors'", 'symmetrical': 'False', 'through': u"orm['product.BookAuthor']", 'to': u"orm['product.Author']"}),
            'binding': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.KnsCategory']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Currency']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['product.Genre']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'isbn': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'mssql_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'original_title': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'page_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'paper': ('django.db.models.fields.CharField', [], {'max_length': '1', 'null': 'True', 'blank': 'True'}),
            'periodical': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '7', 'decimal_places': '2'}),
            'publication_month': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'publication_year': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True', 'max_length': '4', 'null': 'True', 'blank': 'True'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Publisher']"}),
            'rating_score': ('django.db.models.fields.IntegerField', [], {'default': '0', 'blank': 'True'}),
            'rating_votes': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0', 'blank': 'True'}),
            'serie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.BookSerie']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django_autoslug.fields.AutoSlugField', [], {'max_length': '400', 'populate_from': "('title', 'publisher')", 'recursive': 'False', 'blank': 'True'}),
            'stock': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'tax': ('django.db.models.fields.PositiveIntegerField', [], {'default': '8'}),
            'temporary_discount': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'temporary_discount_finish': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'temporary_discount_start': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'view_count': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '7', 'decimal_places': '2', 'blank': 'True'})
        },
        u'product.bookauthor': {
            'Meta': {'unique_together': "(('book', 'author'),)", 'object_name': 'BookAuthor'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Author']"}),
            'book': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Book']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mission': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        u'product.bookserie': {
            'Meta': {'object_name': 'BookSerie'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mssql_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['product.Publisher']"}),
            'slug': ('django_autoslug.fields.AutoSlugField', [], {'max_length': '400', 'populate_from': "('publisher', 'name')", 'recursive': 'False', 'blank': 'True'})
        },
        u'product.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mssql_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'})
        },
        u'product.genre': {
            'Meta': {'object_name': 'Genre'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '127'}),
            'slug': ('django_autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "('name',)", 'recursive': 'False', 'blank': 'True'})
        },
        u'product.knscategory': {
            'Meta': {'object_name': 'KnsCategory'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'mssql_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('mptt.fields.TreeForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': u"orm['product.KnsCategory']"}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'uslug': ('django_autoslug.fields.AutoSlugField', [], {'null': 'True', 'recursive': 'False', 'populate_from': "('name',)", 'max_length': '255', 'blank': 'True', 'unique': 'True'})
        },
        u'product.publisher': {
            'Meta': {'object_name': 'Publisher'},
            'discount': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mssql_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20', 'db_index': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django_autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '127', 'populate_from': "('name',)", 'recursive': 'False', 'blank': 'True'})
        }
    }

    complete_apps = ['fastcart']