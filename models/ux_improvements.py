# returns a list of column names which are more ux friendly


def ux_friendly_cols():
    return ['transaction_id',
            'price_paid',
            'deed_date',
            'postcode',
            'property_type',
            'new_build',
            'estate_type',
            'door_no1',
            'door_no2',
            'street',
            'locality',
            'town',
            'local_authority',
            'county',
            'category_type',
            'record_status']


def ux_friendly_cols_relevant():
    return ['transaction_id',
            'price_paid',
            'deed_date',
            'postcode',
            'property_type',
            'new_build',
            'estate_type',
            'locality',
            'town',
            'local_authority',
            'county', ]


def ux_friendly_prop_type_names():
    return {
        'S': 'Semi',
        'D': 'Detached',
        'T': 'Terrace',
        'F': 'Flat',
        'O': 'Other'
    }
