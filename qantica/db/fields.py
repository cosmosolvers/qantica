from typing import (
    List,
    Dict,
    Any,
    Union,
    Tuple,
    Optional
)


class Field:
    
    value = None
    
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        auto_created: bool=False, # definit comme etant cree automatiquement
        auto_updated: bool=False, # definit comme etant mis a jour automatiquement
        auto_incr: bool=False, # definit comme etant incrementer automatiquement
        choices: Tuple=None, # definit une liste de choix possibles *
        max_length: int=None, # definit une longueur maximale
        min_length: int=None, # definit une longueur minimale
        max_value: Any=None, # definit une valeur maximale
        min_value: Any=None, # definit une valeur minimale
        validators=None, # definit une liste de validateurs
        error_messages=None, # definit une liste de messages d'erreurs
        max_digits: int=None, # definit le nombre de chiffres maximum
        decimal_places: int=None, # definit le nombre de decimales
        power_of_ten: int=None, # definit la puissance de 10
        encoding: str=None, # definit un encodage
        editable: bool=True, # definit comme editable *
        on_delete: str=None, # definit une action a effectuer lors de la suppression
        on_update: str=None, # definit une action a effectuer lors de la mise a jour
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_check=None, # definit une contrainte de verification
        db_default=None, # definit une valeur par defaut *
        db_auto_updated=False, # definit comme etant mis a jour automatiquement
        db_auto_created=False, # definit comme etant cree automatiquement
        db_choices=None, # definit une liste de choix possibles *
        db_max_length=None, # definit une longueur maximale
        db_min_length=None, # definit une longueur minimale
        db_max_value=None, # definit une valeur maximale
        db_min_value=None, # definit une valeur minimale
        db_validators=None, # definit une liste de validateurs
        db_error_messages=None # definit une liste de messages d'erreurs
    ):
        pass
    
    def __get__(self, instance, owner):
        return self.value
    
    def __set__(self, instance, value):
        self.value = value
    
    def __delete__(self, instance):
        del self.value


class IntegerField(Field):
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()
    
    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise ValueError('Value must be an integer')
        super().__set__(instance, value)


class DecimalField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()
    


class FloatField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()
    


class CharField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()
    


class TextField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()
    

class DateField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()
    

class DateTimeField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()
    

class TimeField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()
    


class TimeStampField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()
    

class BooleanField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class BinaryField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class EnumField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class JsonField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class UUIDField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class HTMLField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class CallableField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class ArrayField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class GeoSpatialField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class IPaddressField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class CurrencyField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class URLField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class PhoneField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class EmailField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class ImageField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class MediaField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class AudioField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class GenomicField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class DateTimeOffSetField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class IntervallField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()


class ScriptField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class GPSLocationField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()


class MeasureField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()


class TokenField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()


class PasswordField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()


class HashField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()


class QRCodeField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()


class PercentField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class ColorField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class FileField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class MapField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class SETField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class DocumentField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class SymbolField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class VersionField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class MappingField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class GEOHashField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class QueueField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class CounterField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class SensorField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class LOGField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class Polygon:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class OneToOneField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class OneToManyField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class ManyToOneField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class ManyToManyField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class TreeField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class GraphField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class PolymorphicField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class TemporalField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class SpatialField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class AggregationField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class VersionningField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class DependencyField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class SematicField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class OpinionField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class ChronologicalField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()

class GeographicalField:
    def __init__(
        self,
        primary_key: bool=False, # definit comme cle primaire *
        unique: bool=False, # definit comme unique *
        null: bool=False, # definit comme pouvant etre null *
        blank: bool=False, # definit comme pouvant etre vide *
        default: Any=None, # definit une valeur par defaut *
        choices: Tuple=None, # definit une liste de choix possibles *
        editable: bool=True, # definit comme editable *
        db_column=None, # definit le nom de la colonne en base de donnees *
        db_index=False, # definit comme indexe *
        db_unique=False, # definit comme unique *
        db_primary_key=False, # definit comme cle primaire *
        db_foreign_key=None, # definit comme cle etrangere *
        db_default=None, # definit une valeur par defaut *
        db_choices=None, # definit une liste de choix possibles *
    ):
        super().__init__()
