
import socket
# from waitress import serve
env = 'dev'  
host_ip = socket.gethostbyname(socket.gethostname())
from Mainapp import app



from Mainapp.lnt.lnt import lnt_bp
from Mainapp.lnt.lnt import projinfo
from Mainapp.lnt.lnt import datasheet
from Mainapp.lnt.lnt import final
from Mainapp.auth import auth_bp
from Mainapp.database import  db_bp




app.register_blueprint(db_bp,url_prefix="/lnt")
app.register_blueprint(auth_bp,url_prefix="/lnt")
app.register_blueprint(lnt_bp, url_prefix='/lnt')
app.register_blueprint(projinfo, url_prefix='/lnt')
app.register_blueprint(datasheet, url_prefix='/lnt')
app.register_blueprint(final, url_prefix='/lnt')







if __name__ == '__main__':
    if env == "production":
        print("WSGI SERVER")
    
    else:
        app.run(host=host_ip, port=2500, debug=True)


 