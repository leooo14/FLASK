from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Configuración de Flask-Mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "leopardog152@gmail.com"
app.config["MAIL_PASSWORD"] = "gipv szcu nlss kzog"  # Contraseña de aplicación de Gmail
app.config["MAIL_DEFAULT_SENDER"] = "leopardog152@gmail.com"

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        nombre = request.form["nombre"]
        email = request.form["email"]
        mensaje = request.form["mensaje"]

        # Configuración del mensaje
        msg = Message(
            subject=f"Nuevo mensaje de {nombre}",
            recipients=["leopardog152@gmail.com"],  # Cambiado a tu correo
            body=f"Nombre: {nombre}\nCorreo: {email}\nMensaje: {mensaje}",
        )
        try:
            mail.send(msg)
            flash("¡Tu mensaje ha sido enviado con éxito!", "success")
        except Exception as e:
            flash(f"Hubo un error al enviar el mensaje: {str(e)}", "danger")

        return redirect(url_for("contact"))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
