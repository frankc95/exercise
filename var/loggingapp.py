import ConfigParser
import logging

from logging.handlers import RotatingFileHandler
from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def root():
    this_route = url_for('.root')
    app.logger.info("Logging a test message from "+this_route)
    return "Hello Napier from the configuration testing app (Now with added logging)"

@app.route('/init/')
def init(app):
    config = ConfigParser.Config.Parser()
    try:
        config_location = "etc/logging.cfg"
        config.read(config_location)

        app.config['DEBUG'] = config.get("config", "debug")
        app.config['ip_address'] = config.get("config", "ip_address")
        app.config['port'] = config.get("config", "port")
        app.config['url'] = config.get("config", "url")
        app.config['log_file'] = config.get("config", "log_file")
        app.config['log_location'] = config.get("config", "log_location")
        app.config['log_level'] = config.get("config", "log_level")
    except:
        print "Could not read configs from: ", config_location

@app.route('/logs/')
def logs(app):
    log_pathname = app.config['log_location'] + app.config['log_file']
    file_handler = RotatingFileHandler(log_pathname, maxBytes=1024*1024 * 10 , backupCount=1024)
    file_handler.setLevel( app.config['log.level'] )
    formatter = logging.Formatter("%(levelname)s | %(asctime)s | %(module)s | %(funcName) | %(message)s")
    file_handler.setFormatter(formatter)
    app.logger.setLevel( app.config['log_level'] )
    app.logger.addHandler(file_handler)

    init(app)
    logs(app)

    if __name__ == '__main__':
        init(app)
        logs(app)
        app.run(host=app.config['ip_address'], port=int(app.config['port']))

