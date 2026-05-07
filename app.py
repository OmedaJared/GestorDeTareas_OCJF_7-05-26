import os
import ssl
import certifi
from flask import Flask, render_template, request, redirect, url_for, flash, session
from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
import bcrypt # Para seguridad de contraseñas
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

app = Flask(__name__)
app.secret_key = "secreto_muy_seguro"

# funciones para conectar a mongoDB Atlas usando variables de entorno
def get_db_connection():
    usuario = os.getenv('MONGO_USER', '24308060610036_db_user').strip()
    password = os.getenv('MONGO_PASSWORD', 'yamjarfer53').strip()
    cluster = os.getenv('MONGO_CLUSTER', 'cluster0.0hepetvs.mongodb.net').strip()
    db_name = os.getenv('MONGO_DB', 'control_app_db').strip()

    if not all([usuario, password, cluster]):
        print("WARNING: Configura el archivo .env con tus credenciales de MongoDB Atlas")
        print("   Copia .env.example a .env y completa los valores")
        return None

    if not cluster.endswith('.mongodb.net'):
        cluster = f"{cluster}.mongodb.net"

    uri = f"mongodb+srv://{usuario}:{password}@{cluster}/?retryWrites=true&w=majority"

    try:
        cliente = MongoClient(
            uri,
            tls=True,
            tlsCAFile=certifi.where(),
            serverSelectionTimeoutMS=10000,
            connectTimeoutMS=10000,
            socketTimeoutMS=10000,
        )
        cliente.admin.command('ping')
        print("✅ Conectado a MongoDB Atlas")
        return cliente[db_name]
    except Exception as e:
        print(f"❌ Error conectando a MongoDB: {e}")
        return None

db = get_db_connection()
usuarios_col = db['usuarios'] if db is not None else None
tareas_col = db['tareas'] if db is not None else None

# Crear índices para asegurar correos únicos
if usuarios_col is not None:
    usuarios_col.create_index("email", unique=True)

# --- RUTAS DE AUTENTICACIÓN ---

@app.route('/')
def inicio():
    return render_template('login.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        if usuarios_col is None:
            flash("❌ Base de datos no configurada. Contacta al administrador.", "error")
            return render_template('registro.html')
        
        nombre = request.form.get('nombre')
        email = request.form.get('email')
        password = request.form.get('password')
        
        # password por seguridad
        hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        try:
            usuarios_col.insert_one({
                "nombre": nombre,
                "email": email,
                "password": hashed_pw,
                "fecha_registro": datetime.now()
            })
            flash("Cuenta creada. ¡Inicia sesión!", "success")
            return redirect(url_for('inicio'))
        except:
            flash("El correo ya está registrado.", "error")
            
    return render_template('registro.html')

@app.route('/login', methods=['POST'])
def login():
    if usuarios_col is None:
        flash("❌ Base de datos no configurada. Contacta al administrador.", "error")
        return redirect(url_for('inicio'))
    
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = usuarios_col.find_one({"email": email})
    
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
        session['user_id'] = str(user['_id'])
        session['user_name'] = user['nombre']
        return redirect(url_for('dashboard'))
    
    flash("Credenciales incorrectas", "error")
    return redirect(url_for('inicio'))

@app.route('/recuperar', methods=['GET', 'POST'])
def recuperar():
    if request.method == 'POST':
        if usuarios_col is None:
            flash("❌ Base de datos no configurada.", "error")
            return render_template('recuperar.html')
        
        email = request.form.get('email')
        user = usuarios_col.find_one({"email": email})
        if user:
            flash("Se ha enviado un código a tu correo (Simulado)", "success")
        else:
            flash("Correo no encontrado", "error")
    return render_template('recuperar.html')

#  GESTOR DE TAREAS (CRUD) 

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session: return redirect(url_for('inicio'))
    if tareas_col is None:
        flash("❌ Base de datos no configurada.", "error")
        return redirect(url_for('inicio'))
    
    # Obtener tareas del usuario logueado [cite: 572]
    mis_tareas = list(tareas_col.find({"usuario_id": session['user_id']}))
    return render_template('dashboard.html', tareas=mis_tareas)

@app.route('/nueva_tarea', methods=['POST'])
def nueva_tarea():
    if 'user_id' in session and tareas_col is not None:
        tarea = {
            "usuario_id": session['user_id'],
            "titulo": request.form.get('titulo'),
            "estado": "pendiente",
            "fecha": datetime.now()
        }
        tareas_col.insert_one(tarea) # Insertar documento [cite: 111]
    return redirect(url_for('dashboard'))

@app.route('/completar_tarea/<tarea_id>', methods=['POST'])
def completar_tarea(tarea_id):
    if 'user_id' in session and tareas_col is not None:
        from bson.objectid import ObjectId
        tareas_col.update_one(
            {"_id": ObjectId(tarea_id), "usuario_id": session['user_id']},
            {"$set": {"estado": "completada"}}
        )
    return redirect(url_for('dashboard'))

@app.route('/eliminar_tarea/<tarea_id>', methods=['POST'])
def eliminar_tarea(tarea_id):
    if 'user_id' in session and tareas_col is not None:
        from bson.objectid import ObjectId
        tareas_col.delete_one(
            {"_id": ObjectId(tarea_id), "usuario_id": session['user_id']}
        )
    return redirect(url_for('dashboard'))

@app.route('/editar_tarea/<tarea_id>', methods=['GET', 'POST'])
def editar_tarea(tarea_id):
    if 'user_id' not in session: return redirect(url_for('inicio'))
    if tareas_col is None:
        flash("❌ Base de datos no configurada.", "error")
        return redirect(url_for('inicio'))
    
    from bson.objectid import ObjectId
    tarea = tareas_col.find_one({"_id": ObjectId(tarea_id), "usuario_id": session['user_id']})
    if not tarea:
        flash("Tarea no encontrada.", "error")
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        nuevo_titulo = request.form.get('titulo')
        tareas_col.update_one(
            {"_id": ObjectId(tarea_id), "usuario_id": session['user_id']},
            {"$set": {"titulo": nuevo_titulo}}
        )
        return redirect(url_for('dashboard'))
    
    return render_template('editar_tarea.html', tarea=tarea)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('inicio'))

if __name__ == '__main__':
    app.run(debug=True)
