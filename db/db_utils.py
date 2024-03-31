from app import db
from sqlalchemy.sql.expression import Select, CompoundSelect
from sqlalchemy.sql import select
from sqlalchemy import func

MAX_PAGE_SIZE = 100

def execute_query(query):
    """
    Execute the given SQL query using the database session.
    """
    fetch_result = query.is_select
    
    if fetch_result:
        rows = db.session.execute(query)
        result = []
        for row in rows:
            item = {}
            for column in row.keys():
                item[column] = getattr(row, column)
            result.append(item)
        db.session.close()
        return result
    
    else:
    
        db.session.execute(query)
        db.session.commit()
        db.session.close()




def paginate_query(query, page, page_size):
    """
    Constructs a paginated query from a given sql statement. Also adds a companion COUNT
    to the result that will be used by the callers to retrive the total number of records
    matching the filters.

    Args:
        query: An sqlalchemy expression SELECT statement.
        page: An int representing the page number to start the query from.
        page_size: The desired page_size.

    Returns:
        An sqlalchemy expression statement with pagination
        and COUNT as last column

    Raises:
        AssertionError if the query is not a SELECT or if page_size or page are invalid.

    """
    assert isinstance(query, Select) or isinstance(query, CompoundSelect)
    assert page is not None and page >= 0

    assert page_size in range(1, MAX_PAGE_SIZE + 1)
    
    offset = page_size * page
    query_alias = query.alias()
    count_query = select([func.count()]).select_from(query_alias)

    query = query.offset(offset).limit(page_size)
    return query, count_query

