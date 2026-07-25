import sqlite3


def init_db():

    conn = sqlite3.connect("database/requests.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS requests(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        case_id TEXT,

        request TEXT,

        type TEXT,

        urgency TEXT,

        confidence REAL,

        department TEXT,

        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()


def save_request(case_id,
                 request,
                 result,
                 workflow):

    conn = sqlite3.connect("database/requests.db")
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO requests
    (
        case_id,
        request,
        type,
        urgency,
        confidence,
        department,
        timestamp
    )
    VALUES (?,?,?,?,?,?,?)
    """,
    (
        case_id,
        request,
        result["type"],
        result["urgency"],
        result["confidence"],
        workflow["department"],
        workflow["timestamp"]
    ))

    conn.commit()
    conn.close()

def get_requests():

    conn = sqlite3.connect("database/requests.db")
    conn.row_factory = sqlite3.Row

    cur = conn.cursor()

    cur.execute("""
    SELECT *
    FROM requests
    ORDER BY id DESC
    """)

    rows = cur.fetchall()

    conn.close()

    return rows