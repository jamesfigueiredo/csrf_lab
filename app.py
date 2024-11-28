from flask import Flask, render_template_string, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# Configurações de segurança
app.config['SECRET_KEY'] = 'minha_chave_secreta_segura'  # Alterar em produção
csrf = CSRFProtect(app)  # Habilita proteção CSRF

# Formulário protegido com CSRF
class TransferForm(FlaskForm):
    amount = StringField('Valor', validators=[DataRequired()])
    to_account = StringField('Conta de Destino', validators=[DataRequired()])
    submit = SubmitField('Transferir')

# Página inicial com formulário
@app.route("/", methods=["GET", "POST"])
def index():
    form = TransferForm()
    if form.validate_on_submit():
        amount = form.amount.data
        to_account = form.to_account.data
        # Simula o processamento seguro da transferência
        flash(f"Transferência de R$ {amount} para a conta {to_account} realizada com segurança!")
        return redirect(url_for("index"))
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Transferência Bancária</title>
            <link rel="stylesheet" href="/static/styles.css">
        </head>
        <body>
            <div class="container">
                <h1>Transferência Bancária</h1>
                <form method="POST">
                    {{ form.hidden_tag() }}
                    <label for="amount">Valor:</label>
                    {{ form.amount(class_="input-field") }}
                    <label for="to_account">Conta de Destino:</label>
                    {{ form.to_account(class_="input-field") }}
                    {{ form.submit(class_="submit-button") }}
                </form>
                {% with messages = get_flashed_messages() %}
                {% if messages %}
                    <div class="messages">
                        {% for message in messages %}
                            <p>{{ message }}</p>
                        {% endfor %}
                    </div>
                {% endif %}ß
                {% endwith %}
            </div>
        </body>
        </html>
    ''', form=form)

if __name__ == "__main__":
    app.run(debug=True)
