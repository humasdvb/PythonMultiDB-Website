class MyRouter(object):
        """
        A router to control all database operations on models in the
        auth application.
        """
        def db_for_read(self, model, **hints):
            """
            Attempts to read auth models go to auth_db.
            """
            if model._meta.app_label == 'animal':
                return 'animals'
            return None

        def db_for_write(self, model, **hints):
            """
            Attempts to write auth models go to auth_db.
            """
            if model._meta.app_label == 'animal':
                return 'animals'
            return None

        def allow_relation(self, obj1, obj2, **hints):
            """
            Allow relations if a model in the auth app is involved.
            """
            if obj1._meta.app_label == 'animal' or \
               obj2._meta.app_label == 'animal':
               return True
            return None

        def allow_migrate(self, db, app_label, model_name=None, **hints):
        
            if app_label == 'animal':
                return db == 'animals'
            return None

class OtherRouter(object):
        def db_for_read(self, model, **hints):
            """
            Reads go to a randomly-chosen replica.
            """
            return 'persons'

        def db_for_write(self, model, **hints):
            """
            Writes always go to primary.
            """
            return 'persons'

        def allow_relation(self, obj1, obj2, **hints):
            """
            Relations between objects are allowed if both objects are
            in the primary/replica pool.
            """
            db_list = ('persons', 'animals')
            if obj1._state.db in db_list and obj2._state.db in db_list:
                return True
            return None

        def allow_migrate(self, db, app_label, model_name=None, **hints):
       
                 return True