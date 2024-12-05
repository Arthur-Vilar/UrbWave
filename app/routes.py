from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Product, Order
from app import db

main = Blueprint('main', __name__)

# Rotas para Produtos
@main.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@main.route('/new', methods=['GET', 'POST'])
def new_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        quantity = request.form['quantity']

        new_product = Product(
            name=name, 
            description=description, 
            price=float(price), 
            quantity=int(quantity)
        )
        db.session.add(new_product)
        db.session.commit()

        flash('Produto criado com sucesso!')
        return redirect(url_for('main.index'))

    return render_template('new_product.html')

@main.route('/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)

    if request.method == 'POST':
        product.name = request.form['name']
        product.description = request.form['description']
        product.price = float(request.form['price'])
        product.quantity = int(request.form['quantity'])

        db.session.commit()
        flash('Produto atualizado com sucesso!')
        return redirect(url_for('main.index'))

    return render_template('edit_product.html', product=product)

@main.route('/delete/<int:product_id>')
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()

    flash('Produto excluído com sucesso!')
    return redirect(url_for('main.index'))

# Rotas para Pedidos
@main.route('/orders')
def orders():
    orders = Order.query.all()
    return render_template('orders.html', orders=orders)

@main.route('/new_order', methods=['GET', 'POST'])
def new_order():
    products = Product.query.all()

    if request.method == 'POST':
        product_id = request.form['product_id']
        quantity = int(request.form['quantity'])
        payment_method = request.form['payment_method']
        status = request.form['status']
        
        product = Product.query.get_or_404(product_id)
        total_price = product.price * quantity

        new_order = Order(
            product_id=product.id, 
            quantity=quantity, 
            total_price=total_price, 
            payment_method=payment_method,
            status=status
        )
        db.session.add(new_order)
        db.session.commit()

        flash('Pedido criado com sucesso!')
        return redirect(url_for('main.orders'))

    return render_template('new_order.html', products=products)

@main.route('/delete_order/<int:order_id>')
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()

    flash('Pedido excluído com sucesso!')
    return redirect(url_for('main.orders'))