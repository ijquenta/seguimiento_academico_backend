from core.database import select, execute
from core.database import execute, as_string
from web.wsrrhh_service import *
    
def listarMaterias(data):
    return select(f'''SELECT * FROM materia''')

@catchError()
def insertarMateria(data):
    result = {'code': 0, 'message': 'No hay datos disponibles'}, 404
    print("Ivan->")
    print(data)
    try:
        query = sql.SQL(
            '''
            INSERT INTO materia 
            (
                matnom, nivid
            )
            VALUES
            ({materiaNom}, {nivelId})
            '''
            ).format(materiaNom=sql.Literal(data['materiaNom']),
                nivelId=sql.Literal(data['nivelId'])
            )  
        result = execute(as_string(query))
    except Exception as err:
        print(err)
        return {'code': 0, 'message': 'Error: '+ str(err)}, 404
    return result


@catchError()
def actualizarMateria(data):
    result = {'code': 0, 'message': 'No hay datos disponibles'}, 404
    print("Ivan->")
    print(data)
    try:
        query = sql.SQL(
            '''
            UPDATE materia 
            SET
                matnom = {materiaNom},
                nivid = {nivelId}
            WHERE
                matid = {materiaId}
            '''
        ).format(
            materiaNom=sql.Literal(data['materiaNom']),
            nivelId=sql.Literal(data['nivelId']),
            materiaId=sql.Literal(data['materiaId'])
        )
        result = execute(as_string(query))
    except Exception as err:
        print(err)
        return {'code': 0, 'message': 'Error: ' + str(err)}, 404
    return result


"""
@catchError()
def eliminarMateria(materia_id):
    try:
        query = sql.SQL(
            '''
            DELETE FROM materia
            WHERE matid = {materiaId}
            '''
        ).format(materiaId=sql.Literal(materia_id))
        
        result = execute(as_string(query))
        return {'message': 'Materia eliminada exitosamente'}
    except Exception as err:
        print(err)
        return {'code': 0, 'message': 'Error: ' + str(err)}, 404
"""
