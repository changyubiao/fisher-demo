from flask import Flask

from simplelog import logger


app = Flask(__name__)


@app.route('/')
def hello_world():

    logger.info("hahah  hello world ")
    logger.warning("hahah  hello world ")
    logger.debug("hahah  hello world ")
    logger.error("hahah  hello world ")
    logger.exception("hahah  hello world ")
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
