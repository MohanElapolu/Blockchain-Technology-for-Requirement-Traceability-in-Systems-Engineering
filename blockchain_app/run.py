from requirement_chain import app
from argparse import ArgumentParser

if __name__=="__main__":
    #db.create_all()
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', type=int, default=5000)
    args = parser.parse_args()
    port = args.port
    app.run(host="localhost", port= port, debug=True, threaded=True)