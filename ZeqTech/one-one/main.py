from sqlalchemy import ForeignKey, create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import os

# ----- Database Config -----
engine = create_engine(
    'sqlite:///' + os.path.join(os.path.dirname(os.path.abspath(__file__)), "database.db"),
    echo=True
)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Node(Base):
    __tablename__ = 'nodes'

    id = Column(Integer, primary_key=True)
    value = Column(Integer, nullable=False)
    
    node_id = Column(Integer, ForeignKey('nodes.id'))
    next_node = relationship('Node', remote_side=[id], uselist=False)
    
    def __repr__(self):
        return f"<Node value={self.value}, next node={self.next_node}>>"


Base.metadata.create_all(engine)




node1 = Node(value=1)
node2 = Node(value=2)
node3 = Node(value=3)

node1.next_node = node2
node2.next_node = node3

session.add_all([node1, node2, node3])
session.commit()
