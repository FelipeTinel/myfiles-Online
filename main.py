from myfiles import app
from myfiles import db
from myfiles.models import User, File
if __name__ == '__main__':
    
    app.run(debug=True)
