# Delete the database
database_file = 'UserBookings.db'
if os.path.exists(database_file):
    os.remove(database_file)
