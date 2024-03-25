from flask import jsonify, Blueprint, request
from app.services.user_service import UserService

user = Blueprint('user', __name__)
user_schema = UserSchema()
        
# find all users
@user.route('/find_all', methods=['GET'])
def index():
    service = UserService()
    users = service.find_all()
    return jsonify({"users": [user.to_dict() for user in users]}), 200

#find user
@user.route('/find/<int:id>', methods=['GET'])
def find(id):
    service = UserService()
    response_builder = ResponseBuilder()
    response_builder.add_message("Usuario encontrado")\
        .add_status_code(200)\
        .add_data(UserSchema().dump(service.find_by_id(id)))
    return ResponseSchema().dump(response_builder.build()), 200

#delete user
@user.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    service = UserService()
    service.delete(id)
    return {"message": "Usuario eliminado"}, 200

#update user
@user.route('/update/<int:id>', methods=['PUT'])
def update(id):
    service = UserService()
    user_data = request.json
    service.update(id, user_data)
    return {"message": "Usuario actualizado"}, 200

# get all classes
@user.route('/get_classes', methods=['GET'])
def get_all_classes():
    gym_class_service = GymClassService()
    classes = gym_class_service.find_all()
    return {"classes": [gym_class.to_dict() for gym_class in classes]}, 200

#book class
@user.route('/book_class/<int:user_id>/<int:gym_class_id>', methods=['POST'])
def book_gym_class(user_id, gym_class_id):
    booking_service = BookingService()
    command = BookGymClassCommand(booking_service, user_id, gym_class_id)
    command.execute()
    return {"message": "Clase de gimnasio reservada"}, 200

#book cancel
@user.route('/book_cancel/<int:booking_id>', methods=['DELETE'])
def cancel_gym_class(booking_id):
    booking_service = BookingService()
    command = CancelGymClassCommand(booking_service, booking_id)
    command.execute()
    return {"message": "Reserva de clase de gimnasio cancelada"}, 200

#get all bokkings
@user.route('/get_bookings/<int:user_id>', methods=['GET'])
def get_user_bookings(user_id):
    booking_service = BookingService()
    bookings = booking_service.find_all(user_id)
    return {"bookings": [booking.to_dict() for booking in bookings]}, 200