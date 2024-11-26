# from flask import Flask, render_template, request, redirect, url_for
# from models import db, Product

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # Usando SQLite como banco de dados
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db.init_app(app)

# # Rota para listar todos os produtos
# @app.route('/')
# def index():
#     products = Product.query.all()  # Recupera todos os produtos
#     return render_template('index.html', products=products)

# # Rota para adicionar um novo produto
# @app.route('/add', methods=['GET', 'POST'])
# def add_product():
#     if request.method == 'POST':
#         name = request.form['name']
#         description = request.form['description']
#         price = request.form['price']
#         quantity = request.form['quantity']
#         new_product = Product(name=name, description=description, price=float(price), quantity=int(quantity))
#         db.session.add(new_product)
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('add_product.html')

# # Rota para editar um produto
# @app.route('/edit/<int:id>', methods=['GET', 'POST'])
# def edit_product(id):
#     product = Product.query.get_or_404(id)
#     if request.method == 'POST':
#         product.name = request.form['name']
#         product.description = request.form['description']
#         product.price = float(request.form['price'])
#         product.quantity = int(request.form['quantity'])
#         db.session.commit()
#         return redirect(url_for('index'))
#     return render_template('update_product.html', product=product)

# # Rota para excluir um produto
# @app.route('/delete/<int:id>')
# def delete_product(id):
#     product = Product.query.get_or_404(id)
#     db.session.delete(product)
#     db.session.commit()
#     return redirect(url_for('index'))

# # Rota para exibir os detalhes de um produto
# @app.route('/product/<int:id>')
# def show_product(id):
#     product = Product.query.get_or_404(id)
#     return render_template('show_product.html', product=product)

# if __name__ == "_main_":
#     app.run(debug=True)

# from app import app, db
# with app.app_context():
#     db.create_all()