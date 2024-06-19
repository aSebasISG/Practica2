
from flask import Flask, Blueprint, url_for, jsonify, make_response, request, render_template, redirect, abort
from controller.historialComandoDaoControl import HistorialComandoDaoControl
from controller.tda.linked.linkedList import LinkedList

router = Blueprint('router', __name__)

@router.route('/')
def home():
    return render_template('template.html')

@router.route('/historial')
def lista_persona():
    hc = HistorialComandoDaoControl()
    return render_template('paginas/lista.html', lista=hc.to_dict())

@router.route('/historial/ordenar/<metodo_ordenamiento>/<ascendente_descendente>/<atributo_ordenar>')
def listado_ordenado_historial_comandos(metodo_ordenamiento, ascendente_descendente, atributo_ordenar):
   
    hc = HistorialComandoDaoControl()
    
    diccionario_ordenamiento = {
        "merge": hc._list().ordenamiento_atributo("Merge", f"_{atributo_ordenar}", int(ascendente_descendente)),
        "shell": hc._list().ordenamiento_atributo("Shell", f"_{atributo_ordenar}", int(ascendente_descendente)),
        "quick": hc._list().ordenamiento_atributo("Quick", f"_{atributo_ordenar}", int(ascendente_descendente)),
    }
    lista_nueva = diccionario_ordenamiento[metodo_ordenamiento]
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": hc.to_dic2(lista_nueva)}),
        200
    )
    
@router.route('/historial/buscar/<atributo_a_buscar>/<lineal_o_binaria>/<palabra_buscar>')
def busqueda_historial_comandos(atributo_a_buscar, lineal_o_binaria, palabra_buscar):
    hc = HistorialComandoDaoControl()
    if lineal_o_binaria == "binaria":
        lista_busqueda = hc._list().busquedaBinaria(hc._list(),f"_{atributo_a_buscar}", palabra_buscar)
        lista_navegador = LinkedList()
        lista_navegador.add(lista_busqueda)
    elif lineal_o_binaria == "lbinaria":
        lista_navegador = hc._list().busquedaLinealBinariaAtributo(hc._list(), f"_{atributo_a_buscar}", palabra_buscar)
        lista_navegador.print
    return make_response(
        jsonify({"msg":"OK", "code": 200, "data": hc.to_dic2(lista_navegador)}),
        200
    )
    
@router.route('/historial/comando_nuevo')
def formulario_nuevo_comando():
    return render_template('paginas/nuevo_comando.html')

@router.route('/historial/guardar', methods = ['POST'])  
def guardar_comando_nuevo():
    hc = HistorialComandoDaoControl()
    data = request.form
    if not "usuario" in data.keys():
       abort(400)
    hc._historial_comando._usuario = data['usuario']
    hc._historial_comando._email = data['email']
    hc._historial_comando._comando = data['comando']
    hc._historial_comando._descripcion = data['descripcion']
    hc.save
    return redirect("/historial", code=302)