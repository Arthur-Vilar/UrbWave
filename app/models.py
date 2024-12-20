from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def _repr_(self):
        return f'<Product {self.name}>'

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    address = db.relationship('Address', backref='customer', lazy=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    cpf = db.Column(db.String(11), unique=True, nullable=False)

    def _repr_(self):
        return f'<Customer {self.name}>'
    
class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cep = db.Column(db.String(8), nullable=False)
    number = db.Column(db.String(10), nullable=False)
    complement = db.Column(db.String(100))
    neighborhood = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    state = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    total_price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), nullable=False, default='Pendente')  # Status do pedido
    payment_method = db.Column(db.String(50), nullable=False)  # Método de pagamento

    # Relacionamentos
    customer = db.relationship('Customer', backref=db.backref('orders', lazy=True))
    product = db.relationship('Product', backref=db.backref('orders', lazy=True))

    def _repr_(self):
        return f'<Order {self.id} - Cliente: {self.customer.name}, Produto: {self.product.name}>'