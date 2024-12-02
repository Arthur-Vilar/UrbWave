from flask import render_template, request, redirect, url_for
from .models import Product
from . import db

def init_app(app):
    # Página inicial - Exibir produtos
    @app.route('/')
    def index():
        products = Product.query.all()
        return render_template('index.html', products=products)
    
    # Criar um novo produto
    @app.route('/product/new', methods=['GET', 'POST'])
    def new_product():
        if request.method == 'POST':
            name = request.form['name']
            description = request.form['description']
            price = request.form['price']
            quantity = request.form['quantity']

            product = Product(
                name=name, 
                description=description,
                price=float(price), 
                quantity=int(quantity)
            )
            db.session.add(product)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('new_product.html')
    
    # Editar um produto
    @app.route('/product/edit/<int:id>', methods=['GET', 'POST'])
    def edit_product(id):
        product = Product.query.get_or_404(id)
        if request.method == 'POST':
            product.name = request.form['name']
            product.description = request.form['description']
            product.price = float(request.form['price'])
            product.quantity = int(request.form['quantity'])
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('edit_product.html', product=product)
    
    # Excluir um produto
    @app.route('/product/delete/<int:id>', methods=['POST'])
    def delete_product(id):
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for('index'))