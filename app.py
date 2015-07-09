from osoba.core import app, db, createdb
import osoba.urls

if __name__ == '__main__':
    createdb()
    print "Creating database tables..."
    db.create_all()
    print "Running Osoba..."
    app.run(debug=True, host='0.0.0.0', port=5000)
    print "Exiting!"
