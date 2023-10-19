from flask import Flask, render_template, request, redirect, url_for, Response, session
import os
import database as bd


template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
static_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates', 'static')



app = Flask(__name__, template_folder = template_dir, static_folder= static_dir)

# RUTAS DE ENLACE
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/Principal')
def principal():
    return render_template('Principal.html')

@app.route('/registrar')
def registrar():
    return render_template('registrar.html')

#no necesarios

@app.route('/formulario-equipo')
def f_equipo():
    return render_template('forms/form-equipo.html')

@app.route('/formulario-perifericos')
def f_perifericos():
    return render_template('forms/form-perifericos.html')

@app.route('/formulario-pantalla')
def f_pantalla():
    return render_template('forms/form-pantalla.html')

@app.route('/formulario-otros')
def f_otros():
    return render_template('forms/form-otros.html')


#LOGIN
@app.route('/acceso-login', methods=["GET","POST"])
def login_int():
    if request.method == 'POST' and 'txtCorreo' in request.form and 'txtPassword':
        correo = request.form['txtCorreo']
        password = request.form['txtPassword']

        cur = bd.database.cursor()
        cur.execute('SELECT * FROM login WHERE correo = %s AND password = %s',(correo, password,))
        account = cur.fetchone()

        if account:
            session['logueado'] = True
            session['id'] = account[0]
            
            return render_template('Principal.html')
        else:
            return render_template('login.html',mensaje="Usuario Incorrecto")



# MOSTAR DATOS OTROS
@app.route('/form-otros')
def Otros():
    cursor = bd.database.cursor()
    cursor.execute("SELECT * FROM otros")
    myresult = cursor.fetchall()
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('forms/form-otros.html', data=insertObject)


#añadir otros
@app.route('/otros', methods=['POST'])
def addOtros():
    tipo = request.form['tipo']
    serial =request.form['serial']
    marca =request.form['marca'] 
    descripcion =request.form['descripcion'] 
    ubicacion =request.form['ubicacion'] 

    if id and tipo and serial and marca and descripcion and ubicacion:
        cursor = bd.database.cursor()
        sql="INSERT INTO otros (Otros_Tipo, Otros_Serial, Otros_Marca, Otros_Descripcion, Otros_Ubicacion) VALUES ( %s, %s, %s, %s,%s)"
        data=(tipo, serial, marca, descripcion, ubicacion)
        cursor.execute(sql, data)
        bd.database.commit()
    return redirect(url_for('Otros'))


#MOSTRAR DATOS EQUIPO
@app.route('/form-equipo')
def Equipo():
    cur = bd.database.cursor()
    cur.execute("SELECT * FROM equipo")
    myresult = cur.fetchall()
    insertObject = []
    columnNames = [column[0] for column in cur.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cur.close()
    return render_template('forms/form-equipo.html', data=insertObject)

#AÑADIR EQUIPO
@app.route('/equipo', methods=['POST'])
def addEquipo():
    numero = request.form['numero']
    serial =request.form['serial']
    marca =request.form['marca'] 
    ram =request.form['ram'] 
    procesador =request.form['procesador']
    disco =request.form['disco'] 
    fecha =request.form['fecha']
    estado =request.form['estado']
    grafica =request.form['grafica']
    descripcion =request.form['descripcion']
    ubicacion =request.form['ubicacion']
    
    if numero and serial and marca and ram and procesador and disco and fecha and estado and grafica and descripcion and ubicacion:
        cursor = bd.database.cursor()
        sql="INSERT INTO equipo (N_Equipo, Equipo_Serial, Equipo_Marca, Equipo_Ram, Equipo_Procesador, Equipo_Disco, Equipo_FechaRegis, Equipo_Estado, Equipo_Grafica, Equipo_Descripcion, Equipo_Ubicacion) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"
        data=(numero, serial, marca, ram, procesador, disco, fecha, estado, grafica, descripcion, ubicacion)
        cursor.execute(sql, data)
        bd.database.commit()
    return redirect(url_for('Equipo'))


#MOSTRAR DATOS PERIFERICOS
@app.route('/form-perifericos')
def Perifericos():
    cursor_peri = bd.database.cursor()
    cursor_peri.execute("SELECT * FROM perifericos")
    myresult = cursor_peri.fetchall()
    insertObject = []
    columnNames = [column[0] for column in cursor_peri.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor_peri.close()
    return render_template('forms/form-perifericos.html', datos = insertObject)

#AÑADIR DATOS PERIFERICOS
@app.route('/perifericos', methods=['POST'])
def addPerifericos():
    n_equi = request.form['n_equi']
    serial_mause =request.form['serial-mouse']
    marca_mause =request.form['marca-mouse'] 
    estado_mause =request.form['estado-mouse'] 
    descripcion_mause =request.form['descripcion-mouse']
    serial_teclado =request.form['serial-teclado'] 
    marca_teclado =request.form['marca-teclado']
    estado_teclado =request.form['estado_teclado']
    descripcion_teclado =request.form['descripcion-teclado']
    ubicacion =request.form['ubicacion']
    
    if n_equi and serial_mause and marca_mause and estado_mause and descripcion_mause and serial_teclado and marca_teclado and estado_teclado  and descripcion_teclado and ubicacion:
        cursor = bd.database.cursor()
        sql="INSERT INTO perifericos (N_Equipo, Mouse_Serial, Mouse_Marca, Mouse_Estado, Mouse_Descripcion, Teclado_Serial, Teclado_Marca, Teclado_Estado, Teclado_Descripcion, Peri_Ubicacion) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s)"
        datos=(n_equi, serial_mause, marca_mause, estado_mause, descripcion_mause, serial_teclado, marca_teclado, estado_teclado, descripcion_teclado, ubicacion)
        cursor.execute(sql, datos)
        bd.database.commit()
    return redirect(url_for('Perifericos'))



#MOSTAR DATOS PANTALLA
@app.route('/form-pantalla')
def Pantalla():
    cursor = bd.database.cursor()
    cursor.execute("SELECT * FROM pantalla")
    myresult = cursor.fetchall()
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('forms/form-pantalla.html', data=insertObject)

#AÑADIR DATOS PANTALLA
@app.route('/pantalla', methods=['POST'])
def addPantalla():
    n_equi = request.form['n_equi']
    serial = request.form['serial']
    marca =request.form['marca']
    pulgadas =request.form['pulgadas'] 
    resolucion =request.form['resolucion'] 
    estado =request.form['estado'] 
    descripcion =request.form['descripcion']
    ubicacion =request.form['ubicacion']  

    if n_equi and serial and marca and pulgadas and resolucion and estado and descripcion and ubicacion:
        cursor = bd.database.cursor()
        sql="INSERT INTO pantalla (N_Equipo, Pantalla_Serial, Pantalla_Marca, Pantalla_Pulgadas, Pantalla_Resolucion, Pantalla_Estado, Pantalla_Descripcion, Pantalla_Ubicacion) VALUES (%s, %s, %s, %s, %s,%s,%s,%s)"
        data=(n_equi, serial, marca, pulgadas, resolucion, estado, descripcion, ubicacion)
        cursor.execute(sql, data)
        bd.database.commit()
    return redirect(url_for('Pantalla'))


#EDITAR DATOS EQUIPO
@app.route('/edit/<id>')
def edit_equipo(id):
    cursor = bd.database.cursor()
    cursor.execute('SELECT * FROM equipo WHERE ID_Equipo = %s', [id])
    data = cursor.fetchall()
    return render_template('forms/edit-equipo.html', equip = data[0])

@app.route('/update-equipo/<id>', methods=['POST'])
def update_equip(id):
    if request.method == 'POST':
        numero = request.form['numero']
        serial =request.form['serial']
        marca =request.form['marca'] 
        ram =request.form['ram'] 
        procesador =request.form['procesador']
        disco =request.form['disco'] 
        fecha =request.form['fecha']
        estado =request.form['estado']
        grafica =request.form['grafica']
        descripcion =request.form['descripcion']
        ubicacion =request.form['ubicacion']

        cursor = bd.database.cursor()
        cursor.execute("""UPDATE equipo 
                       SET N_Equipo = %s,
                        Equipo_Serial = %s,
                        Equipo_Marca = %s,
                        Equipo_Ram = %s,
                        Equipo_Procesador = %s,
                        Equipo_Disco = %s,
                        Equipo_FechaRegis = %s,
                        Equipo_Estado = %s,
                        Equipo_Grafica = %s,
                        Equipo_Descripcion = %s,
                        Equipo_Ubicacion = %s WHERE ID_equipo = %s""", (numero, serial, marca, ram, procesador, disco, fecha, estado, grafica, descripcion, ubicacion, id))
        bd.database.commit()
        return redirect(url_for('registrar'))



#EDITAR DATOS OTROS
@app.route('/edit_otros/<id>')
def edit_otros(id):
    cursor = bd.database.cursor()
    cursor.execute('SELECT * FROM otros WHERE ID_Otros = %s', [id])
    data = cursor.fetchall()
    return render_template('forms/edit-otros.html', otros = data[0])

@app.route('/update-otros/<id>', methods=['POST'])
def update_otros(id):
    if request.method == 'POST':
        tipo = request.form['tipo']
        serial =request.form['serial']
        marca =request.form['marca'] 
        descripcion =request.form['descripcion'] 
        ubicacion =request.form['ubicacion'] 

        cursor = bd.database.cursor()
        cursor.execute("""UPDATE otros 
                       SET Otros_Tipo = %s,
                        Otros_Serial = %s,
                        Otros_Marca = %s,
                        Otros_Descripcion = %s,
                        Otros_Ubicacion = %s WHERE ID_Otros = %s""", (tipo, serial, marca, descripcion, ubicacion, id))
        bd.database.commit()
        return redirect(url_for('registrar'))

#EDITAR DATOS PERIFERICOS
@app.route('/edit_perife/<id>')
def edit_perife(id):
    cursor = bd.database.cursor()
    cursor.execute('SELECT * FROM perifericos WHERE ID_Periferico = %s', [id])
    data = cursor.fetchall()
    return render_template('forms/edit-perifericos.html', perife = data[0])

@app.route('/update-perife/<id>', methods=['POST'])
def update_perifericos(id):
    if request.method == 'POST':
        n_equi = request.form['n_equi']
        serial_mause =request.form['serial-mouse']
        marca_mause =request.form['marca-mouse'] 
        estado_mause =request.form['estado-mouse'] 
        descripcion_mause =request.form['descripcion-mouse']
        serial_teclado =request.form['serial-teclado'] 
        marca_teclado =request.form['marca-teclado']
        estado_teclado =request.form['estado_teclado']
        descripcion_teclado =request.form['descripcion-teclado']
        ubicacion =request.form['ubicacion']

        cursor = bd.database.cursor()
        cursor.execute("""UPDATE perifericos 
                       SET N_Equipo = %s,
                        Mouse_Serial = %s,
                        Mouse_Marca = %s,
                        Mouse_Estado = %s,
                        Mouse_Descripcion = %s,
                        Teclado_Serial = %s,
                        Teclado_Marca = %s,
                        Teclado_Estado = %s,
                        Teclado_Descripcion = %s,
                        Peri_Ubicacion = %s WHERE ID_Periferico = %s""", (n_equi, serial_mause, marca_mause, estado_mause, descripcion_mause, serial_teclado, marca_teclado, estado_teclado, descripcion_teclado, ubicacion, id))
        bd.database.commit()
        return redirect(url_for('registrar'))


#EDITAR DATOS PANTALLAS
@app.route('/edit_pantalla/<id>')
def edit_pantalla(id):
    cursor = bd.database.cursor()
    cursor.execute('SELECT * FROM pantalla WHERE ID_Pantalla = %s', [id])
    data = cursor.fetchall()
    return render_template('forms/edit-pantalla.html', pantalla = data[0])

@app.route('/update-pantalla/<id>', methods=['POST'])
def update_pantalla(id):
    if request.method == 'POST':
        n_equi = request.form['n_equi']
        serial = request.form['serial']
        marca =request.form['marca']
        pulgadas =request.form['pulgadas'] 
        resolucion =request.form['resolucion'] 
        estado =request.form['estado'] 
        descripcion =request.form['descripcion']
        ubicacion =request.form['ubicacion']

        cursor = bd.database.cursor()
        cursor.execute("""UPDATE pantalla 
                       SET N_Equipo = %s,
                        Pantalla_Serial = %s,
                        Pantalla_Marca = %s,
                        Pantalla_Pulgadas = %s,
                        Pantalla_Resolucion = %s,
                        Pantalla_Estado = %s,
                        Pantalla_Descripcion = %s,
                        Pantalla_Ubicacion = %s WHERE ID_Pantalla = %s""", (n_equi, serial, marca, pulgadas, resolucion, estado, descripcion, ubicacion, id))
        bd.database.commit()
        return redirect(url_for('registrar'))


#ELIMINAR DATOS EQUIPO
@app.route('/delete/<string:id>')
def delete_equipo(id):
    cur = bd.database.cursor()
    cur.execute('DELETE FROM equipo WHERE ID_Equipo = %s', [id])
    bd.database.commit()
    return redirect(url_for('Equipo'))


#ELIMINAR DATOS OTROS
@app.route('/delete-otros/<string:id>')
def delete_otros(id):
    cur = bd.database.cursor()
    cur.execute('DELETE FROM otros WHERE ID_Otros  = %s', [id])
    bd.database.commit()
    return redirect(url_for('Otros'))

#ELIMINAR DATOS PANTALLA
@app.route('/delete-pantalla/<string:id>')
def delete_pantalla(id):
    cur = bd.database.cursor()
    cur.execute('DELETE FROM pantalla WHERE ID_Pantalla  = %s', [id])
    bd.database.commit()
    return redirect(url_for('Pantalla'))


#ELIMINAR DATOS PANTALLA
@app.route('/delete-perife/<string:id>')
def delete_periferico(id):
    cur = bd.database.cursor()
    cur.execute('DELETE FROM perifericos WHERE ID_Periferico  = %s', [id])
    bd.database.commit()
    return redirect(url_for('Perifericos'))

#PUERTO
if __name__ == '__main__':
    app.secret_key="inventario"
    app.run(debug=True,host='0.0.0.0', port=4000, threaded=True)