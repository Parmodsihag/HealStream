import sqlite3

def connect_to_database(db_file):
    """Connects to a SQLite3 database."""
    try:
      conn = sqlite3.connect(db_file)
      return conn
    except sqlite3.Error as err:
      print("Error connecting to database:", err)
      return None

conn = connect_to_database("databases//mydb.db")

def execute_query(sql, params=(), conn=conn):
    """Executes a query with optional parameters."""
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()
    return cursor

def fetch_all(cursor):
    """Fetches all rows from the cursor."""
    return cursor.fetchall()

def fetch_one(cursor):
    """Fetches a single row from the cursor."""
    return cursor.fetchone()

def close_database_connection(conn=conn):
    """Closes the connection to the database."""
    if conn:
      conn.close()

def close_database_connection(conn= conn):
    """Closes the connection to the database."""
    if conn:
      conn.close()

def create_tables(conn= conn):
    """Creates tables if they don't exist."""
    patients_table = """
    CREATE TABLE IF NOT EXISTS Patients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER,
        sex TEXT NOT NULL,
        address TEXT NOT NULL,
        mobile_number TEXT NOT NULL,
        guardian TEXT NOT NULL
    )
    """
    departments_table = """
    CREATE TABLE IF NOT EXISTS Departments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """
    doctors_table = """
    CREATE TABLE IF NOT EXISTS Doctors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department_id INTEGER REFERENCES Departments(id)
    )
    """
    opd_slips_table = """
    CREATE TABLE IF NOT EXISTS OPD_Slips (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER REFERENCES Patients(id),
        doctor_id INTEGER REFERENCES Doctors(id),
        slip_date TEXT NOT NULL,
        valid_upto TEXT NOT NULL,
        amount INTEGER,
        UHID_NO TEXT NOT NULL
    )
    """
    cursor = execute_query(patients_table)
    cursor = execute_query(departments_table)
    cursor = execute_query(doctors_table)
    cursor = execute_query(opd_slips_table)
# Patient Functions

def create_patient(name, age, sex, address, mobile_number, guardian):
    """Inserts a new patient record."""
    sql = "INSERT INTO Patients (name, age, sex, address, mobile_number, guardian) VALUES (?, ?, ?, ?, ?, ?)"
    params = (name, age, sex, address, mobile_number, guardian)
    cursor = execute_query(sql, params)
    return cursor.lastrowid  # Get the ID of the inserted row

def get_patient_by_id(patient_id, conn=conn):
    """Retrieves a patient record by ID."""
    sql = "SELECT * FROM Patients WHERE id = ?"
    params = (patient_id,)
    cursor = execute_query(sql, params)
    return fetch_one(cursor)

def get_all_patients(conn=conn):
    """Retrieves all patient records."""
    sql = "SELECT * FROM Patients"
    cursor = execute_query(sql)
    return fetch_all(cursor)

# Department Functions

def create_department(name, conn=conn):
    """Inserts a new department record."""
    sql = "INSERT INTO Departments (name) VALUES (?)"
    params = (name,)
    execute_query(sql, params)

def get_department_by_id(department_id):
    """Retrieves a department record by ID."""
    sql = "SELECT * FROM Departments WHERE id = ?"
    params = (department_id,)
    cursor = execute_query(sql, params)
    return fetch_one(cursor)

def get_all_departments():
    """Retrieves all department records."""
    sql = "SELECT * FROM Departments"
    cursor = execute_query(sql)
    return fetch_all(cursor)

# Doctor Functions

def create_doctor(name, department_id, conn=conn):
    """Inserts a new doctor record."""
    sql = "INSERT INTO Doctors (name, department_id) VALUES (?, ?)"
    params = (name, department_id)
    execute_query(sql, params)

def get_doctor_by_id(doctor_id, conn=conn):
    """Retrieves a doctor record by ID."""
    sql = "SELECT * FROM Doctors WHERE id = ?"
    params = (doctor_id,)
    cursor = execute_query(sql, params)
    return fetch_one(cursor)

def get_doctors_by_department(department_id, conn=conn):
    """Retrieves all doctors associated with a department."""
    sql = "SELECT * FROM Doctors WHERE department_id = ?"
    params = (department_id,)
    cursor = execute_query(sql, params)
    return fetch_all(cursor)

# OPD Slip Functions

def create_opd_slip(patient_id, doctor_id, department_id, date_time, symptoms, conn=conn):
    """Inserts a new OPD slip record."""
    sql = """
    INSERT INTO OPD_Slips (patient_id, doctor_id, department_id, date_time, symptoms)
    VALUES (?, ?, ?, ?, ?)
    """
    params = (patient_id, doctor_id, department_id, date_time, symptoms)
    execute_query(sql, params)

def get_opd_slip_by_id(opd_slip_id, conn=conn):
    """Retrieves an OPD slip record by ID."""
    sql = "SELECT * FROM OPD_Slips WHERE id = ?"
    params = (opd_slip_id,)
    cursor = execute_query( sql, params)
    return fetch_one(cursor)

def get_opd_slips_by_patient(patient_id, conn=conn):
    """Retrieves all OPD slips for a specific patient."""
    sql = "SELECT * FROM OPD_Slips WHERE patient_id = ?"
    params = (patient_id,)
    cursor = execute_query( sql, params)
    return fetch_all(cursor)

# Additional OPD Slip Functions (consider adding these if needed)

# def update_opd_slip_diagnosis(conn, opd_slip_id, diagnosis):
#   """Updates the diagnosis for an OPD slip."""
#   sql = "UPDATE OPD_Slips SET diagnosis = ? WHERE id = ?"
#   params = (diagnosis, opd_slip_id)
#   execute_query(conn, sql, params)

# def update_opd_slip_prescription(conn, opd_slip_id, prescription):
#   """Updates the prescription for an OPD slip."""
#   sql = "UPDATE OPD_Slips SET prescription = ? WHERE id = ?"
#   params = (prescription, opd_slip_id)
#   execute_query(conn, sql, params)

create_tables(conn)

# if __name__ == "__main__":
    # print('hello world')