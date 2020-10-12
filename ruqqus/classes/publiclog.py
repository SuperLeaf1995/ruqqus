from sqlalchemy import *
from flask import g

from ruqqus.helpers.base36 import *
from ruqqus.__main__ import Base

class PublicLog(Base):
	__tablename__ = "logs"
	id = Column(BigInteger, primary_key=True)
	author_id = Column(Integer)
	content = Column(String(4095))
	
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	def __repr__(self):
		return f"<BadgeDef(author_id={self.author_id}, content={self.content})>"
		
	@property
	def json(self):
		return {
			'id':self.id,
			'author_id':self.author_id,
			'content':self.content
		}
