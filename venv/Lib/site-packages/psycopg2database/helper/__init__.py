def insert_record(*k, **p):
    raise Exception('It works!')

import psycopg2

def psycopg2UnicodeFetch(encoding):
    def psycopg2UnicodeFetch_converter(conversion, state=None):
        """\

        Convert the results of a cursor fetch to the correct format.
    
        The ``conversion.value.cursor.description`` argument contains
        information about each value returned in the form of a 7-item tuple:
        ``(name, type_code, display_size, internal_size, precision, scale,
        null_ok)``. The ``.description`` attribute will be ``None`` for
        operations which do not return rows.
    
        The ``type_code`` will be different for each driver.

        """
        cursor = conversion.value.cursor
        rows = conversion.value.result
    
        if cursor.description is None:
            conversion.result = result
        else:
            new_rows = []
            for row in rows:
                new_row = []
                for i, value in enumerate(row):
                    if value is not None and cursor.description[i][1] == psycopg2.STRING:
                        new_row.append(value.decode(encoding))
                    else:
                        new_row.append(value)
                new_rows.append(tuple(new_row))
            conversion.result = tuple(new_rows)
    return psycopg2UnicodeFetch_converter

psycopg2_utf8_fetch = psycopg2UnicodeFetch('utf8')

def postgresql_insert_record(
    connection, 
    table_name, 
    data_dict, 
    primary_key_column_name=None,
    database=None,
):
    """\
    Implementation of ``insert_record()`` for PostgreSQL. See 
    ``insert_record()`` for details.
    """
    cursor = connection.cursor()
    columns = []
    values = []
    for k, v in data_dict.items():
        values.append(v)
        columns.append(k)
    values_str = ""
    for value in values:
        values_str += "%s, "
    values_str = values_str[:-2]

    if primary_key_column_name is not None:
        # This should try determine the type of database
        cursor.execute(
            """SELECT nextval(%s)""", 
            ('"'+table_name+'_%s_seq"'%primary_key_column_name,)
        )
        uid = cursor.fetchall()[0][0]
        values_str += ', %s'
        values.append(uid)
        columns.append(primary_key_column_name)
    
    if primary_key_column_name and data_dict.has_key(primary_key_column_name):
        raise Exception(
            "You shouldn't specify the primary key in the data_dict, "
            "the new value will be returned automatically if you specify "
            "primary_key_column_name"
        )
    sql = """
        INSERT INTO %s (%s) VALUES (%s);
    """ % (
        table_name,
        ', '.join(['"%s"'%col for col in columns]),
        values_str
    )
    cursor.execute(sql, tuple(values))
    cursor.close()
    if primary_key_column_name is not None:
        return uid 
    return None


def dbport(conversion, flow): 
    values = conversion.value.copy()
    if not values.get('port'):
        port = {
            '': None,
            'MySQLdb.connect' : u'6603',
            'psycopg2.connect' : u'5432',
            'psycopg.connect' : u'5432',
        }.get(
            values.get('creator', ''), 
            None
        )
        if port is not None:
            values['port'] = port
    conversion.result = values

def psycopg2_update_config(flow, name, config):
    from configconvert import handle_option_error, handle_section_error
    from stringconvert import unicodeToUnicode, unicodeToInteger,\
       unicodeToBoolean
    from recordconvert import toRecord
    from configconvert import stringToObject
    from conversionkit import Conversion, chainConverters

    # Re-use the converters   
    unicode_to_integer = unicodeToInteger()
    null = unicodeToUnicode()

    database_config = chainConverters(
        dbport,
        toRecord(
            missing_defaults=dict(
                creator=psycopg2.connect,
                fetch_converter=psycopg2_utf8_fetch,
                execute_converter=None,
            ),
            missing_or_empty_errors = dict(
                database="The required option '%s.database' is missing"%(name,),
            ),
            converters=dict(
                database = null,
                user = null,
                # Could use formencode.validators.URL() for host?
                host = null,
                password = null,
                port = unicode_to_integer,

                creator = stringToObject(),
                fetch_converter = stringToObject(),
                execute_converter = stringToObject(),
            ),
            # Keep the pool options as they are
            filter_extra_fields = False
        ),
    )
    conversion = Conversion(config).perform(database_config)
    if not conversion.successful:
        handle_option_error(conversion, name)
    else:
        config = conversion.result
    return config

update_config = psycopg2_update_config

