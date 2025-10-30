import web

urls = (
    '/', 'mvc.controllers.index.Index',
    '/lista_usuarios', 'mvc.controllers.usuarios.lista_usuarios.ListaUsuarios',
    '/detalle_usuario', 'mvc.controllers.usuarios.detalle_usuario.DetalleUsuario',
    '/insertar_usuario', 'mvc.controllers.usuarios.insertar_usuario.InsertarUsuario',
    '/lista_productos', 'mvc.controllers.productos.lista_productos.ListaProductos',
    '/detalle_producto', 'mvc.controllers.productos.detalle_producto.DetalleProducto',
    '/insertar_producto', 'mvc.controllers.productos.insertar_producto.InsertarProducto'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()