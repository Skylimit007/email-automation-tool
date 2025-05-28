from flask import Flask, request, send_file
import logging
import datetime

app = Flask(__name__)

# Configure logging into a file
logging.basicConfig(filename='tracking.log', level=logging.INFO, format='%(asctime)s %(message)s')

@app.route('/pixel.png')
def pixel():
    # Log the request with query parameters, e.g. email
    email = request.args.get('email', 'unknown')
    user_agent = request.headers.get('User-Agent', '')
    ip = request.remote_addr
    logging.info(f"Pixel requested by email={email} ip={ip} user_agent={user_agent}")

    # Serve the 1x1 transparent pixel image file
    return send_file('pixel.png', mimetype='image/png')

if __name__ == '__main__':
    # Run the server accessible on all interfaces on port 5000
    app.run(host='0.0.0.0', port=5000)
