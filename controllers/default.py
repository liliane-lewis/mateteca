# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------

@auth.requires_login()
def index():
    response.flash = T("Bem indo a biblioteca")
    return locals()


@auth.requires_membership('admin')
def cadastrar_livro():
    response.flash = T("Cadastrar Livros")
    form = crud.create(db.livros)

    return locals()

#    form = SQLFORM(db.livros)
#
#    if form.process().accepted:
#        response.flash = 'Livro cadastrado'
#    elif form.errors:
#        response.flash = 'Houve um erro:'+str(form.errors)
#    else:
#        response.flash = 'Deu merda'
#
#    return locals()

@auth.requires_membership('admin')
def alterar_livro():
    response.flash = T("Alterar Livro")

    id_livro = request.args(0)

    form = crud.update(db.livros, id_livro)
#    form = SQLFORM(db.livros, record=id_livro,
#        deletable=True)

#    if form.process().accepted:
#        response.flash = 'Livro cadastrado'
#    elif form.errors:
#        response.flash = 'Houve um erro:'+str(form.errors)
#    else:
#        response.flash = 'Deu merda'

    return locals()

def listar_livros():
#    livros = db(db.livros.id > 0).select()
    livros = SQLFORM.grid(db.livros)
    return locals()

def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


