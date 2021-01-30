import sqlite3


def connection_db(func):
    def wrapper(*args, **kwargs):
        connection = sqlite3.connect('bot_db.db')
        cursor = connection.cursor()

        result = func(*args, cursor)
        connection.commit()

        cursor.close()
        connection.close()

        return result

    return wrapper


@connection_db
def get_start_users(cursor=None):
    num_users = 0
    try:
        cursor.execute('SELECT COUNT(*) FROM users')
        num_users = cursor.fetchone()[0]
    except Exception as e:
        num_users = False
        print(e)
    finally:
        return num_users


@connection_db
def insert_user(id, name, cursor=None):
    response = True
    try:
        cursor.execute('INSERT INTO users VALUES (?, ?)', (id, name))
    except Exception as e:
        response = False
        print(e)
    finally:
        return response


@connection_db
def update_delay(id, delay, cursor=None):
    response = True
    try:
        cursor.execute('UPDATE delays SET delay = ? WHERE id = ?', (delay, id))
    except Exception as e:
        response = False
        print(e)
    finally:
        return response


@connection_db
def get_delay(id, cursor=None):
    result = None
    try:
        cursor.execute('SELECT delay FROM delays WHERE id = ?', (id,))
        result = cursor.fetchone()[0]
    except Exception as e:
        result = False
        print(e)
    finally:
        return result


@connection_db
def update_score(id, result, cursor=None):
    response = True
    try:
        if result == 'eagle':
            cursor.execute('UPDATE statistic SET score = (score + 1), eagle = eagle + 1 WHERE id = ?', (id,))
        else:
            cursor.execute('UPDATE statistic SET score = (score + 1), tail = tail + 1  WHERE id = ?', (id,))
    except Exception as e:
        response = False
        print(e)
    finally:
        return response

@connection_db
def get_statistic(id, cursor=None):
    result = None
    try:
        cursor.execute(
            '''
            SELECT 
                users.name,
                statistic.score,
                statistic.eagle,
                statistic.tail
            FROM
                statistic, users
            WHERE
                users.id = ?
            ''', (id,))
        result = cursor.fetchall()
    except Exception as e:
        result = False
        print(e)
    finally:
        return result
