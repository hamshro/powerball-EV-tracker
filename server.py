from flask import Flask, render_template
from pb import jackpot, EV_of_ticket, next_jackpot3, alpha
from waitress import serve

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template(
        'index.html',
        jackpot=next_jackpot3, 
        ticket_value=EV_of_ticket
    
    )
    
if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8000)