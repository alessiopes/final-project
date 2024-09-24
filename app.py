from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista fittizia di accounts come "database" in memoria
accounts = [
    {'id': 1, 'name': 'John Doe', 'balance': 1000},
    {'id': 2, 'name': 'Jane Smith', 'balance': 2000}
]

# Crea un nuovo account (CREATE)
@app.route('/api/accounts', methods=['POST'])
def create_account():
    data = request.json
    new_account = {
        'id': len(accounts) + 1,  # Auto-increment id
        'name': data['name'],
        'balance': data['balance']
    }
    accounts.append(new_account)
    return jsonify(new_account), 201

# Ottieni i dettagli di un singolo account (READ)
@app.route('/api/accounts/<int:account_id>', methods=['GET'])
def get_account(account_id):
    account = next((acc for acc in accounts if acc['id'] == account_id), None)
    if account:
        return jsonify(account)
    else:
        return jsonify({'message': 'Account not found'}), 404

# Elenca tutti gli account (LIST)
@app.route('/api/accounts', methods=['GET'])
def list_accounts():
    return jsonify(accounts)

# Aggiorna i dettagli di un account esistente (UPDATE)
@app.route('/api/accounts/<int:account_id>', methods=['PUT'])
def update_account(account_id):
    data = request.json
    account = next((acc for acc in accounts if acc['id'] == account_id), None)
    if account:
        account['name'] = data.get('name', account['name'])
        account['balance'] = data.get('balance', account['balance'])
        return jsonify(account)
    else:
        return jsonify({'message': 'Account not found'}), 404

# Elimina un account esistente (DELETE)
@app.route('/api/accounts/<int:account_id>', methods=['DELETE'])
def delete_account(account_id):
    global accounts
    accounts = [acc for acc in accounts if acc['id'] != account_id]
    return jsonify({'message': f'Account {account_id} deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
