window.addEventListener('load', () => {
    const form = document.getElementById('formulario')
    const nombreID = document.getElementById('nombre')
    const apellidoID = document.getElementById('apellidos')
    const edadID = document.getElementById('edad')
    const rutID = document.getElementById('rut')
    const contactoID = document.getElementById('contacto')
    const enfermedadesID = document.getElementById('enfermedades')
    const observacionesID = document.getElementById('observaciones')


    form.addEventListener('submit', (e) => {
        e.preventDefault()
        validaCampos()
        if (validaCampos()) {
            console.log('formulario enviado')
            form.submit();
        }
        else {
            console.log(validaCampos())
            console.log('formulario no enviado')
        }
           
    })
    const validaCampos = () => {
        const nombreValor = nombreID.value.trim()
        const apellido = apellidoID.value.trim()
        const edad = edadID.value
        const rut = rutID.value
        const contacto = contactoID.value
        const enfermedades = enfermedadesID.value
        const observaciones = observacionesID.value


    if (!nombreValor) {
        validaFalla(nombre, 'El nombre no debe estar en blanco')
    }
    else {
        validaOk(nombre)
    }
    if (!apellido) {
        validaFalla(apellidoID, 'El apellido no debe estar en blanco')
    }
    else if (apellido.length <= 3) {
        validaFalla(apellidoID, 'El apellido no debe contener menos de 3 letras.')
    }
    else {
        validaOk(apellidoID)

    }
    if (!edad) {
        validaFalla(edadID, 'La edad no debe estar en blanco')
    }
    else if (edad < 55 || edad > 150) {
        validaFalla(edadID, 'La edad no puede ser menor a 55 o mayor a 150 años')
    }
    else if (isNaN(edad)) {
        validaFalla(edadID, 'La edad debe ser un numero')
    }
    else {
        validaOk(edadID)
    }
    if (!contacto) {
        validaFalla(contactoID, 'El contacto no debe estar en blanco')
    }
    else if (contacto.length <= 7) {
        validaFalla(contactoID, 'El numero de contacto debe ser mayor a 8 digitos')
    }
    else {
        validaOk(contactoID)
    }

    if (rut.length <= 8) {
        validaFalla(rutID, 'El rut no puede ser menor a 8 digitos')
    }
    else {
        validaOk(rutID)
    }
    if (nombreValor && apellido && edad && rut && !isNaN(contacto) ) {
        return true
    }
    else {
        return false
    }

}
    const validaFalla = (input, mensaje) => {
        const formControl = input.parentElement
        const aviso = formControl.querySelector('p')
        aviso.innerText = mensaje   //innerText es para que se vea el texto
        formControl.className = 'form-control falla'
    }
    const validaOk = (input) => {
        const formControl = input.parentElement
        formControl.className = 'form-control ok'
    }

})
