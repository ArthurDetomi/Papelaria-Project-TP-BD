from persistence.UsuarioDao import UsuarioDao

dao = UsuarioDao()

users = dao.find_all()
print(users[0])

print(dao.find_by_id(1))
print(dao.find_by_id(12))
