from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///online_bank.db'
db = SQLAlchemy(app)

# Модель для товаров (услуг) в корзине
class CartItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Добавление товара в корзину
@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    name = request.form.get('name')
    price = float(request.form.get('price'))

    if not name or price <= 0:
        flash('Пожалуйста, введите корректные данные.', 'error')
        return redirect(url_for('index'))

    item = CartItem(name=name, price=price)
    db.session.add(item)
    db.session.commit()

    flash('Товар добавлен в корзину!', 'success')
    return redirect(url_for('cart'))

# Страница корзины
@app.route('/cart')
def cart():
    items = CartItem.query.all()
    total = sum(item.price for item in items)
    return render_template('cart.html', items=items, total=total)

# Удаление товара из корзины
@app.route('/remove_from_cart/<int:item_id>')
def remove_from_cart(item_id):
    item = CartItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    flash('Товар удален из корзины!', 'success')
    return redirect(url_for('cart'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Создание базы данных
    app.run(debug=True)