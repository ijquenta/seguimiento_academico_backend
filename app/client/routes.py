# apiVersion = "/calculobs_api"
#apiVersion = "/bsocial_api"
apiVersion = "/academico_api"
class Routes:
    index = apiVersion + '/'
    protected = apiVersion + '/secure'

    listarMaterias = apiVersion + '/listarMaterias'

    insertarMateria = apiVersion + '/insertarMateria'

    actualizarMateria = apiVersion + '/actualizarMateria'




    obtenerDatosDocente = apiVersion + '/obtenerDatosDocente' 

    listarBeneficiosDocente = apiVersion + '/listarBeneficiosDocente'

    listarTipoMotivo = apiVersion + '/listarTipoMotivo'

    prueba = apiVersion + '/prueba'

    obtenerDatosModificar = apiVersion + '/obtenerDatosModificar'


    listarTresUltimosMesesRemuneraadosDocente = apiVersion + '/listarTresUltimosMesesRemuneraadosDocente'

    regTresUltMesRemDoc = apiVersion + '/regTresUltMesRemDoc'

    registrarBeneficioNuevo = apiVersion + '/registrarBeneficioNuevo'

    eliminarBeneficio = apiVersion + '/eliminarBeneficio'

    # actualizarBeneficiosSociales = apiVersion + '/actualizarBeneficiosSociales'
    # Ejemplo Insertar Registro en base de datos
    # regRestaurarMes = apiVersion + '/regRestaurarMes'
    