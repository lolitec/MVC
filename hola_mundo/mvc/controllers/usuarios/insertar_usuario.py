import web

render = web.template.render("mvc/views/usuarios/")

class InsertarUsuario:
    def __init__(self):
        pass

    def GET(self):
        return render.insertar_usuario()