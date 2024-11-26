from flask import render_template
from.models import Product

def init__app(app):
    @app.route('/')
    def index():
        return render_template('index.html')
    
    @app.route('/')
    def index():
        products = Product.query.all()  # Recupera todos os produtos
        return render_template('index.html', products=products)
    
    # Rota para criar um novo produto
    @app.route('/product/new', methods=['GET', 'POST'])
    def new_product():
        if request.method == 'POST':
            name = request.form['name']
            price = request.form['price']
            product = Product(name=name, price=float(price))
            db.session.add(product)
            db.session.commit()
            return redirect(url_for('main.index'))
        return render_template('new_product.html')
    
    # Rota para editar um produto existente
    @app.route('/product/edit/<int:id>', methods=['GET', 'POST'])
    def edit_product(id):
        product = Product.query.get_or_404(id)
        if request.method == 'POST':
            product.name = request.form['name']
            product.price = float(request.form['price'])
            db.session.commit()
            return redirect(url_for('main.index'))
        return render_template('edit_product.html', product=product)
    
    # Rota para excluir um produto
    @app.route('/product/delete/<int:id>', methods=['POST'])
    def delete_product(id):
        product = Product.query.get_or_404(id)
        db.session.delete(product)
        db.session.commit()
        return redirect(url_for('main.index'))