import enum
class UserType(enum.Enum):
	STUDENT = 1
	CMO = 2
	AD = 3
	ALLOCATIONTEAM = 4
	SUPERUSER = 5
	ADMIN = 6	

class NatureOfQuery(enum.Enum):
	MEDICAL=1