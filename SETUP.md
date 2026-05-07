## 🚀 GUÍA RÁPIDA DE CONFIGURACIÓN

### ✅ ESTADO ACTUAL
✔️ Servidor Flask: FUNCIONANDO en http://127.0.0.1:5000
✔️ Todas las plantillas: LISTA
✔️ Sistema de autenticación: LISTO
✔️ Base de datos: PENDIENTE DE CONFIGURACIÓN

---

### 📊 LOS 3 PASOS PARA HACER FUNCIONAR TODO

#### **PASO 1: Crear cuenta en MongoDB Atlas (5 minutos)**

1. Ve a: https://www.mongodb.com/cloud/atlas
2. Haz clic en "Start Free" (Gratis)
3. Completa el registro y crea una cuenta
4. Crea un nuevo PROYECTO
5. Crea un CLUSTER (elige el plan gratuito)
6. ESPERA A QUE SE CREE (toma 1-5 minutos)

#### **PASO 2: Obtener credenciales (3 minutos)**

1. En Atlas, ve a: **Database** → **Clusters**
2. Haz clic en tu cluster → **CONNECT**
3. Selecciona **"Connect your application"**
4. Elige **Python** y **3.6 or later**
5. **COPIA** la connection string que aparece

Verá algo como:
```
mongodb+srv://usuario:contraseña@cluster0.abcde.mongodb.net/?retryWrites=true&w=majority
```

#### **PASO 3: Actualizar .env (1 minuto)**

En `c:\Users\User\OneDrive\Desktop\CONTROL (1)\.env`:

Cambia:
```env
MONGO_USER=tu_usuario_aqui
MONGO_PASSWORD=tu_contraseña_aqui
MONGO_CLUSTER=tu_cluster_aqui
```

Por los valores reales extraídos de la connection string:

Ejemplo:
```env
MONGO_USER=usuario123
MONGO_PASSWORD=miClaveSegura456
MONGO_CLUSTER=cluster0
```

---

### 📱 AHORA PUEDES USAR LA APP

1. **Abre**: http://127.0.0.1:5000
2. **Haz clic**: "Regístrate"
3. **Completa**:
   - Nombre completo
   - Correo válido
   - Contraseña segura
4. **¡Listo!** Inicia sesión y comienza a crear tareas

---

### 🔍 DÓNDE ENCONTRAR TUS CREDENCIALES

En MongoDB Atlas:

**MONGO_USER**: El nombre de usuario que creaste
```
Menú → Database Access → Veras el usuario
```

**MONGO_PASSWORD**: La contraseña que creaste
```
Menú → Database Access → Edita el usuario para ver/cambiar
```

**MONGO_CLUSTER**: El nombre del cluster (ej: cluster0, cluster1)
```
Menú → Clusters → Veras el nombre arriba a la izquierda
```

---

### ⚙️ SI ALGO NO FUNCIONA

**Error: "DNS query name does not exist"**
- ✓ Verifica que escribiste correctamente MONGO_CLUSTER
- ✓ Asegúrate de que el cluster está completamente creado (espera 5+ minutos)

**Error: "Invalid username/password"**
- ✓ Verifica que MONGO_USER y MONGO_PASSWORD sean exactos
- ✓ No debe tener espacios extras

**No puedo acceder a MongoDB Atlas**
- ✓ Agrega tu IP a la lista blanca:
  - Dashboard → Network Access → Add IP Address
  - Escribe: 0.0.0.0/0 (permite todas las IPs, solo para desarrollo)

---

### 🎨 QUÉ PUEDES HACER YA

✅ **Funciones Disponibles:**
- Registrarse con email y contraseña
- Iniciar sesión seguro
- Ver perfil de usuario
- Crear tareas nuevas
- Ver todas tus tareas
- Estadísticas de tareas
- Cerrar sesión

**Próximas funciones:**
- Editar tareas
- Eliminar tareas
- Cambiar estado de tareas (completada/pendiente)
- Temas personalizados

---

### 📞 SERVIDOR ACTIVO

Tu servidor estará escuchando en:
```
http://127.0.0.1:5000
```

Si quieres cambiar el puerto, edita la última línea de `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=8000)  # Cambia 5000 por 8000
```

---

**¡Ahora todo debe funcionar! 🎉**
