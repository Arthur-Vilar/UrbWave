from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import Product, Order, Customer
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

# Rotas para clientes
@main.route('/customers')
def customers():
    customers = Customer.query.all()
    return render_template('customers.html', customers=customers)

@main.route('/new_customer', methods=['GET', 'POST'])
def new_customer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        address = request.form['address']
        username = request.form['username']
        password = request.form['password']
        purchase_history = request.form['purchase_history']

        new_customer = Customer(
            name=name,
            email=email,
            phone=phone,
            address=address,
            username=username,
            password=password,
            purchase_history=purchase_history
        )
        db.session.add(new_customer)
        db.session.commit()

        flash('Cliente criado com sucesso!')
        return redirect(url_for('main.customers'))

    return render_template('new_customer.html')

@main.route('/edit_customer/<int:customer_id>', methods=['GET', 'POST'])
def edit_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)

    if request.method == 'POST':
        customer.name = request.form['name']
        customer.email = request.form['email']
        customer.phone = int(request.form['phone'])
        customer.address = request.form['address']
        customer.username = request.form['username']
        customer.password = request.form['password']

        db.session.commit()
        flash('Cliente atualizado com sucesso!')
        return redirect(url_for('main.customers'))

    return render_template('edit_customer.html', customer=customer)

@main.route('/delete_customer/<int:customer_id>')
def delete_customer(customer_id):
    customer = Customer.query.get_or_404(customer_id)
    db.session.delete(customer)
    db.session.commit()

    flash('Cliente excluído com sucesso!')
    return redirect(url_for('main.customers'))

# Rotas para Pedidos
@main.route('/orders')
def orders():
    orders = Order.query.all()
    return render_template('orders.html', orders=orders)

@main.route('/new_order', methods=['GET', 'POST'])
def new_order():
    customers = Customer.query.all()
    products = Product.query.all()

    if request.method == 'POST':
        customer_id = request.form['customer_id']
        product_id = request.form['product_id']
        quantity = int(request.form['quantity'])
        payment_method = request.form['payment_method']
        status = request.form['status']

        product = Product.query.get(product_id)
        total_price = quantity * product.price

        new_order = Order(
            customer_id=customer_id,
            product_id=product_id,
            quantity=quantity,
            total_price=total_price,
            payment_method=payment_method,
            status=status
        )
        db.session.add(new_order)
        db.session.commit()

        flash('Pedido criado com sucesso!')
        return redirect(url_for('main.orders'))

    return render_template('new_order.html', customers=customers, products=products)

@main.route('/delete_order/<int:order_id>')
def delete_order(order_id):
    order = Order.query.get_or_404(order_id)
    db.session.delete(order)
    db.session.commit()

    flash('Pedido excluído com sucesso!')
    return redirect(url_for('main.orders'))