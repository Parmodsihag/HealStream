import sqlite3
import datetime

db_file = "C://HealStream//data//healstream.db"

try:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

   

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
        opd_number INTEGER NOT NULL,
        patient_id INTEGER REFERENCES Patients(id),
        doctor_id INTEGER REFERENCES Doctors(id),
        slip_date TEXT NOT NULL,
        slip_time TEXT NOT NULL,
        valid_upto TEXT NOT NULL,
        amount INTEGER
    )
    """
    query = """
        CREATE UNIQUE INDEX IF NOT EXISTS opd_slip_unique_idx
        ON OPD_Slips (opd_number, slip_date)
    """

    
    cursor.execute(patients_table)
    cursor.execute(departments_table)
    cursor.execute(doctors_table)
    cursor.execute(opd_slips_table)
    cursor.execute(query)
    conn.commit()
 
except sqlite3.Error as err:
    print("Error connecting to database:", err)

def execute_query(sql, params=()):
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

def close_database_connection():
    """Closes the connection to the database."""
    if conn:
      conn.close()

def close_database_connection():
    """Closes the connection to the database."""
    if conn:
      conn.close()


# Patient Functions

def create_patient(name, age, sex, address, mobile_number, guardian):
    """Inserts a new patient record."""
    sql = "INSERT INTO Patients (name, age, sex, address, mobile_number, guardian) VALUES (?, ?, ?, ?, ?, ?)"
    params = (name, age, sex, address, mobile_number, guardian)
    cursor = execute_query(sql, params)
    return cursor.lastrowid  # Get the ID of the inserted row

def get_patient_by_id(patient_id):
    """Retrieves a patient record by ID."""
    sql = "SELECT * FROM Patients WHERE id = ?"
    params = (patient_id,)
    cursor = execute_query(sql, params)
    return fetch_one(cursor)

def get_all_patients():
    """Retrieves all patient records."""
    sql = "SELECT * FROM Patients"
    cursor = execute_query(sql)
    return fetch_all(cursor)

# Department Functions

def create_department(name):
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

def create_doctor(name, department_id):
    """Inserts a new doctor record."""
    sql = "INSERT INTO Doctors (name, department_id) VALUES (?, ?)"
    params = (name, department_id)
    execute_query(sql, params)

def get_doctor_by_id(doctor_id):
    """Retrieves a doctor record by ID."""
    sql = "SELECT * FROM Doctors WHERE id = ?"
    params = (doctor_id,)
    cursor = execute_query(sql, params)
    return fetch_one(cursor)

def get_doctors_by_department(department_id):
    """Retrieves all doctors associated with a department."""
    sql = "SELECT * FROM Doctors WHERE department_id = ?"
    params = (department_id,)
    cursor = execute_query(sql, params)
    return fetch_all(cursor)


def get_all_doctors():
    """Retrieves all Doctors records."""
    sql = "SELECT * FROM Doctors"
    cursor = execute_query(sql)
    return fetch_all(cursor)

# OPD Slip Functions
def get_opd_slip(opd_number, date):
    """
    Retrieves the OPD slip data for a given OPD number and date from the OPD_Slips table.
  
    Args:
        opd_number: The OPD number to search for.
        date: The date in dd-mm-yyyy format to search for.
  
    Returns:
        A tuple containing the OPD slip data, or None if not found.
    """
    cursor = conn.cursor()
    query = """
    SELECT *
    FROM OPD_Slips
    WHERE opd_number = ? AND slip_date = ?
    """
    cursor.execute(query, (opd_number, date))
    opd_slip = cursor.fetchone()
    return opd_slip
    


def check_opd_number_exists(opd_number, date):
    """
    This function checks if a given OPD number already exists for a specific date in the OPD_Slips table.
  
    Args:
        conn: A database connection object.
        opd_number: The OPD number to check.
        date: The date in dd-mm-yyyy format to check against.
  
    Returns:
        True if the OPD number exists for the given date, False otherwise.
    """
  
    cursor = conn.cursor()
  
    query = """
    SELECT COUNT(*)
    FROM OPD_Slips
    WHERE opd_number = ? AND slip_date = ?
    """
    # Execute the query with parameters
    cursor.execute(query, (opd_number, date))
  
    count = cursor.fetchone()[0]
    return count > 0

def get_opd_number(date_str):
    """
    This function retrieves the next OPD number for a given date.
  
    Args:
        cursor (sqlite3.Cursor): A database cursor object.
        date_str (str): The date in dd-mm-yyyy format.
  
    Returns:
        int: The next OPD number for the provided date.
    """
    cursor = conn.cursor()
  
    # Check for existing OPD slips for the provided date
    cursor.execute(f"""
        SELECT MAX(opd_number)
        FROM OPD_Slips
        WHERE slip_date = "{date_str}"
    """)
    max_opd_number = cursor.fetchone()[0]
    # If no OPD slips exist for the date, start from 1
    if max_opd_number is None:
      return 1
    else:
      # Increment the last OPD number for the date
      return max_opd_number + 1

def create_opd_slip(opd_number, patient_id, doctor_id, slip_date, slip_time, valid_upto, amount):
    """Inserts a new OPD slip record."""
    sql = """
    INSERT INTO OPD_Slips (opd_number, patient_id, doctor_id, slip_date, slip_time, valid_upto, amount)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    params = (opd_number, patient_id, doctor_id, slip_date, slip_time, valid_upto, amount)
    execute_query(sql, params)

def get_opd_slip_by_id(opd_slip_id):
    """Retrieves an OPD slip record by ID."""
    sql = "SELECT * FROM OPD_Slips WHERE id = ?"
    params = (opd_slip_id,)
    cursor = execute_query( sql, params)
    return fetch_one(cursor)

def get_opd_slips_by_patient(patient_id):
    """Retrieves all OPD slips for a specific patient."""
    sql = "SELECT * FROM OPD_Slips WHERE patient_id = ?"
    params = (patient_id,)
    cursor = execute_query( sql, params)
    return fetch_all(cursor)


def get_all_opd_today(today_date):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM OPD_slips
        WHERE slip_date = ?
        ORDER BY opd_number DESC;
    """, (today_date,))
    results = cursor.fetchall()
    return results


# if __name__ == "__main__":
    # print('hello world')