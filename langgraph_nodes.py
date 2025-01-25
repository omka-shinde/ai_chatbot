# langgraph_nodes.py
from langgraph_nodes import SimpleSQLNode
from database import get_session  # Assuming get_session is in database.py

class FetchProductSupplierNode(SimpleSQLNode):
    def query(self, inputs):
        # The query will search for products and supplier information
        query = f"""
            SELECT p.name, p.category, p.price, s.name AS supplier_name, s.contact_details 
            FROM products p 
            JOIN suppliers s ON p.supplier_id = s.id
            WHERE p.name LIKE '%{inputs['query']}%';
        """
        # Get a new session for querying the database
        session = get_session()
        result = session.execute(query).fetchall()  # Execute the query
        session.close()  # Always close the session

        # Format the result as a dictionary to pass it to the next node
        data = [{"product_name": row[0], "category": row[1], "price": row[2], "supplier_name": row[3], "contact_details": row[4]} for row in result]
        return {"data": data}
