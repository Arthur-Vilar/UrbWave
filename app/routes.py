from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import Customer, Address, Product
from app import db

main = Blueprint('main', _name_)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@main.route('/new_customer', methods=['GET', 'POST'])
def new_customer():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        birth_date = request.form['date']
        cpf = request.form['cpf']
        
        new_customer = Customer(name=name, birth_date=birth_date, cpf=cpf, phone=phone, email=email, password=password)
        db.session.add(new_customer)
        db.session.commit()

        # Save Address
        address = Address(
            cep=request.form['cep'],
            number=request.form['n'],
            complement=request.form['complemento'],
            neighborhood=request.form['bairro'],
            city=request.form['city'],
            state=request.form['estado'],
            country=request.form['pais'],
            customer_id=request.form['customer_id']
        )
        db.session.add(address)
        db.session.commit()

        flash('Cadastro realizado com sucesso!')
        return redirect(url_for('main.login'))

    return render_template('new_customer.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['senha']

        # Verificar se o usuário existe e a senha está correta
        customer = Customer.query.filter_by(email=email, password=password).first()
        if customer:
            session['user_id'] = customer.id  # Salvar o ID do usuário na sessão
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Email ou senha incorretos.', 'error')

    return render_template('login.html')