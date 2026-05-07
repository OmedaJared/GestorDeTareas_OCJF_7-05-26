# 📋 TaskManager - Sistema de Gestión de Tareas

Un sistema moderno de gestión de tareas con diseño inspirado en Discord, construido con Flask y MongoDB Atlas.

## ✨ Características

- 🎨 **Diseño Discord-like**: Interfaz moderna con tema oscuro y colores característicos
- 🔐 **Autenticación Segura**: Registro/login con encriptación bcrypt
- 📝 **Gestión de Tareas**: Crear, ver y gestionar tareas personales
- ☁️ **MongoDB Atlas**: Base de datos en la nube
- 📱 **Responsive**: Funciona en desktop y móvil

## 🚀 Instalación y Configuración

### 1. Clona o descarga el proyecto

### 2. Instala las dependencias

```bash
cd "C:\Users\User\OneDrive\Desktop\CONTROL (1)\CONTROL"
uv add flask pymongo bcrypt python-dotenv
```

### 3. Configura MongoDB Atlas

1. Ve a [https://www.mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
2. Crea una cuenta gratuita
3. Crea un nuevo cluster
4. Ve a "Database Access" → "Add New Database User"
5. Ve a "Network Access" → "Add IP Address" (agrega `0.0.0.0/0` para desarrollo)
6. Ve a "Clusters" → "Connect" → "Connect your application"
7. Copia la connection string

### 4. Configura las variables de entorno

Edita el archivo `.env` en la raíz del proyecto:

```env
# Configuración de MongoDB Atlas
MONGO_USER=tu_usuario_real
MONGO_PASSWORD=tu_contraseña_real
MONGO_CLUSTER=tu_cluster_real
```

**Ejemplo:**
```env
MONGO_USER=usuario123
MONGO_PASSWORD=miClaveSegura456
MONGO_CLUSTER=cluster0.abcde
```

### 5. Ejecuta la aplicación

```bash
python app.py
```

La aplicación estará disponible en: `http://127.0.0.1:5000`

## 🎯 Uso de la Aplicación

### Registro de Usuario
1. Ve a la página principal
2. Haz clic en "Regístrate"
3. Completa nombre, email y contraseña
4. ¡Listo! Ya puedes iniciar sesión

### Gestión de Tareas
1. Inicia sesión con tu cuenta
2. En el dashboard, escribe una nueva tarea
3. Haz clic en "Añadir"
4. Tus tareas aparecerán en la lista

## 🎨 Paleta de Colores (Discord-like)

- **Fondo principal**: `#23272a` (Discord Darker)
- **Paneles**: `#2c2f33` (Discord Dark)
- **Elementos**: `#36393f` (Discord Light)
- **Acento**: `#5865f2` (Discord Blurple)
- **Texto**: `#dcddde` (Discord Text)
- **Texto secundario**: `#72767d` (Discord Text Muted)

## 📁 Estructura del Proyecto

```
CONTROL (1)/
├── app.py                    # Aplicación principal Flask
├── .env                      # Variables de entorno (configurar)
├── .env.example             # Ejemplo de configuración
├── templates/
│   ├── login.html           # Página de inicio de sesión
│   ├── registro.html        # Página de registro
│   ├── recuperar.html       # Recuperación de contraseña
│   └── dashboard.html       # Panel principal de tareas
└── CONTROL/
    └── .venv/               # Entorno virtual Python
```

## 🔧 Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Base de Datos**: MongoDB Atlas
- **Frontend**: HTML5, Tailwind CSS
- **Seguridad**: bcrypt para encriptación
- **Sesiones**: Flask-Session

## 🚨 Solución de Problemas

### Error de conexión MongoDB
- Verifica que las credenciales en `.env` sean correctas
- Asegúrate de que tu IP esté permitida en MongoDB Atlas
- Espera unos minutos después de crear el cluster

### Error de dependencias
```bash
cd CONTROL
uv add flask pymongo bcrypt python-dotenv
```

### Puerto ocupado
Si el puerto 5000 está ocupado:
```python
if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Cambia el puerto
```

## 📝 Notas de Desarrollo

- El sistema de recuperación de contraseña está simulado
- Las tareas solo tienen estado "pendiente" (se puede expandir)
- La interfaz es completamente responsive

## 🤝 Contribución

Siéntete libre de mejorar el diseño o añadir funcionalidades como:
- Estados de tareas (completada, en progreso)
- Edición y eliminación de tareas
- Categorías de tareas
- Notificaciones
- Tema claro/oscuro

---

**¡Disfruta gestionando tus tareas con estilo Discord! 🎉**